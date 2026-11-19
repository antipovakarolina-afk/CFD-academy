"""YouTube Shorts, 16 c. «Twinkle, Twinkle, Little Star» — sing-along (народная песенка, общественное достояние).
Мелодия и аранжировка — свои (tools/song.py). Слова появляются в такт: 120 BPM, 4 строки по 8 долей = 16 с.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

NO_VOICE = True
PAUSE, INTRO, MOTION_FPS = 0.0, 0.35, 15
NIGHT = "#2a2160"
BEAT = 0.5

# (слово, доля начала) для каждой строки
LINES = [
    [("Twinkle,", 0), ("twinkle,", 2), ("little", 4), ("star", 6)],
    [("How I", 0), ("wonder", 2), ("what you", 4), ("are", 6)],
    [("Up a-", 0), ("bove the", 2), ("world so", 4), ("high", 6)],
    [("Like a", 0), ("diamond", 2), ("in the", 4), ("sky", 6)],
]


def lyric(line, y=900, size=125, cls="hand"):
    """слова строки появляются по очереди в такт; позиции — в два ряда, чтобы не тесно"""
    out = ""
    xs = [250, 750, 250, 750]
    ys = [y - 140, y - 140, y, y]
    for k, (w, beat) in enumerate(line):
        out += mv(mv(hand(w, xs[k], ys[k], size, cls, (-1) ** k * 3), "appear", d=beat * BEAT), "pulse", a=0.06, p=0.5, d=beat * BEAT + 0.45)
    return out


TWINKLES = "".join(mv(sparkle(x, y, sc), "pulse", a=0.5, p=0.45 + (k % 3) * 0.15, d=0.05 * k)
                   for k, (x, y, sc) in enumerate([(120, 120, 0.8), (880, 160, 1.0), (180, 520, 0.6), (850, 560, 0.7), (520, 60, 0.6), (60, 330, 0.5), (940, 380, 0.6)]))

SCENES = [
    dict(bg=NIGHT, dur=4.0, text="",
         svg=TWINKLES + mv(mv(happy_star(500, 330, 1.2), "spin", p=8), "pulse", a=0.08, p=0.5)
             + hand("Twinkle Twinkle Little Star", 500, 600, 62, "hand orange", -2) + lyric(LINES[0])),
    dict(bg=NIGHT, dur=4.0, text="",
         svg=TWINKLES + mv(happy_star(700, 230, 0.75), "bob", a=20, p=0.5) + person(330, 470, 0.75, "o", "up")
             + mv(qmarks(420, 200), "wiggle", a=10, p=0.5) + lyric(LINES[1])),
    dict(bg=NIGHT, dur=4.0, text="",
         svg=TWINKLES + mv(happy_star(500, 160, 0.7), "bob", a=26, p=0.5) + mv(earth(500, 580, 150), "spin", p=6)
             + mv('<path class="ln" style="stroke:#ffd23f;stroke-width:6;stroke-dasharray:4 18" d="M500 300 V420"/>', "pulse", a=0.1, p=0.5)
             + lyric(LINES[2])),
    dict(bg=NIGHT, dur=4.0, text="",
         svg=TWINKLES + mv(mv(diamond(500, 380, 1.3), "wiggle", a=6, p=0.5), "pulse", a=0.06, p=0.5)
             + mv(sparkle(330, 250, 1.1), "spin", p=1.2) + mv(sparkle(690, 520, 1.0), "spin", p=1.0)
             + lyric(LINES[3])),
]
