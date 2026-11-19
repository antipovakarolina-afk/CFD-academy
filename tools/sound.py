"""Звуковое оформление рилса: эффекты на сменах картинок + тихая калимба под голосом.

Запуск (интерпретатор earshot, в нём есть банк звуков):
    /root/.local/share/uv/tools/earshot/bin/python tools/sound.py reels/<папка>/scenes.py
Берёт output/.work-<папка>/ (собранный tools/reel.py) и пишет output/<папка>-sound.mp4.

Сцены, где на картинке крупно год (цифры), получают «звоночек» (celesta), последняя — колокольчик,
остальные — мягкий «плоп». Музыка: калимба, C–Am–F–G, ~84 удара в минуту, приглушается под голосом.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

from earshot.forge import bank

ROOT = Path(__file__).resolve().parent.parent
SR = 48000
BPM = 84
CHORDS = [("C4", "E4", "G4", "C5"), ("A3", "C4", "E4", "A4"), ("F3", "A3", "C4", "F4"), ("G3", "B3", "D4", "G4")]
MUSIC_DB = -27.0     # уровень музыки (dBFS пик ноты) относительно голоса ~ -1 dBFS
SFX_DB = {"pop": -9.0, "bell": -12.0, "end": -10.0, "thump": -8.0}


def render(sound, seed=0, pitch=None, peak_db=-1.0):
    y, meta = bank.render(sound, seed=seed, pitch=pitch, peak_db=peak_db, sr=SR)
    y = np.asarray(y, np.float32)
    if y.ndim == 1:
        y = np.stack([y, y], 1)
    return y, meta


def add(buf, y, t, gain_db=0.0, pan=0.0):
    i = int(round(t * SR))
    if i < 0:
        y, i = y[-i:], 0
    n = min(len(y), len(buf) - i)
    if n <= 0:
        return
    g = 10 ** (gain_db / 20)
    lr = np.array([min(1, 1 - pan), min(1, 1 + pan)], np.float32)
    buf[i:i + n] += y[:n] * g * lr


NOTE = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def hz(n):
    return 440.0 * 2 ** ((NOTE[n[0]] + 12 * (int(n[-1]) + 1) - 69) / 12)


def pad_note(f, dur, detune=0.006, bright=5):
    t = np.arange(int(dur * SR)) / SR
    y = np.zeros((len(t), 2), np.float32)
    for ch, d in enumerate((-detune, detune)):
        for k in range(1, bright + 1):
            y[:, ch] += np.sin(2 * np.pi * f * (1 + d) * k * t + k) / k ** 1.6
    env = np.minimum(1, t / 0.9) * np.minimum(1, (dur - t) / 1.2).clip(0, 1)
    return (y * env[:, None] * 0.25).astype(np.float32)


def dark_music(total):
    """тёмный синтезаторный фон: Am – F – C – G, мягкий бас и тихий пульс"""
    bpm = 92
    bar = 4 * 60 / bpm
    prog = [("A2", "A3", "C4", "E4"), ("F2", "F3", "A3", "C4"), ("C3", "G3", "C4", "E4"), ("G2", "G3", "B3", "D4")]
    n = int((total + 3) * SR)
    m = np.zeros((n, 2), np.float32)
    t, k = 0.0, 0
    while t < total + 1:
        ch = prog[k % 4]
        for j, note in enumerate(ch):
            y = pad_note(hz(note), 2 * bar + 1.0, bright=2 if j == 0 else 5)
            add(m, y, t, -6 if j == 0 else -12)
        t += 2 * bar
        k += 1
    kick = render("cut_hit/kick", seed=0, pitch="A1")
    tick = render("hover_tick/air", seed=0)
    beat = 60 / bpm
    b, i = 4 * bar, 0                      # пульс вступает после первого такта
    while b < total:
        add(m, kick[0], b - kick[1]["onset_s"], -20)
        add(m, tick[0], b + beat / 2 - tick[1]["onset_s"], -30, pan=(-0.4, 0.4)[i % 2])
        b += beat
        i += 1
    return m


def scene_starts(work):
    sc = json.loads((work / "scenes.json").read_text())
    return [x["start"] for x in sc], sc[-1]["start"] + sc[-1]["dur"]


def main(spec):
    spec = Path(spec).resolve()
    name = spec.parent.name
    work = ROOT / "output" / f".work-{name}"
    video = ROOT / "output" / f"{name}.mp4"
    starts, total = scene_starts(work)
    texts = re.findall(r'svg=.*', spec.read_text())  # строки с картинками, по сцене
    big_year = [bool(re.search(r'hand\("1\d{3}"', s)) for s in texts]

    n = int((total + 2) * SR)
    music = np.zeros((n, 2), np.float32)
    sfx = np.zeros((n, 2), np.float32)

    dark = bool(re.search(r'^MUSIC\s*=\s*"dark"', spec.read_text(), re.M))
    # музыка: арпеджио калимбы, по 4 удара на аккорд (или тёмный синт-фон)
    if dark:
        music = dark_music(total)[:n] * 10 ** (-8 / 20)
    m_bpm = re.search(r'^BPM\s*=\s*(\d+)', spec.read_text(), re.M)   # темп музыки из сценария
    beat = 60 / (int(m_bpm.group(1)) if m_bpm else BPM)
    cache = {}
    k = 0
    t = 0.0
    while not dark and t < total + 0.5:
        chord = CHORDS[(k // 4) % len(CHORDS)]
        for j, note in enumerate((chord[0], chord[2], chord[1], chord[3]) if k % 2 else chord[:2]):
            key = (note, (k + j) % 3)
            if key not in cache:
                cache[key] = render("pluck/kalimba_soft", seed=key[1], pitch=note)[0]
            add(music, cache[key], t + j * beat / (2 if k % 2 == 0 else 4), MUSIC_DB, pan=(-0.3, 0.3)[(k + j) % 2])
        k += 1
        t += beat
    # плавное начало и конец музыки
    fade = int(1.5 * SR)
    music[:fade] *= np.linspace(0, 1, fade)[:, None]
    end = int(total * SR)
    music[end - fade:end] *= np.linspace(1, 0, fade)[:, None]
    music[end:] = 0

    # эффекты на сменах картинок
    if dark:
        whoosh = [render("fit/whoosh.short/bamboo_swish", seed=s_) for s_ in range(3)]
        blip = [render("ui_pop/soft", seed=s_) for s_ in range(3)]
        ding = render("notify/m0", seed=0, pitch="A4")
        for i, t in enumerate(starts):
            if i > 0:
                y, m = whoosh[i % 3]
                add(sfx, y, t - m["peak_s"], -12, pan=(-0.3, 0.3)[i % 2])
            y, m = blip[i % 3]
            add(sfx, y, t + 0.35 - m["onset_s"], -16)
        y, m = ding
        add(sfx, y, starts[-1] + 0.6 - m["onset_s"], -14)
    pop = [render("fit/pop/mouth_plop", seed=s) for s in range(4)]
    bell = [render("mallet/celesta", seed=s, pitch="C6") for s in range(2)]
    ding = render("notify/m0", seed=0, pitch="C5")
    thump = render("pro_pop_in/deep", seed=0)
    for i, t in enumerate(starts if not dark else []):
        if i == len(starts) - 1:
            y, m = ding
            add(sfx, y, t - m["onset_s"], SFX_DB["end"])
        elif i == 0 or (i < len(big_year) and big_year[i]):
            y, m = bell[i % 2]
            add(sfx, y, t - m["onset_s"], SFX_DB["bell"], pan=0.15)
            y, m = thump
            add(sfx, y, t - m["onset_s"], SFX_DB["thump"])
        else:
            y, m = pop[i % 4]
            add(sfx, y, t - m["onset_s"], SFX_DB["pop"], pan=(-0.2, 0.2)[i % 2])

    mw, sw = work / "music.wav", work / "sfx.wav"
    sf.write(mw, music, SR, subtype="PCM_24")
    sf.write(sw, sfx, SR, subtype="PCM_24")

    out = ROOT / "output" / f"{name}-sound.mp4"
    flt = ("[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,asplit=2[v][vk];"
           "[1:a][vk]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400[m];"
           "[v][m][2:a]amix=inputs=3:normalize=0,alimiter=limit=0.70:level=disabled,loudnorm=I=-14:TP=-2:LRA=11,aresample=48000[a]")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(video), "-i", str(mw), "-i", str(sw),
                    "-filter_complex", flt, "-map", "0:v", "-map", "[a]", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", "-movflags", "+faststart", str(out)],
                   check=True)
    print("Готово:", out, f"({len(starts)} сцен, эффекты на", len(starts) - 1, "сменах)")


if __name__ == "__main__":
    main(sys.argv[1])
