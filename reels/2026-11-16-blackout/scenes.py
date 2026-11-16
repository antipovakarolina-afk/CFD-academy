"""What did I google today? — What is a blackout? (спокойный, полезный тон; без политики и шуток про войну)

Факты:
- «Blackout» — изначально театральный термин: полностью погасить свет на сцене (начало XX века);
  потом — затемнение городов во время войн.
- Энергосистема должна каждую секунду держать баланс производства и потребления; частота 50 Гц (в США 60 Гц).
  При сильном сбое станции отключаются для защиты — каскадом.
- 14 августа 2003, северо-восток США и Онтарио: ~50 млн человек; причины — ошибка в программе тревог
  у энергокомпании и линии, провисшие на деревья в Огайо.
- 30–31 июля 2012, Индия: крупнейший блэкаут в истории, ~600+ млн человек.
- Набор на случай отключений: павербанк, фонарик (не свечи — риск пожара), вода, заряженный телефон.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.08
P = PASTEL

SCENES = [
    dict(bg=P["blue"], text="What did I google today? What actually is a blackout? Everyone's talking about it, so let's figure it out.",
         svg=intro_search("what is a blackout?")),
    dict(bg=P["night"], text="The word comes from the theatre. A blackout was when all the stage lights went off at once.",
         svg=curtains(500, 560, 1.0) + hand("lights off!", 500, 560, 120, "hand orange", -4)),
    dict(bg=P["yellow"], text="So why does the power go out? The grid has to stay perfectly balanced every single second. Power in must equal power used.",
         svg=balance(500, 520, 1.3, powerbank(-220, -60, 0.5), bulb(220, -60, 0.6)) + hand("balance", 500, 900, 130, "hand blue", -3)),
    dict(bg=P["mint"], text="That balance keeps the electricity at fifty hertz. If it drifts too far, power plants switch off to protect themselves. One after another, like dominoes.",
         svg=hand("50 Hz", 500, 230, 170, "hand green", -3) + wave(500, 450, 1.3) + wave(500, 660, 1.3, "#d7263d", bad=True)
             + "".join(f'<rect class="ln" x="{200 + i * 120}" y="860" width="40" height="110" style="fill:#ffd23f" transform="rotate({i * 18} {220 + i * 120} 970)"/>' for i in range(5))),
    dict(bg=P["peach"], text="Fact: in two thousand three, fifty million people in the US and Canada lost power. It started with a software bug and power lines touching trees.",
         svg=powerline(500, 520, 0.95, tree=True, spark=True) + hand("2003", 820, 230, 140, "hand red", 6)
             + hand("50 million people", 500, 950, 95, "hand purple", -2)),
    dict(bg=P["night"], text="And the biggest blackout in history? India, twenty twelve. More than six hundred million people. That's almost twice the population of the US.",
         svg=skyline(500, 760, 1.0, lit=False) + hand("2012", 500, 230, 170, "hand orange", -4) + hand("600,000,000+", 500, 900, 120, "hand pink", -2)),
    dict(bg=P["lilac"], text="So here's a simple blackout kit. A charged power bank, a flashlight, water, and a full phone battery. Flashlights are safer than candles.",
         svg=powerbank(200, 450, 1.0) + flashlight(420, 640, 0.7, -15) + bottle(640, 470, 1.0) + candle_x(850, 520, 0.6)
             + hand("blackout kit", 500, 170, 130, "hand purple", -3) + hand("safer than candles", 500, 900, 95, "hand red", 2)),
    dict(bg=P["pink"], text="What's in your blackout kit? Share your tips in the comments. Stay safe!",
         svg=bubble(500, 300, 800, 220, "#fff", "what's in your kit?", 80, "hand purple")
             + powerbank(330, 680, 0.9) + flashlight(640, 780, 0.6, 25) + hand("stay safe", 500, 960, 120, "hand red", -3)),
]
