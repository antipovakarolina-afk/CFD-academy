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

    # музыка: арпеджио калимбы, по 4 удара на аккорд
    beat = 60 / BPM
    cache = {}
    k = 0
    t = 0.0
    while t < total + 0.5:
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
    pop = [render("fit/pop/mouth_plop", seed=s) for s in range(4)]
    bell = [render("mallet/celesta", seed=s, pitch="C6") for s in range(2)]
    ding = render("notify/m0", seed=0, pitch="C5")
    thump = render("pro_pop_in/deep", seed=0)
    for i, t in enumerate(starts):
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
