"""What did I google today? — How was Nvidia created?

Факты (сверено в интернете 16.11.2026, см. источники в ответе):
- 1993, Сан-Хосе: Дженсен Хуанг, Крис Малаховски, Кёртис Прием обсуждали идею в кабинке закусочной Denny's
  (2484 Berryessa Road). Компания зарегистрирована 5 апреля 1993.
- Хуанг подростком работал в Denny's (мыл посуду / помощник официанта).
- Стартовый капитал — около $40 000 (так обычно пишут; первичных документов нет).
- Название: файлы «NV» (next version) + латинское invidia — «зависть».
- Первый чип NV1 (1995) не продавался; неофициальный девиз — «our company is thirty days from going out of business».
- 1997: RIVA 128 спас компанию. 1999: GeForce 256 — «первый в мире GPU». Потом GPU стали основой обучения ИИ.
Без конкретной рыночной стоимости — цифры быстро устаревают.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.08
P = PASTEL
G = NV_GREEN

SCENES = [
    dict(bg=P["blue"], text="What did I google today? How was Nvidia created?",
         svg=intro_search("how was nvidia created?")),
    dict(bg=P["peach"], text="It all started in nineteen ninety three, in a booth at Denny's. A cheap American diner in San Jose.",
         svg=diner(500, 620, 1.0) + mug(400, 560, 0.6, "#4fa3f7") + mug(600, 560, 0.6, "#ffd23f")
             + hand("1993", 500, 220, 170, "hand red", -4) + hand("a diner booth", 500, 950, 90, "hand", 3)),
    dict(bg=P["yellow"], text="Three engineers, Jensen Huang, Chris Malachowsky and Curtis Priem, ordered coffee and talked about one big idea.",
         svg=mug(220, 560, 1.0, "#e63946", "smile") + mug(500, 560, 1.0, G, "o") + mug(780, 560, 1.0, "#4fa3f7", "think")
             + hand("Jensen", 220, 760, 80, "hand red") + hand("Chris", 500, 760, 80, "hand green") + hand("Curtis", 780, 760, 80, "hand blue")
             + hand("one big idea", 500, 280, 110, "hand purple", -3) + bulb(870, 240, 0.6)),
    dict(bg=P["night"], text="The idea: special chips that make video game graphics fast and beautiful.",
         svg=screen_cube(500, 430, 1.3) + chip(500, 820, 0.8, "3D") + star(160, 250, 1.2) + star(860, 680, 1.0, "#ff8fb1")),
    dict(bg=P["pink"], text="Fun fact: Jensen worked at Denny's as a teenager. He washed dishes there!",
         svg=plates(500, 640, 1.6) + hand("fun fact", 500, 220, 120, "hand pink", -5) + hand("dishwasher", 500, 900, 110, "hand blue", 3)),
    dict(bg=P["mint"], text="They started with about forty thousand dollars.",
         svg=moneybag(500, 560, 1.6) + hand("~$40,000", 500, 900, 140, "hand green", -3)),
    dict(bg=P["lilac"], text="The name came from files called N V, for next version. Then they found the Latin word invidia. It means envy.",
         svg=hand("NV", 500, 260, 200, "hand") + '<path class="ln" style="stroke-width:9" d="M500 320 v90 M470 380 l30 35 l30 -35"/>'
             + hand("invidia", 500, 580, 170, "hand purple", -3) + hand("= envy", 500, 800, 140, "hand green", 3)),
    dict(bg=P["night"], text="But their first chip flopped. The company almost went bankrupt. Their unofficial motto was: we are thirty days from going out of business.",
         svg=chip(500, 430, 1.1, "NV1", mark=False) + hand("30 days left", 500, 830, 130, "hand red", -4)),
    dict(bg=P["yellow"], text="Then in nineteen ninety seven, a new chip called RIVA one twenty eight finally sold. They were saved!",
         svg=chip(470, 520, 1.3, "RIVA", mark=True) + hand("1997", 500, 210, 170, "hand orange", -4) + hand("saved!", 500, 900, 130, "hand green", 3)),
    dict(bg=P["blue"], text="In nineteen ninety nine they released the GeForce two fifty six, and called it the world's first G P U.",
         svg=chip(500, 520, 1.3, "GPU") + hand("1999", 500, 210, 170, "hand blue", -4) + hand("world's first GPU", 500, 900, 105, "hand purple", 2)),
    dict(bg=P["night"], text="Years later, it turned out these chips are perfect for training artificial intelligence.",
         svg=brain(330, 520, 1.3) + chip(760, 560, 0.8, "AI") + '<path class="ln" style="stroke:#ffd23f;stroke-width:9" d="M520 540 h110 M600 510 l30 30 l-30 30"/>'
             + hand("AI boom", 500, 880, 140, "hand orange", -3)),
    dict(bg=P["mint"], text="Today, Nvidia is one of the most valuable companies in the world. And it all started at a diner table. Not financial advice, just a fun story!",
         svg=chart_up(500, 470, 1.4) + mug(830, 820, 0.55, "#e63946") + hand("from a diner", 400, 820, 110, "hand red", -4)
             + hand("not financial advice", 500, 960, 60, "hand")),
]
