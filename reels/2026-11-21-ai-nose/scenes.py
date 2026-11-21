"""Рисованный стиль, для монетизации (>60 c). What did I google today? — Can AI smell? (Osmo)

Факты (сверено 21.11.2026):
- MIT Technology Review, 18.11.2026: Osmo заявляет «human-level olfactory intelligence» — по их определению модель
  примерно как средний человек замечает и различает запахи. Заявление компании, по её собственным тестам; журнал — скептичен.
- Osmo выросла из Google Research, запуск январь 2023, $60 млн (Lux Capital, Google Ventures).
- Science, 2023 («A Principal Odor Map…», с Monell Center): по структуре молекулы предсказывает описание запаха;
  на 400 новых молекулах точнее совпадало со средним мнением панели, чем типичный эксперт панели.
- Данные: >10 млн оценок людьми (по словам компании).
- Применение: парфюмерия; со StockX — поиск поддельных кроссовок по «химическому запаху» материалов.
- Критика: независимой проверки нет; учёный Avery Gilbert называет часть заявлений недоказанными;
  человеческое обоняние зависит от контекста и памяти.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 0.98
MOTION_FPS = 12
P = PASTEL

def sniff(x, y, d=0.0):
    return mv(g(x, y, 1, '<path class="ln" style="stroke:#9aa1ab;stroke-width:6" d="M0 0 q20 -30 0 -60 q-20 -30 0 -60"/>'), "rise", a=110, p=1.3, d=d)

SCENES = [
    dict(bg=P["mint"], text="What did I google today? Can AI actually smell? A startup says its AI nose is now as good as yours.",
         svg=intro_search("can ai smell?", "#c6efd8")),
    dict(bg=P["blue"], text="The company is called Osmo. It started inside Google Research, and in 2023 it raised sixty million dollars.",
         svg=mv(nose(330, 560, 1.4, robot=True), "wiggle", a=5, p=0.6) + mv(moneybag(760, 560, 1.1, "$"), "bob", a=18, p=0.7)
             + mv(hand("Osmo", 500, 230, 170, "hand purple", -4), "pulse", a=0.06, p=0.8) + hand("$60M · 2023", 500, 920, 110, "hand green", 3)),
    dict(bg=P["yellow"], text="Here's how it works. The AI looks at a molecule, just its shape, and predicts how it smells. Flowery? Woody? Fruity?",
         svg=mv(molecule(500, 380, 1.3), "spin", p=6) + mv(hand("flowery?", 200, 820, 90, "hand pink", -4), "appear", d=2.2)
             + mv(hand("woody?", 500, 880, 90, "hand orange", 3), "appear", d=3.4) + mv(hand("fruity?", 800, 820, 90, "hand red", -3), "appear", d=4.6)),
    dict(bg=P["pink"], text="In 2023, in the journal Science, its predictions matched expert sniffers better than a typical expert did.",
         svg=mv(paper(330, 520, 1.1), "bob", a=12, p=0.9) + nose(760, 520, 1.1) + mv(check(760, 250, 1.6), "appear", d=1.8)
             + hand("2023", 330, 230, 110, "hand red", -6) + hand("better than experts", 500, 950, 90, "hand purple", 2)),
    dict(bg=P["peach"], text="It learned from more than ten million human smell ratings.",
         svg="".join(mv(nose(160 + (k % 4) * 230, 330 + (k // 4) * 260, 0.45), "appear", d=round(0.3 + k * 0.25, 2)) for k in range(8))
             + mv(hand("10,000,000+", 500, 900, 140, "hand red", -3), "pulse", a=0.06, p=0.6)),
    dict(bg=P["lilac"], text="And now the company says its model is about as good as an average person at telling smells apart.",
         svg=mv(nose(260, 560, 1.0, robot=True), "bob", a=16, p=0.7) + hand("=", 500, 600, 220, "hand purple") + mv(nose(740, 560, 1.0), "bob", a=16, p=0.8)
             + sniff(230, 380) + sniff(290, 380, 0.6) + sniff(710, 380, 0.3) + sniff(770, 380, 0.9) + hand("human-level?", 500, 220, 120, "hand blue", -4)),
    dict(bg=P["blue"], text="It's already used to create perfumes, and even to sniff out fake sneakers.",
         svg=mv(perfume(270, 540, 1.3), "wiggle", a=6, p=0.7) + mv(sneaker(700, 600, 0.9), "bob", a=14, p=0.6)
             + mv(hand("FAKE?", 700, 380, 120, "hand red", 8), "pulse", a=0.12, p=0.4) + hand("perfume", 270, 860, 90, "hand pink", -3)),
    dict(bg=P["yellow"], text="But scientists are skeptical. That claim comes from the company's own tests. Nobody independent has checked it yet.",
         svg=mv(magnifier(420, 520, 1.6), "move", x=180, y=-60) + mv(qmarks(700, 280), "wiggle", a=10, p=0.5)
             + hand("own tests", 500, 860, 120, "hand red", -3) + mv(check(800, 860, 1.0, ok=False), "wiggle", a=10, p=0.5)),
    dict(bg=P["pink"], text="And human smell isn't just chemistry. It's memory, mood, and moments.",
         svg=mv(brain(500, 460, 1.1), "pulse", a=0.07, p=0.8) + mv(heart(220, 300, 0.6), "bob", a=14, p=0.6) + mv(cookie(800, 330, 2.6), "bob", a=12, p=0.7)
             + mv(hand("memory", 200, 830, 90, "hand purple", -4), "appear", d=1.4) + mv(hand("mood", 500, 900, 90, "hand pink", 3), "appear", d=2.0)
             + mv(hand("moments", 800, 830, 90, "hand orange", -3), "appear", d=2.6)),
    dict(bg=P["mint"], text="So, can AI smell like you? Almost. But it still can't remember your grandma's kitchen.",
         svg=mv(nose(330, 520, 1.1, robot=True), "wiggle", a=6, p=0.5) + mv(qmarks(470, 250), "wiggle", a=10, p=0.6)
             + "".join(mv(cookie(640 + k * 120, 640 - (k % 2) * 70, 2.2), "bob", a=10, p=0.6 + k * 0.1) for k in range(3))
             + mv(hand("almost.", 500, 920, 140, "hand green", -4), "appear", d=1.5)),
]
