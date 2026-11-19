"""Рисованный стиль, для монетизации (>60 c), без вопроса зрителям.
What did I google today? — Why things feel hard: familiar vs unfamiliar, practice, sleep, myelin.

Факты:
- Эффект распределённой практики (spacing effect): короткие регулярные занятия эффективнее редких длинных
  при том же общем времени (многочисленные исследования памяти и моторных навыков).
- Сон закрепляет выученное (sleep-dependent consolidation; напр. Walker et al., 2002 — моторные навыки).
- Миелин — жировая оболочка аксонов (её образуют олигодендроциты); чем она толще, тем быстрее идёт сигнал.
  Активность и практика влияют на миелинизацию (activity-dependent myelination).
- «Медленные точные повторения лучше всего растят миелин» — популярная идея (напр. «The Talent Code»),
  строго не доказана → в тексте «many experts believe».
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.05
P = PASTEL

MOTION_FPS = 12

SEG = "".join(mv(f'<rect class="ln" x="{290 + k * 75}" y="494" width="62" height="52" rx="24" style="fill:#ffd23f;stroke-width:5"/>',
                 "appear", d=round(0.9 + k * 0.45, 2)) for k in range(6))
CHECKS = "".join(mv(check(200 + k * 100, 470, 0.7), "appear", d=round(0.7 + k * 0.4, 2)) for k in range(7))

SCENES = [
    dict(bg=P["lilac"], text="What did I google today? Why do some things feel so hard? Turns out, your brain doesn't even know what hard means.",
         svg=intro_search("why do things feel hard?", "#ddd0ff")),
    dict(bg=P["pink"], text="For your brain, there's no easy or difficult. There's only familiar, and unfamiliar.",
         svg=mv(brain(500, 470, 1.4), "pulse", a=0.07, p=0.8)
             + hand("easy", 220, 210, 100, "hand", -6) + mv(check(380, 190, 1.0, ok=False), "wiggle", a=12, p=0.5)
             + hand("hard", 690, 210, 100, "hand", 6) + mv(check(870, 190, 1.0, ok=False), "wiggle", a=12, p=0.45)
             + mv(hand("familiar", 260, 860, 100, "hand green", -4), "bob", a=14, p=0.9) + mv(hand("new", 760, 860, 110, "hand purple", 4), "bob", a=14, p=0.7)),
    dict(bg=P["mint"], text="Something you've done a hundred times feels easy. Something you're doing for the first time feels hard. That's really it.",
         svg=dirt_path(500, 400, 1.0) + mv(person(150, 360, 0.32, "smile", "down"), "move", x=680, y=-20)
             + hand("done 100 times", 500, 210, 95, "hand green", -3)
             + hand("first time", 500, 700, 95, "hand purple", 3) + mv(qmarks(640, 870), "wiggle", a=10, p=0.6)),
    dict(bg=P["yellow"], text="Fact one. Your brain rewires itself all the time. It's called neuroplasticity. And it loves consistency, not marathons.",
         svg=hand("#1", 150, 200, 150, "hand orange") + neuron(500, 480, 1.0)
             + mv(signal(270, 470, 1.0), "travel", p=1.1, x=470) + mv(signal(270, 470, 1.0), "travel", p=1.1, d=1.75, x=470)
             + hand("neuroplasticity", 500, 770, 110, "hand purple", -3) + mv(hand("consistency > marathons", 500, 930, 80, "hand red", 2), "pulse", a=0.06, p=0.7)),
    dict(bg=P["blue"], text="Studies show that short practice every day beats one long session once a week. Even with the same total time.",
         svg=mv(bar_pair(500, 620, 1.1, "10 min × 7 days", "70 min × 1", 0.6, 1.5), "grow", d=0.3)
             + mv(check(260, 260, 1.4), "appear", d=1.6) + mv(check(720, 210, 1.2, ok=False), "appear", d=2.3)
             + hand("same time, better result", 500, 950, 80, "hand blue", -2)),
    dict(bg=P["night"], text="Fact two. While you sleep, your brain locks in what you practiced. So showing up every day matters more than one big effort.",
         svg=hand("#2", 150, 200, 150, "hand orange") + mv(moon(780, 250, 90), "bob", a=16, p=1.4) + snow(14, 6, "#9fb3ff") + bed(500, 640, 1.0)
             + mv(zzz(620, 520, 0.8, "hand"), "rise", a=120, x=40, p=1.8) + mv(zzz(620, 520, 0.8, "hand"), "rise", a=120, x=40, p=1.8, d=1.9)
             + mv(hand("sleep = save", 500, 920, 120, "hand orange", -3), "pulse", a=0.06, p=0.8)),
    dict(bg=P["peach"], text="Fact three. When you repeat something again and again, the wires between your neurons get wrapped in a thin fatty layer called myelin.",
         svg=hand("#3", 150, 200, 150, "hand red") + neuron(500, 520, 1.0) + SEG
             + mv(signal(270, 510, 0.9), "travel", p=0.8, x=480) + hand("myelin", 470, 360, 120, "hand orange", -4)
             + mv(hand("repeat, repeat, repeat", 500, 830, 90, "hand purple", 2), "bob", a=12, p=0.6)),
    dict(bg=P["mint"], text="The thicker the myelin, the faster the signals travel. Like turning a dirt road into a highway.",
         svg=dirt_path(500, 300, 0.8) + mv('<path class="ln" style="stroke-width:9" d="M500 450 v90 M470 510 l30 35 l30 -35"/>', "bob", a=14, p=0.5)
             + highway(500, 700, 0.85) + mv(car(180, 690, 0.45), "move", x=640) + mv(hand("faster signals", 500, 950, 100, "hand green", -3), "pulse", a=0.05, p=0.6)),
    dict(bg=P["lilac"], text="And many experts believe that slow, precise practice builds skills best. Slow is smooth. And smooth becomes fast.",
         svg=mv(snail(330, 560, 1.4), "move", x=260) + mv(hand("slow", 180, 250, 105, "hand purple", -5), "appear", d=0.5)
             + mv(hand("→ smooth", 480, 250, 100, "hand blue", -3), "appear", d=2.0) + mv(hand("→ fast", 820, 250, 100, "hand green", 3), "appear", d=3.6)
             + hand("precise > rushed", 500, 920, 90, "hand red", -2)),
    dict(bg=P["yellow"], text="So here's the secret. A little every day, slowly and carefully. Your brain will do the rest.",
         svg=calendar(500, 470, 100, cols=7, rows=1) + CHECKS + mv(brain(500, 730, 0.7), "pulse", a=0.1, p=0.7)
             + hand("a little every day", 500, 250, 110, "hand orange", -3) + hand("your brain does the rest", 500, 960, 85, "hand purple", 2)),
]
