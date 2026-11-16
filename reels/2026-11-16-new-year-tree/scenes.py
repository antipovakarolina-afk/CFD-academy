"""What did I google today? — Why do we put up a tree for New Year?

Факты:
- Вечнозелёные ветки зимой — древний символ жизни (римляне на Сатурналии, кельты, египтяне и др.).
- Украшенная ёлка — Германия, XVI век. Таллин (1441) и Рига (1510) обе считают, что ёлка была у них первой.
- 1848: Illustrated London News — королева Виктория и принц Альберт у ёлки → мода в Британии и США.
- СССР: в конце 1920-х ёлку как религиозную традицию запретили; в декабре 1935 вернули как новогоднюю,
  звезда стала красной. Поэтому в бывших республиках ёлку ставят на Новый год.
- Мишура: Нюрнберг, начало XVII века, из настоящего серебра.
- Электрические гирлянды: 1882, Эдвард Джонсон (компаньон Эдисона).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.08
P = PASTEL

SCENES = [
    dict(bg=P["blue"], text="What did I google today?",
         svg=blob(330, 600, 300, "#cfe0ff") + me(330, 640, 0.9, "phone", "o")
             + hand("what did I", 720, 330, 85) + google_word(720, 470, 150) + hand("today?", 720, 580, 85)
             + snow(10, 1, "#9cc0ff")),
    dict(bg=P["mint"], text="Why do we put up a tree for New Year? Like, a real tree. Inside our homes.",
         svg=blob(560, 560, 320, "#c6efd8", 1) + xtree(600, 560, 1.0) + me(220, 640, 0.85, "think", "worry")
             + hand("why?!", 780, 220, 120, "hand red", 8)),
    dict(bg=P["night"], text="Long before Christmas, people brought evergreen branches inside in the middle of winter. A little promise that spring would come back.",
         svg=snow(30, 2) + branch(260, 420, 1.4, -10) + branch(330, 620, 1.2, 12)
             + sun(800, 260, 70) + hand("spring is coming", 500, 880, 100, "hand orange", -3)),
    dict(bg=P["yellow"], text="Decorated trees started in Germany, around the fifteen hundreds.",
         svg=blob(500, 560, 320, "#ffe7a3", 2) + xtree(500, 660, 1.0) + hand("Germany", 500, 170, 130, "hand", -3)
             + hand("1500s", 820, 940, 110, "hand red", 6)),
    dict(bg=P["peach"], text="And Tallinn and Riga still argue about who had the very first one!",
         svg=xtree(280, 600, 0.8, face="angry") + xtree(720, 600, 0.8, face="angry")
             + hand("Tallinn 1441", 280, 940, 85, "hand blue") + hand("Riga 1510", 720, 940, 85, "hand red")
             + hand("me first!", 500, 230, 110, "hand purple", -5)),
    dict(bg=P["lilac"], text="Then in eighteen forty eight, a newspaper printed Queen Victoria next to a Christmas tree. And suddenly everyone wanted one.",
         svg=crown(500, 150, 1.1) + xtree(500, 660, 0.95, lights=False) + hand("1848", 830, 420, 120, "hand purple", 8)
             + hand("trendy!", 190, 880, 110, "hand pink", -6)),
    dict(bg=P["night"], text="But why New Year, and not Christmas? In the Soviet Union, Christmas was banned. And so was the tree.",
         svg=snow(24, 5) + xtree(500, 600, 0.95, balls=False) + check(500, 560, 4.5, ok=False)
             + hand("banned", 500, 930, 120, "hand red", -4)),
    dict(bg=P["pink"], text="Then in nineteen thirty five, the tree came back. But as a New Year tree, with a red star on top.",
         svg=xtree(400, 620, 1.0, red_star=True) + clock12(800, 330, 0.9) + hand("1935", 810, 560, 130, "hand red", -6)
             + hand("New Year tree", 500, 960, 100, "hand green", 3)),
    dict(bg=P["blue"], text="That's why so many of us still put it up for New Year. Bonus fact: tinsel used to be made of real silver.",
         svg=tinsel(500, 360, 2.0) + hand("real silver!", 500, 820, 130, "hand blue", -4) + star(170, 230, 1.2) + star(840, 700, 1.0, "#ff8fb1")),
    dict(bg=P["night"], text="And the first electric tree lights? Eighteen eighty two.",
         svg=xtree(400, 600, 0.95, balls=False, lights=True) + bulb(800, 330, 1.0) + hand("1882", 800, 560, 130, "hand orange", 6)),
    dict(bg=P["peach"], text="And me? Honestly, I'm just here for the lights. And the mandarins.",
         svg=xtree(700, 560, 0.85, lights=True) + me(280, 640, 0.8, "wave", "big")
             + mandarin(560, 880, 0.9) + mandarin(680, 905, 0.8) + mandarin(800, 880, 0.9)
             + hand("happy New Year!", 500, 210, 105, "hand red", -3)),
]
