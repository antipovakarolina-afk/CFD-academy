"""What did I google today? — How many nuts a day (advent calendar).

Факты: ~30 г орехов в день (горсть) — рекомендация NHS / многих диет. 1 oz (28 г) ≈ 23 миндаля,
14 половинок грецкого, 18 кешью (USDA). Бразильский орех: 1–2 шт. из‑за селена. 30 г ≈ 160–200 ккал.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

SCENES = [
    dict(text="What did I google today?",
         svg=person(430, 620, 1.1, "o", "front") + phone(470, 600, 0.8) + qmarks(640, 260)),
    dict(text="How many nuts can you actually eat in one day?",
         svg=hand("how many nuts?", 500, 330, 120) + walnut(330, 620, 1.3) + almond(560, 640, 1.3, 20) + cashew(740, 620, 1.2)),
    dict(text="Because I'm making an advent calendar. Twenty four tiny boxes, and I want to put nuts in every single one.",
         svg=calendar(500, 520, 130) + hand("24", 850, 900, 150, "hand red", -8)),
    dict(text="And then I thought. Wait. Is there a limit?",
         svg=person(380, 600, 1.1, "worry", "chin") + hand("limit?", 720, 360, 150, "hand red", -6)),
    dict(text="Turns out, there is. About thirty grams a day. That's one small handful.",
         svg=hand("30 g", 500, 330, 220) + g(500, 650, 1, '<path class="ln" d="M-180 -20 q0 140 180 140 q180 0 180 -140 z" fill="#fff"/>')
         + almond(420, 610, 0.8, -20) + walnut(520, 600, 0.7) + cashew(610, 615, 0.7, 30) + hand("= one handful", 500, 900, 90)),
    dict(text="That's around twenty almonds. Or fourteen walnut halves. Or eighteen cashews.",
         svg=almond(220, 330, 1.1) + hand("~20", 450, 360, 110)
         + walnut(220, 560, 1.0) + hand("14 halves", 530, 590, 110)
         + cashew(220, 800, 1.1) + hand("~18", 450, 830, 110)),
    dict(text="But Brazil nuts are different. Only one or two a day. They are so full of selenium that a handful is way too much.",
         svg=brazil(330, 520, 2.2, -10) + brazil(560, 540, 2.2, 12) + hand("1–2 only!", 740, 300, 130, "hand red", -8)
         + hand("selenium", 760, 820, 90)),
    dict(text="And thirty grams of nuts is already about a hundred and eighty calories.",
         svg=hand("30 g", 500, 380, 180) + hand("≈ 180 kcal", 500, 640, 170, "hand red", -4)),
    dict(text="So my advent calendar just got very, very small.",
         svg=calendar(500, 520, 45) + person(820, 760, 0.6, "o", "down")),
    dict(text="One handful a day, for twenty four days. Totally fine.",
         svg=person(500, 520, 1.0, "smile", "up") + hand("fine :)", 760, 900, 120, rot=-6)),
    dict(text="Unless I also eat tomorrow's box.",
         svg=calendar(500, 260, 75, open_=(16, 17)) + person(500, 760, 0.9, "sly", "front") + hand("oops", 820, 640, 110, "hand red", 10)),
]
