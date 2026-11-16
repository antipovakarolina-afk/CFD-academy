"""What did I google today? — Bacteria & viruses facts.

Факты:
- Старый миф «бактерий в 10 раз больше, чем клеток» опровергнут: Sender, Fuchs, Milo (2016) —
  ~38 трлн бактерий и ~30 трлн клеток человека, примерно 1:1.
- Масса бактерий в кишечнике ~0,2 кг (та же работа).
- Бактериофаги — вирусы, поражающие бактерии; их ~10^31 на Земле — больше, чем звёзд в наблюдаемой Вселенной (~10^22–10^24).
- ~8% генома человека — эндогенные ретровирусы (следы древних вирусов).
- 1928: Флеминг обнаружил пенициллин в чашке Петри, заросшей плесенью, после отпуска.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.1
P = PASTEL

SCENES = [
    dict(bg=P["mint"], text="What did I google today? Bacteria and viruses. And fact three sounds like a horror movie.",
         svg=intro_search("bacteria facts")),
    dict(bg=P["yellow"], text="Fact one. You've probably heard that there are ten times more bacteria in you than your own cells. That's a myth!",
         svg=hand("#1", 150, 200, 150, "hand green") + hand("10x more?", 500, 300, 150, "hand", -3)
             + bacterium(330, 560, 0.9, "#7ed957", 10) + bacterium(650, 600, 0.8, "#ffb347", -15, "o")
             + check(500, 830, 2.2, ok=False) + hand("myth", 760, 860, 120, "hand red", 6)),
    dict(bg=P["blue"], text="Scientists counted again. It's about thirty eight trillion bacteria and thirty trillion human cells. Pretty much one to one.",
         svg=balance(500, 560, 1.4,
                     bacterium(-220, -40, 0.45, "#7ed957", 0, None) + bacterium(-220, -100, 0.35, "#ffb347", 20, None),
                     '<circle class="ln" cx="220" cy="-40" r="50" style="fill:#ff9fb3"/><circle cx="220" cy="-40" r="16" style="fill:#d4567a"/>')
             + hand("38 trillion", 210, 260, 80, "hand green") + hand("30 trillion", 790, 260, 80, "hand pink")
             + hand("about 1 : 1", 500, 930, 130, "hand purple", -3)),
    dict(bg=P["peach"], text="Fact two. All the bacteria in your gut weigh about two hundred grams. Like a cup of yogurt!",
         svg=hand("#2", 150, 200, 150, "hand orange")
             + "".join(bacterium(300 + (i % 3) * 200, 400 + (i // 3) * 150, 0.6, c, (i * 37) % 60 - 30, "smile" if i % 2 else None)
                       for i, c in enumerate(["#7ed957", "#ffb347", "#4fa3f7", "#ff8fb1", "#b79bff", "#ffd23f"]))
             + hand("~200 g", 500, 880, 170, "hand red", -4)),
    dict(bg=P["night"], text="Fact three. There are viruses that hunt bacteria. They're called phages. And there are more of them on Earth than stars in the universe.",
         svg=hand("#3", 150, 200, 150, "hand orange") + phage(360, 560, 1.4) + bacterium(720, 720, 0.8, "#7ed957", 0, "o")
             + star(800, 260, 1.2) + star(650, 360, 0.8) + star(880, 450, 0.7, "#ff8fb1")
             + hand("more than stars", 500, 960, 100, "hand pink", -2)),
    dict(bg=P["lilac"], text="Fact four. About eight percent of your DNA came from ancient viruses. They're literally part of you.",
         svg=hand("#4", 150, 200, 150, "hand purple") + dna(400, 570, 1.2, hl=(3, 7, 11)) + virus(760, 470, 60, "#e0457b", "smile")
             + hand("~8%", 760, 760, 170, "hand red", 6)),
    dict(bg=P["mint"], text="Bonus. Penicillin was discovered by accident. In nineteen twenty eight, Alexander Fleming came back from vacation and found mould in a forgotten dish.",
         svg=petri(500, 560, 1.5) + hand("1928", 500, 260, 170, "hand green", -4) + hand("oops, mould!", 500, 880, 120, "hand orange", 3)),
    dict(bg=P["pink"], text="Which fact surprised you the most? Tell me in the comments!",
         svg=bubble(500, 300, 800, 220, "#fff", "which one? 1, 2, 3 or 4?", 75, "hand purple")
             + bacterium(300, 680, 0.8, "#7ed957", -10) + virus(700, 680, 70, "#4fa3f7", "smile")
             + hand("comment!", 500, 950, 120, "hand red", -3)),
]
