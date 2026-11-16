"""Рисованный стиль. What did I google today? — Funny Christmas presents (обратный отсчёт 5 → 1).

Факты/пояснения:
- Носки и подушки с фото питомца — популярный подарок на заказ.
- Гигантские мармеладные мишки весом около 2,3 кг (5 lb) реально продаются.
- «Уголь» для непослушных: в Италии Бефана (6 января) приносит детям carbone dolce — сладкий уголь из сахара.
- Мини-гольф для туалета — известный шуточный подарок.
- Pet Rock: Гэри Даль, 1975 — продано около 1,5 млн «камней-питомцев» в коробке за несколько месяцев.
Бренды не называем и не рисуем.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.1
P = PASTEL

SCENES = [
    dict(bg=P["pink"], text="What did I google today? Funny Christmas presents. And number one is a real thing people paid for.",
         svg=intro_search("funny christmas gifts")),
    dict(bg=P["mint"], text="No idea what to get someone this year? Here are five gifts that are funny, and kind of useful. Kind of.",
         svg=gift(300, 560, 1.0) + gift(560, 620, 0.8, "#4fa3f7", "#ff8fb1") + gift(760, 560, 0.9, "#2e9d5b", "#ffd23f")
             + hand("top 5", 500, 250, 170, "hand red", -5) + hand("kind of useful", 500, 900, 100, "hand purple", 3)),
    dict(bg=P["blue"], text="Number five. Socks with your pet's face on them. Your dog, on your feet. All winter.",
         svg=hand("#5", 150, 200, 150, "hand blue") + sock(370, 540, 1.1, "#4fa3f7", -8) + sock(650, 560, 1.1, "#ff8fb1", 8)
             + hand("your dog, on your feet", 500, 930, 85, "hand purple", -2)),
    dict(bg=P["yellow"], text="Number four. A giant gummy bear. About five pounds of candy. Roughly the size of a cat.",
         svg=hand("#4", 150, 200, 150, "hand orange") + gummy(370, 600, 1.3) + cat(760, 640, 0.85)
             + hand("same size?!", 760, 300, 100, "hand red", 6) + hand("~5 lb", 370, 940, 120, "hand red", -3)),
    dict(bg=P["lilac"], text="Number three. A lump of coal, for someone who was a little naughty this year. Don't worry, it's actually candy.",
         svg=hand("#3", 150, 200, 150, "hand purple") + coal(500, 500, 1.4) + hand("naughty list", 500, 280, 110, "hand red", -4)
             + hand("(it's candy)", 500, 820, 110, "hand pink", 3)),
    dict(bg=P["peach"], text="Number two. A mini golf set for the toilet. For that one person who spends way too long in the bathroom.",
         svg=hand("#2", 150, 200, 150, "hand red") + toilet(340, 640, 0.95) + golf_set(720, 700, 0.85)
             + hand("hole in one", 500, 950, 100, "hand green", -3)),
    dict(bg=P["mint"], text="And number one. A pet rock. In 1975, a man sold about one and a half million ordinary rocks in a box. As pets. And people loved them.",
         svg=hand("#1", 150, 200, 150, "hand green") + pet_rock(500, 560, 1.4) + hand("1975", 820, 260, 120, "hand purple", 6)
             + hand("1,500,000 sold", 500, 965, 105, "hand red", -3)),
    dict(bg=P["pink"], text="What's the funniest gift you ever got? Tell me in the comments!",
         svg=bubble(500, 300, 800, 220, "#fff", "funniest gift ever?", 80, "hand purple")
             + gift(330, 700, 0.8) + pet_rock(680, 700, 0.6, box=False) + hand("comment!", 500, 960, 120, "hand red", -3)),
]
