"""Рисованный стиль, для монетизации (>60 c), без вопроса зрителям. История Spire of Dublin.

Факты:
- Nelson's Pillar: гранитная колонна со статуей адмирала Нельсона на O'Connell Street; закладка 1808, открыта 1809.
- 8 марта 1966 — взрыв (республиканцы), уничтожена верхняя половина со статуей; через несколько дней армия
  взорвала остаток («обрубок»), и этот второй взрыв выбил окна вокруг.
- Позже — конкурс на новый памятник; победил проект Ian Ritchie Architects «Monument of Light».
- Spire установлен в 2002–2003 (завершён в январе 2003): нержавеющая сталь, ~120 м; ~3 м в диаметре у основания,
  ~15 см наверху; верхушка подсвечивается ночью.
- Для сравнения: башня Биг-Бена (Elizabeth Tower) ~96 м.
- Народные прозвища: the Spike, the Stiletto in the Ghetto (и др.).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.0
MOTION_FPS = 12
P = PASTEL

SCENES = [
    dict(bg=P["blue"], text="What did I google today? Why is there a giant needle in the middle of Dublin?",
         svg=intro_search("why is there a spire in dublin?", "#cfe0ff")),
    dict(bg=P["yellow"], text="Before the needle, this spot had a huge stone column with a statue of the British admiral Nelson on top. It went up in 1809.",
         svg=street(940, 2) + mv(pillar(500, 870, 1.25), "flyin", x=0, y=700, a=0, d=0.2) + mv(hand("1809", 820, 230, 140, "hand purple", 6), "stamp", d=1.6)
             + mv(hand("Nelson's Pillar", 500, 120, 110, "hand orange", -3), "appear", d=0.8)),
    dict(bg=P["night"], text="Then, one night in 1966, a bomb went off. The top half of the pillar, and Nelson, came crashing down.",
         svg=snow(20, 4, "#9fb3ff") + street(940, 2) + pillar(500, 870, 1.25, broken=True)
             + mv(boom(500, 300, 1.4), "pulse", a=0.15, p=0.3) + mv(g(560, 200, 0.9, '<circle class="ln" cx="0" cy="0" r="30" style="fill:#8d929b"/>'), "fall", a=300, x=180, y=700, p=1.4, d=0.4)
             + mv(hand("1966", 190, 560, 150, "hand orange", -6), "stamp", d=1.2)),
    dict(bg=P["peach"], text="A few days later, the army blew up what was left. That second blast broke more windows than the first one!",
         svg=street(940, 5) + mv(boom(500, 700, 1.1), "shake", a=10, p=0.2)
             + "".join(mv(g(200 + k * 150, 600, 0.5, '<path class="ln" style="fill:#cfe8ff" d="M0 0 l40 -20 l20 40 l-50 10z"/>'), "fall", a=200, x=(k - 3) * 40, y=400, p=1.0, d=round(0.3 + k * 0.15, 2)) for k in range(6))
             + mv(hand("oops", 500, 220, 160, "hand red", 6), "stamp", d=1.8)),
    dict(bg=P["mint"], text="For years, the spot stayed empty. Then the city held a competition to design something new.",
         svg=street(940, 7) + mv(qmarks(470, 600), "wiggle", a=10, p=0.6) + mv(paper(780, 380, 0.7, "ideas"), "flyin", x=400, y=-200, a=30, d=1.2)
             + mv(bulb(230, 380, 0.8), "pulse", a=0.12, p=0.5) + hand("empty...", 500, 200, 130, "hand purple", -3)),
    dict(bg=P["blue"], text="The winner was the Monument of Light, by architect Ian Ritchie. It was finished in 2003.",
         svg=street(960, 9) + mv(spire(500, 930, 1.0, 680), "grow", d=0.3) + mv(hand("Monument of Light", 500, 120, 100, "hand purple", -3), "appear", d=1.6)
             + mv(hand("2003", 800, 420, 140, "hand red", 6), "stamp", d=2.4)),
    dict(bg=P["lilac"], text="It's a hundred and twenty meters of stainless steel. Taller than Big Ben's tower. Three meters wide at the bottom, and just fifteen centimeters at the top.",
         svg=mv(spire(330, 960, 1.0, 900), "bob", a=6, p=1.2) + mv(bigben(720, 960, 1.0, 720), "appear", d=1.5)
             + mv(hand("120 m", 160, 420, 110, "hand red", -6), "stamp", d=0.6) + mv(hand("96 m", 880, 300, 100, "hand", 4), "appear", d=2.0)
             + mv(hand("3 m → 15 cm", 500, 1060, 90, "hand purple", -2), "appear", d=4.5)),
    dict(bg=P["night"], text="And at night, the very top lights up, like a candle over the city.",
         svg=snow(24, 8, "#9fb3ff") + street(960, 11) + mv(spire(500, 930, 1.0, 860, lit=True), "bob", a=4, p=1.5)
             + mv('<circle cx="500" cy="70" r="70" style="fill:#fff6c8;opacity:.35"/>', "pulse", a=0.4, p=0.8)
             + mv(hand("glow", 760, 300, 120, "hand orange", 6), "appear", d=1.2)),
    dict(bg=P["pink"], text="Of course, Dubliners gave it nicknames right away. The Spike. And the Stiletto in the Ghetto.",
         svg=mv(spire(250, 960, 1.0, 860), "wiggle", a=2, p=0.8) + mv(stiletto(640, 520, 1.3), "bounce", a=26, p=0.7)
             + mv(hand("the Spike", 640, 230, 110, "hand purple", -5), "stamp", d=1.6) + mv(hand("the Stiletto", 640, 760, 100, "hand red", 3), "appear", d=3.2)
             + mv(hand("in the Ghetto", 640, 870, 100, "hand red", 3), "appear", d=3.8)),
    dict(bg=P["blue"], text="So, from a fallen admiral, to a needle of light. That's Dublin.",
         svg=liffey(880) + street(880, 13) + mv(spire(500, 860, 1.0, 600, lit=True), "bob", a=5, p=1.4)
             + mv(pillar(180, 860, 0.45, broken=True), "appear", d=0.3) + mv(heart(820, 260, 0.6), "pulse", a=0.15, p=0.6)
             + mv(hand("that's Dublin", 500, 120, 120, "hand green", -3), "stamp", d=2.2)),
]
