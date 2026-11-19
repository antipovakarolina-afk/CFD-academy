"""Простая аранжировка детской песенки: мелодия на калимбе/челесте + мягкие аккорды + лёгкий ритм.
    /root/.local/share/uv/tools/earshot/bin/python tools/song.py <папка рилса> twinkle
Пишет output/.work-<папка>/song.wav и сводит с видео в output/<папка>-song.mp4.
"""
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf
from earshot.forge import bank

ROOT = Path(__file__).resolve().parent.parent
SR = 48000
NOTE = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}

SONGS = {
    # (нота, длительность в долях); 120 BPM
    "twinkle": dict(bpm=120, melody=[
        ("C5", 1), ("C5", 1), ("G5", 1), ("G5", 1), ("A5", 1), ("A5", 1), ("G5", 2),
        ("F5", 1), ("F5", 1), ("E5", 1), ("E5", 1), ("D5", 1), ("D5", 1), ("C5", 2),
        ("G5", 1), ("G5", 1), ("F5", 1), ("F5", 1), ("E5", 1), ("E5", 1), ("D5", 2),
        ("G5", 1), ("G5", 1), ("F5", 1), ("F5", 1), ("E5", 1), ("E5", 1), ("D5", 2)],
        chords=[("C", 4), ("F", 2), ("C", 2), ("F", 2), ("C", 2), ("G", 2), ("C", 2),
                ("C", 2), ("F", 2), ("C", 2), ("G", 2), ("C", 2), ("F", 2), ("C", 2), ("G", 2)]),
}
CHORD = {"C": ("C3", "E4", "G4", "C4"), "F": ("F2", "F4", "A4", "C4"), "G": ("G2", "G4", "B3", "D4")}


def hz(n):
    return 440.0 * 2 ** ((NOTE[n[0]] + 12 * (int(n[-1]) + 1) - 69) / 12)


def render(sound, **kw):
    y, meta = bank.render(sound, sr=SR, **kw)
    y = np.asarray(y, np.float32)
    return (np.stack([y, y], 1) if y.ndim == 1 else y), meta


def add(buf, y, t, db=0.0, pan=0.0):
    i = int(t * SR)
    n = min(len(y), len(buf) - i)
    if n > 0:
        buf[i:i + n] += y[:n] * 10 ** (db / 20) * np.array([1 - max(0, pan), 1 + min(0, pan)], np.float32)


def pad(f, dur):
    t = np.arange(int(dur * SR)) / SR
    y = sum(np.sin(2 * np.pi * f * k * t) / k ** 2 for k in (1, 2, 3))
    env = np.minimum(1, t / 0.08) * np.exp(-t * 1.2)
    return np.stack([y * env, y * env], 1).astype(np.float32) * 0.3


def main(folder, song):
    S = SONGS[song]
    beat = 60 / S["bpm"]
    total = sum(d for _, d in S["melody"]) * beat
    buf = np.zeros((int((total + 1.5) * SR), 2), np.float32)
    t, cache = 0.0, {}
    for k, (n, d) in enumerate(S["melody"]):                       # мелодия: калимба + тихая челеста октавой
        key = (n, k % 2)
        if key not in cache:
            cache[key] = (render("pluck/kalimba", pitch=n, seed=k % 2)[0], render("mallet/celesta", pitch=n, seed=k % 2)[0])
        add(buf, cache[key][0], t, -3)
        add(buf, cache[key][1], t, -16, 0.2)
        t += d * beat
    t = 0.0
    for c, d in S["chords"]:                                       # аккорды: мягкий «пад» + бас
        for j, n in enumerate(CHORD[c]):
            add(buf, pad(hz(n), d * beat + 0.4), t, -14 if j else -10, (-0.3, 0.3)[j % 2])
        t += d * beat
    tick = render("hover_tick/air", seed=0)[0]
    kick = render("cut_hit/kick", seed=0, pitch="C2")[0]
    for b in range(int(total / beat)):                             # лёгкий ритм
        add(buf, kick, b * beat, -22 if b % 2 else -18)
        add(buf, tick, b * beat + beat / 2, -26, (-0.4, 0.4)[b % 2])
    fade = int(0.6 * SR)
    buf[int(total * SR):] *= 0
    buf[int(total * SR) - fade:int(total * SR)] *= np.linspace(1, 0.4, fade)[:, None]
    buf = buf[:int(total * SR)]
    work = ROOT / "output" / f".work-{folder}"
    wav = work / "song.wav"
    sf.write(wav, buf / max(1e-6, np.abs(buf).max()) * 0.8, SR, subtype="PCM_24")
    out = ROOT / "output" / f"{folder}-song.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(ROOT / "output" / f"{folder}.mp4"), "-i", str(wav),
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", "loudnorm=I=-14:TP=-2:LRA=11",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)], check=True)
    print("Готово:", out, f"({total:.1f} c)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
