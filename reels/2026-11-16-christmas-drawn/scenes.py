"""Рисованный стиль. What did I google today? — Why is Christmas on December 25?
Факты — см. reels/2026-11-16-christmas-date/scenes.py (без 7 января и Украины).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.1
P = PASTEL

SCENES = [
    dict(bg=P["blue"], text="What did I google today? Why is Christmas on December 25? And fact three surprised me.",
         svg=intro_search("why december 25?")),
    dict(bg=P["pink"], text="Here's the thing. The Bible never actually gives a date. Not the day, not even the month.",
         svg=open_book(500, 520, 1.6) + hand("date?", 500, 230, 140, "hand red", -5) + qmarks(700, 880)),
    dict(bg=P["yellow"], text="Fact one. The first record of Christmas on December 25 comes from Rome, in the year 336.",
         svg=hand("#1", 150, 200, 150, "hand orange") + cal_page(500, 520, 1.2) + hand("Rome, 336", 500, 900, 140, "hand purple", -3)),
    dict(bg=P["night"], text="Fact two. One theory: it's right after the winter solstice. The darkest days are over, and the light comes back.",
         svg=hand("#2", 150, 200, 150, "hand orange") + snow(18, 3) + sun(500, 480, 120)
             + hand("shortest day: Dec 21", 500, 790, 85, "hand") + hand("light comes back", 500, 920, 100, "hand orange", -3)),
    dict(bg=P["mint"], text="Fact three. Writing Xmas isn't rude. The X is the Greek letter Chi, the first letter of Christ in Greek.",
         svg=hand("#3", 150, 200, 150, "hand green") + hand("Xmas", 500, 420, 230, "hand red", -4)
             + '<path class="ln" style="stroke-width:9" d="M500 470 v90 M470 530 l30 35 l30 -35"/>' + hand("X = Chi", 500, 760, 160, "hand green", 3)),
    dict(bg=P["peach"], text="Fact four. Coca-Cola did not invent the red Santa. He was already wearing red years before their 1931 ads.",
         svg=hand("#4", 150, 200, 150, "hand red") + santa_hat(340, 520, 1.1) + soda(730, 540, 1.0)
             + hand("myth!", 500, 900, 140, "hand red", -4)),
    dict(bg=P["lilac"], text="Fact five. Jingle Bells was the first song ever played in space. Two astronauts, a harmonica, and tiny bells. 1965.",
         svg=hand("#5", 150, 200, 150, "hand purple") + star(820, 250, 1.1) + star(640, 300, 0.7, "#ff8fb1")
             + rocket(330, 560, 0.9) + jingle_bell(720, 480, 0.8) + note(760, 760, 0.8) + hand("1965", 500, 940, 120, "hand blue", -3)),
    dict(bg=P["pink"], text="What's your favorite Christmas tradition? Tell me in the comments!",
         svg=bubble(500, 300, 800, 220, "#fff", "your favorite tradition?", 75, "hand purple")
             + xtree(330, 730, 0.6, lights=True) + santa_hat(700, 700, 0.7) + hand("comment!", 500, 960, 120, "hand red", -3)),
]
