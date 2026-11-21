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


ROBO = lambda x, y, s=1.0, face="smile": nose(x, y, s, robot=True, face=face)
NOSES = "".join(mv(nose(130 + (k % 5) * 185, 230 + (k // 5) * 190, 0.33, face="smile" if k % 3 else "happy"), "appear", d=round(0.2 + k * 0.12, 2)) for k in range(20))
ORBIT = "".join(mv(f'<circle class="ln" cx="{500 + 230 * __import__("math").cos(k * 1.257):.0f}" cy="{380 + 230 * __import__("math").sin(k * 1.257):.0f}" r="20" style="fill:{c}"/>', "orbit", x=500, y=380, p=3 + k * 0.4)
                for k, c in enumerate(["#ff8fc7", "#7ed957", "#4fa3f7", "#ffd23f", "#b79bff"]))

SCENES = [
    dict(bg=P["mint"], text="What did I google today? Can AI actually smell? A startup says its AI nose is now as good as yours.",
         svg=intro_search("can ai smell?", "#c6efd8") + mv(ROBO(860, 860, 0.5, "o"), "bounce", a=40, p=0.7)),
    dict(bg=P["blue"], text="The company is called Osmo. It started inside Google Research, and in 2023 it raised sixty million dollars.",
         svg=coin_rain(16, 1) + mv(ROBO(340, 580, 1.3, "happy"), "bounce", a=36, p=0.8) + mv(moneybag(770, 640, 1.1, "$"), "bounce", a=26, p=0.6)
             + mv(hand("Osmo", 500, 200, 180, "hand purple", -4), "stamp", d=0.4) + mv(hand("$60M · 2023", 500, 930, 110, "hand green", 3), "appear", d=1.4)),
    dict(bg=P["yellow"], text="Here's how it works. The AI looks at a molecule, just its shape, and predicts how it smells. Flowery? Woody? Fruity?",
         svg=ORBIT + mv(molecule(500, 380, 1.1), "spin", p=4) + mv(ROBO(150, 300, 0.45, "o"), "wiggle", a=10, p=0.4)
             + mv(flower(200, 700, 0.6), "flyin", x=-300, y=200, a=-30, d=2.0) + mv(hand("flowery?", 200, 900, 85, "hand pink", -4), "appear", d=2.3)
             + mv(xtree(500, 760, 0.45), "flyin", x=0, y=400, a=10, d=3.2) + mv(hand("woody?", 500, 940, 85, "hand green", 3), "appear", d=3.5)
             + mv(apple(800, 700, 1.4), "flyin", x=300, y=200, a=40, d=4.4) + mv(hand("fruity?", 800, 900, 85, "hand red", -3), "appear", d=4.7)),
    dict(bg=P["pink"], text="In 2023, in the journal Science, its predictions matched expert sniffers better than a typical expert did.",
         svg=mv(paper(320, 520, 1.1), "flyin", x=-700, y=-200, a=-40, d=0.2) + mv(nose(760, 540, 1.0, face="o"), "bounce", a=24, p=0.7)
             + sniff(740, 300, 0.5) + mv(check(760, 230, 1.6), "stamp", d=2.2) + star(160, 180, 1.0) + mv(star(900, 760, 0.8, "#ff8fb1"), "spin", p=2)
             + mv(hand("2023", 320, 200, 110, "hand red", -6), "appear", d=0.8) + mv(hand("better than experts", 500, 950, 90, "hand purple", 2), "appear", d=2.8)),
    dict(bg=P["peach"], text="It learned from more than ten million human smell ratings.",
         svg=NOSES + mv(hand("10,000,000+", 500, 950, 140, "hand red", -3), "stamp", d=2.6)),
    dict(bg=P["lilac"], text="And now the company says its model is about as good as an average person at telling smells apart.",
         svg=mv(ROBO(260, 600, 1.0, "smile"), "bounce", a=30, p=0.6) + mv(hand("=", 500, 620, 220, "hand purple"), "pulse", a=0.15, p=0.4)
             + mv(nose(740, 600, 1.0, face="smile"), "bounce", a=30, p=0.6, d=0.6)
             + sniff(230, 380) + sniff(290, 380, 0.6) + sniff(710, 380, 0.3) + sniff(770, 380, 0.9) + mv(hand("human-level?", 500, 200, 120, "hand blue", -4), "stamp", d=0.5)),
    dict(bg=P["blue"], text="It's already used to create perfumes, and even to sniff out fake sneakers.",
         svg=mv(perfume(230, 460, 1.1), "wiggle", a=8, p=0.5) + mist(300, 330, 10, 300) + mv(sneaker(680, 760, 0.85), "bounce", a=14, p=0.7)
             + mv('<rect x="420" y="640" width="14" height="230" style="fill:#7ed957;opacity:.7"/>', "travel", x=500, p=1.2)
             + mv(mv(hand("FAKE!", 700, 560, 140, "hand red", -10), "stamp", d=2.6), "shake", a=6, p=0.3, d=3.0) + hand("perfume", 230, 760, 90, "hand pink", -3)),
    dict(bg=P["yellow"], text="But scientists are skeptical. That claim comes from the company's own tests. Nobody independent has checked it yet.",
         svg=mv(magnifier(380, 520, 1.4), "orbit", x=500, y=520, p=2.4) + mv(qmarks(700, 240), "shake", a=6, p=0.4)
             + mv(ROBO(500, 520, 0.6, "o"), "shake", a=4, p=0.3) + mv(hand("own tests", 500, 880, 120, "hand red", -3), "stamp", d=2.4)),
    dict(bg=P["pink"], text="And human smell isn't just chemistry. It's memory, mood, and moments.",
         svg=mv(brain(500, 620, 1.0), "pulse", a=0.08, p=0.6)
             + mv(heart(250, 520, 0.6), "rise", a=420, x=-40, p=2.2) + mv(cookie(750, 520, 2.4), "rise", a=420, x=40, p=2.2, d=0.7)
             + mv(flower(500, 480, 0.5), "rise", a=420, x=0, p=2.2, d=1.4)
             + mv(hand("memory", 200, 900, 90, "hand purple", -4), "appear", d=1.4) + mv(hand("mood", 500, 950, 90, "hand pink", 3), "appear", d=2.0)
             + mv(hand("moments", 800, 900, 90, "hand orange", -3), "appear", d=2.6)),
    dict(bg=P["mint"], text="So, can AI smell like you? Almost. But it still can't remember your grandma's kitchen.",
         svg=mv(ROBO(300, 640, 1.0, "sad"), "wiggle", a=5, p=0.8)
             + thought(650, 300, 0.95, "".join(mv(cookie(560 + k * 90, 300, 2.0), "orbit", x=650, y=300, p=3) for k in range(3)))
             + mv(hand("almost.", 500, 950, 150, "hand green", -4), "stamp", d=2.0)),
]
