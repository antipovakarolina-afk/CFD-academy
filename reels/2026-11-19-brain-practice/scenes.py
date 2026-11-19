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

SCENES = [
    dict(bg=P["lilac"], text="What did I google today? Why do some things feel so hard? Turns out, your brain doesn't even know what hard means.",
         svg=intro_search("why do things feel hard?", "#ddd0ff")),
    dict(bg=P["pink"], text="For your brain, there's no easy or difficult. There's only familiar, and unfamiliar.",
         svg=brain(500, 470, 1.4) + hand("easy", 220, 210, 100, "hand", -6) + check(380, 190, 1.0, ok=False)
             + hand("hard", 690, 210, 100, "hand", 6) + check(870, 190, 1.0, ok=False)
             + hand("familiar", 260, 860, 100, "hand green", -4) + hand("new", 760, 860, 110, "hand purple", 4)),
    dict(bg=P["mint"], text="Something you've done a hundred times feels easy. Something you're doing for the first time feels hard. That's really it.",
         svg=dirt_path(500, 400, 1.0) + hand("done 100 times", 500, 210, 95, "hand green", -3)
             + hand("first time", 500, 700, 95, "hand purple", 3) + qmarks(640, 870)),
    dict(bg=P["yellow"], text="Fact one. Your brain rewires itself all the time. It's called neuroplasticity. And it loves consistency, not marathons.",
         svg=hand("#1", 150, 200, 150, "hand orange") + neuron(500, 480, 1.0) + signal(650, 420, 1.0)
             + hand("neuroplasticity", 500, 770, 110, "hand purple", -3) + hand("consistency > marathons", 500, 930, 80, "hand red", 2)),
    dict(bg=P["blue"], text="Studies show that short practice every day beats one long session once a week. Even with the same total time.",
         svg=bar_pair(500, 620, 1.1, "10 min × 7 days", "70 min × 1", 0.6, 1.5) + check(260, 260, 1.4) + check(720, 210, 1.2, ok=False)
             + hand("same time, better result", 500, 950, 80, "hand blue", -2)),
    dict(bg=P["night"], text="Fact two. While you sleep, your brain locks in what you practiced. So showing up every day matters more than one big effort.",
         svg=hand("#2", 150, 200, 150, "hand orange") + moon(780, 250, 90) + snow(14, 6, "#9fb3ff") + bed(500, 640, 1.0) + zzz(660, 480, 0.8, "hand")
             + hand("sleep = save", 500, 920, 120, "hand orange", -3)),
    dict(bg=P["peach"], text="Fact three. When you repeat something again and again, the wires between your neurons get wrapped in a thin fatty layer called myelin.",
         svg=hand("#3", 150, 200, 150, "hand red") + neuron(500, 520, 1.0, myelin=6) + hand("myelin", 470, 360, 120, "hand orange", -4)
             + hand("repeat, repeat, repeat", 500, 830, 90, "hand purple", 2)),
    dict(bg=P["mint"], text="The thicker the myelin, the faster the signals travel. Like turning a dirt road into a highway.",
         svg=dirt_path(500, 300, 0.8) + '<path class="ln" style="stroke-width:9" d="M500 450 v90 M470 510 l30 35 l30 -35"/>'
             + highway(500, 700, 0.85) + car(560, 690, 0.45) + hand("faster signals", 500, 950, 100, "hand green", -3)),
    dict(bg=P["lilac"], text="And many experts believe that slow, precise practice builds skills best. Slow is smooth. And smooth becomes fast.",
         svg=snail(420, 560, 1.4) + hand("slow", 180, 250, 105, "hand purple", -5) + hand("→ smooth", 480, 250, 100, "hand blue", -3)
             + hand("→ fast", 820, 250, 100, "hand green", 3) + hand("precise > rushed", 500, 920, 90, "hand red", -2)),
    dict(bg=P["yellow"], text="So here's the secret. A little every day, slowly and carefully. Your brain will do the rest.",
         svg=calendar(500, 470, 100, cols=7, rows=1, open_=(1, 2, 3, 4, 5, 6, 7)) + brain(500, 730, 0.7)
             + hand("a little every day", 500, 250, 110, "hand orange", -3) + hand("your brain does the rest", 500, 960, 85, "hand purple", 2)),
]
