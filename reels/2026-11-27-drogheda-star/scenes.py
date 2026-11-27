"""Рисованный стиль, для монетизации (>60 c), без вопроса зрителям. Уважительный тон о Голоде.
Why does Drogheda's coat of arms have a star and crescent?

Факты (сверено 27.11.2026):
- Великий голод (1845–1852): фитофтороз картофеля (Phytophthora infestans); ~1 млн умерших; 1–2 млн эмигрировали;
  население сократилось на 20–25%. Провалы политики помощи усугубили катастрофу.
- Султан Абдул-Меджид I прислал £1000 (31 марта 1847, Дублинский замок) — задокументировано.
- Легенда: хотел дать £10 000, попросили не больше королевы (£2000); тайно послал 3 корабля с едой в Дроэду;
  в благодарность город добавил звезду и полумесяц. Легенда распространилась примерно с 1930-х (Aramco World).
- Против: звезда и полумесяц на гербе Дроэды старше Голода — связывают со средневековыми хартиями (как у Портсмута);
  Drogheda Historical Society: записей о заходе османских кораблей нет; газеты мая 1847 пишут лишь о «foreign ships».
- Choctaw Nation, март 1847: сбор для голодающих ирландцев (обычно называют $170), вскоре после «Тропы слёз»;
  скульптура Kindred Spirits (Мидлтон, графство Корк, 2015).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.08
MOTION_FPS = 12
P = PASTEL
GREEN = "#d9f2e3"

SCENES = [
    dict(bg=P["blue"], text="What did I google today? Why does Drogheda, in Ireland, have a star and a crescent, just like the Turkish flag?",
         svg=intro_search("why drogheda star and crescent?", "#cfe0ff") + mv(crescent_star(860, 880, 0.6, "#e63946"), "spin", p=6)),
    dict(bg=GREEN, text="To understand the story, we go back to 1845. A disease called potato blight hit Ireland, and the potatoes rotted in the ground.",
         svg="".join(mv(potato(220 + k * 280, 500, 1.0), "appear", d=round(0.3 + k * 0.3, 1)) for k in range(3))
             + "".join(mv(potato(220 + k * 280, 780, 1.0, rotten=True), "appear", d=round(2.2 + k * 0.4, 1)) for k in range(3))
             + mv(hand("1845", 500, 230, 150, "hand", -4), "stamp", d=0.5) + mv(hand("blight", 500, 990, 110, "hand red", 3), "appear", d=3.5)),
    dict(bg=P["lilac"], text="For millions of poor families, potatoes were almost the only food. It became the Great Famine.",
         svg=mv(potato(500, 520, 2.0, rotten=True), "wiggle", a=3, p=1.2) + mv(hand("the Great Famine", 500, 230, 120, "hand purple", -3), "appear", d=1.0)
             + mv(hand("1845 – 1852", 500, 900, 100, "hand", 2), "appear", d=2.2)),
    dict(bg=P["peach"], text="Around one million people died. One to two million more left Ireland on ships. The population fell by about a quarter.",
         svg=sea(760) + mv(ship(260, 760, 0.6), "move", x=600) + mv(hand("~1,000,000", 500, 260, 130, "hand", -3), "appear", d=0.6)
             + mv(hand("lives lost", 500, 380, 80, "hand purple", 2), "appear", d=1.2) + mv(hand("1–2 million emigrated", 500, 1080, 90, "hand blue", -2), "appear", d=3.0)),
    dict(bg=P["yellow"], text="In 1847, the Ottoman Sultan, Abdulmejid, sent a thousand pounds to help. That part is real, and it's recorded.",
         svg=mv(crescent_star(500, 330, 1.6, "#e63946"), "pulse", a=0.06, p=0.8) + mv(moneybag(500, 720, 1.2, "£"), "flyin", x=0, y=-600, a=20, d=0.8)
             + mv(hand("£1,000", 820, 760, 120, "hand green", 6), "stamp", d=1.8) + mv(check(200, 760, 1.4), "stamp", d=3.2) + hand("1847", 180, 220, 110, "hand red", -6)),
    dict(bg=P["pink"], text="But the legend says more. He wanted to give ten thousand. He was asked not to give more than Queen Victoria. So he secretly sent three ships of food to Drogheda.",
         svg=crown(220, 250, 1.0) + mv(hand("£2,000", 220, 400, 90, "hand", -4), "appear", d=1.2) + mv(hand("£10,000?", 720, 280, 105, "hand red", 6), "shake", a=4, p=0.4, d=2.0)
             + sea(760) + "".join(mv(ship(100 + k * 70, 760, 0.42), "move", x=520, d=round(2.8 + k * 0.5, 1)) for k in range(3))
             + mv(hand("the legend", 500, 1060, 100, "hand purple", -2), "appear", d=3.0)),
    dict(bg=P["blue"], text="And to say thank you, Drogheda put the star and crescent on its coat of arms. Beautiful story, right?",
         svg=mv(shield(500, 520, 1.3, ""), "flyin", x=0, y=500, a=0, d=0.2) + mv(crescent_star(480, 470, 1.4, "#fff"), "appear", d=1.4)
             + mv(heart(820, 250, 0.6), "pulse", a=0.15, p=0.5) + mv(hand("thank you?", 500, 1020, 110, "hand purple", -3), "appear", d=2.4)),
    dict(bg=P["yellow"], text="Here's the twist. The star and crescent were on Drogheda's arms centuries before the famine. They likely come from the town's medieval charters.",
         svg=mv(paper(330, 500, 1.1, "1200s"), "bob", a=10, p=0.9) + shield(760, 520, 0.7, "") + crescent_star(745, 495, 0.75, "#fff")
             + mv(hand("plot twist!", 500, 200, 130, "hand red", -5), "stamp", d=0.4) + mv(hand("much older", 500, 1000, 110, "hand purple", 3), "appear", d=2.6)),
    dict(bg=P["peach"], text="And the ships? Local papers mention foreign ships in May 1847, but no record proves they were Turkish. Historians still debate it.",
         svg=mv(newspaper(330, 520, 0.8, "1847"), "wiggle", a=3, p=0.8) + sea(820) + mv(ship(760, 820, 0.5), "bob", a=12, p=1.0)
             + mv(qmarks(700, 360), "shake", a=6, p=0.4) + mv(hand("unproven", 500, 200, 120, "hand red", -3), "stamp", d=2.6)),
    dict(bg=GREEN, text="Bonus fact. In 1847, the Choctaw Nation in America, who had just survived their own forced removal, also collected money for the starving Irish.",
         svg=mv(kindred_feathers(500, 820, 1.0), "grow", d=0.3) + mv(heart(500, 250, 0.6), "pulse", a=0.15, p=0.6)
             + mv(hand("Choctaw Nation", 500, 140, 110, "hand green", -3), "appear", d=0.8) + mv(hand("Kindred Spirits, Cork", 500, 1020, 80, "hand purple", 2), "appear", d=3.5)),
    dict(bg=P["blue"], text="So, the star on Drogheda's arms is older than the story. But the kindness from far away? That part was real.",
         svg=shield(500, 460, 1.1, "") + mv(crescent_star(485, 420, 1.2, "#fff"), "pulse", a=0.06, p=0.8) + mv(heart(200, 300, 0.5), "bob", a=14, p=0.7)
             + mv(heart(820, 320, 0.5, "#e63946"), "bob", a=14, p=0.8) + mv(hand("kindness was real", 500, 980, 110, "hand green", -3), "stamp", d=2.4)),
]
