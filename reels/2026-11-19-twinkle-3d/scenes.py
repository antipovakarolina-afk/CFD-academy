"""3D-версия «Twinkle, Twinkle, Little Star» для YouTube Shorts (16 c). Свои персонажи: глянцевая звезда, мишка, детская.
Песенка — общественное достояние; музыка — своя (tools/song.py twinkle)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from reel3d import O, L  # noqa

NO_VOICE = True
PAUSE = 0.0
BEAT = 0.5
WH, YE, PK = "#ffffff", "#ffe066", "#ff9fd0"
LINES = [
    [("Twinkle,", 0), ("twinkle,", 2), ("little", 4), ("star", 6)],
    [("How I", 0), ("wonder", 2), ("what you", 4), ("are", 6)],
    [("Up a-", 0), ("bove the", 2), ("world so", 4), ("high", 6)],
    [("Like a", 0), ("diamond", 2), ("in the", 4), ("sky", 6)],
]


def lyric(i):
    xs, ys = [250, 750, 250, 750], [780, 780, 920, 920]
    return [L(w, xs[k], ys[k], 125, YE if k % 2 else WH, (-1) ** k * 3, d=b * BEAT) for k, (w, b) in enumerate(LINES[i])]


ROOM = O("room", 500, 480, 1.0, [True], spin=0)

SCENES = [
    dict(bg="#3b2f86", dur=4.0, text="", moonlight="#c9b8ff",
         objs=[ROOM, O("glossyStar", 430, 330, 1.45, spin=0.6), O("bear", 840, 760, 0.7, spin=0.3), O("sparkles", 500, 400, 1.0, [28, 1], spin=0)],
         labels=[L("Twinkle Twinkle Little Star", 500, -170, 80, PK, -2, d=0.1)] + lyric(0)),
    dict(bg="#3b2f86", dur=4.0, text="", moonlight="#c9b8ff",
         objs=[ROOM, O("bear", 330, 700, 1.05, spin=0.4), O("glossyStar", 720, 260, 1.0, spin=0.6), O("sparkles", 500, 350, 1.0, [22, 2], spin=0)],
         labels=[L("?", 420, 200, 130, PK, -10, d=0.6), L("?", 500, 140, 110, YE, 8, d=1.1)] + lyric(1)),
    dict(bg="#1d1b55", dur=4.0, text="", moonlight="#9fc8ff",
         objs=[O("earth3d", 500, 800, 1.05, spin=0), O("glossyStar", 500, 120, 0.95, spin=0.6), O("sparkles", 500, 400, 1.0, [40, 3, 3.8], spin=0)],
         labels=lyric(2)),
    dict(bg="#2a2160", dur=4.0, text="", moonlight="#bdf0ff",
         objs=[O("crystal", 500, 420, 1.5, spin=1.0), O("glossyStar", 820, 170, 0.6, spin=0.6), O("sparkles", 500, 420, 1.0, [35, 4], spin=0)],
         labels=lyric(3)),
]
