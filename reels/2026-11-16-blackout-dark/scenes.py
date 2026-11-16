"""Тёмный стиль. What is a blackout? (факты — см. reels/2026-11-16-blackout/scenes.py)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from dark import *  # noqa

VOICE = "af_heart"
SPEED = 1.12
MUSIC = "dark"

SCENES = [
    dict(title="WHAT IS A BLACKOUT?", sub="explained in 60 seconds",
         text="Everyone is talking about *blackouts* right now. So what actually happens when the lights go out?",
         svg=item(i_city(500, 760, 1.05, lit=True)) + item(i_bulb(500, 230, 1.1, on=False))),
    dict(title="THE WORD", sub="it started in the theatre",
         text="The word comes from the *theatre.* A blackout meant every stage light switched off at once.",
         svg=item(i_stage(500, 520, 1.0)) + item(pill("LIGHTS: OFF", 500, 520, RED, 40))),
    dict(title="THE GRID", sub="power in = power used",
         text="The power grid has to stay *perfectly balanced.* Every second, power made must equal power used.",
         svg=item(scale_balance(500, 520, 1.1, i_tower(0, -60, 0.35, BLUE), i_bulb(0, -40, 0.6)))
             + item(label("power made", 170, 900, BLUE, 26) + label("power used", 830, 900, YELLOW, 26))),
    dict(title="50 HERTZ", sub="the heartbeat of the grid",
         text="That balance keeps the grid at *50 hertz.* If it drifts too far, power plants switch off to protect themselves.",
         svg=item(card(160, 90, 680, 260, "grid frequency", GREEN) + count(50.0, 500, 290, 150, GREEN, "", " Hz", 1, 0))
             + item(sine(150, 520, 700, 40, 4, BLUE)) + item(sine(150, 760, 700, 25, 5, RED, grow=1.0))
             + item(label("normal", 150, 610, BLUE, 24, "start") + label("unstable", 150, 920, RED, 24, "start"))),
    dict(title="THE DOMINO EFFECT", sub="cascading failure",
         text="One plant goes down, the others get overloaded, and they *fall like dominoes.*",
         svg="".join(item(i_tower(170 + k * 165, 520, 0.6, RED if k < 3 else WHITE)) for k in range(5))
             + item(arrow(150, 860, 850, 860, RED, 7))),
    dict(title="USA & CANADA · 2003", sub="a software bug + trees",
         text="In 2003, *50 million* people lost power. It started with a software bug, and power lines touching trees.",
         svg=item(card(110, 60, 780, 300, "people without power", YELLOW) + count(50000000, 500, 270, 104, YELLOW))
             + item(i_tower(330, 690, 0.75)) + item(i_tree(640, 700, 1.0))
             + item(pill("BUG IN THE ALARM SOFTWARE", 500, 960, RED, 28))),
    dict(title="INDIA · 2012", sub="the biggest blackout ever",
         text="The biggest blackout in history? India, 2012. More than *600 million* people.",
         svg=item(bars(180, 820, 640, 600, [50, 600], ["USA 2003", "INDIA 2012"], [BLUE, YELLOW], "", "M"))),
    dict(title="BLACKOUT KIT", sub="what to keep at home",
         text="Keep a simple kit. A *power bank,* a *flashlight,* water, and a charged phone. Flashlights are safer than candles.",
         svg=checklist(220, 230, [("Power bank", True), ("Flashlight", True), ("Water", True),
                                  ("Charged phone", True), ("Candles", False)], 140, 60)),
    dict(title="YOUR TURN", sub="comment below",
         text="What's in *your* kit? Tell me in the comments. And stay safe.",
         svg=item(i_phone(330, 480, 1.4, BLUE)) + item(i_battery(680, 480, 1.4, 0.85))
             + item(pill("STAY SAFE", 500, 900, GREEN, 44))),
]
