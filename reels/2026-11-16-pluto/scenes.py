"""What did I google today? — Why Pluto is not a planet anymore (+ 3 facts).

Факты:
- 2006, Международный астрономический союз (IAU): планета = вращается вокруг Солнца, круглая,
  «расчистила» свою орбиту. Плутон делит орбиту с телами пояса Койпера → «карликовая планета».
- Плутон меньше Луны: ~2 377 км против ~3 474 км.
- Имя предложила 11-летняя Венеция Берни (Оксфорд, Англия) в 1930 году.
- Год на Плутоне ≈ 248 земных лет; с открытия (1930) он ещё не сделал полного оборота (≈2178).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.08
P = PASTEL
PLUTO = "#d9b48f"

SCENES = [
    dict(bg=P["blue"], text="What did I google today?",
         svg=blob(330, 600, 300, "#cfe0ff") + me(330, 640, 0.9, "phone", "o")
             + hand("what did I", 720, 330, 85) + google_word(720, 470, 150) + hand("today?", 720, 580, 85)
             + star(850, 220, 1.2) + star(620, 760, 0.9, "#ff8fb1")),
    dict(bg=P["lilac"], text="Why is Pluto not a planet anymore?",
         svg=blob(500, 560, 300, "#ddd0ff", 1) + planet(500, 560, 190, PLUTO, face="sad")
             + hand("not a planet?!", 500, 230, 120, "hand purple", -4)),
    dict(bg=P["night"], text="I grew up with nine planets. Then in two thousand six, scientists basically said: sorry Pluto, you're out!",
         svg=planet(70, 500, 22, "#b0a8a0") + planet(150, 500, 34, "#f2c46d") + planet(250, 500, 36, "#4fa3f7")
             + planet(340, 500, 28, "#e0603a") + planet(480, 500, 80, "#e8b27d", stripes="#c47a45")
             + planet(660, 500, 60, "#f1d28a", ring="#c9a659") + planet(800, 500, 44, "#8fd3e8")
             + planet(895, 500, 42, "#3d6fe0") + planet(960, 640, 16, PLUTO)
             + check(960, 640, 1.3, ok=False) + hand("2006", 500, 300, 170, "hand orange", -4)),
    dict(bg=P["yellow"], text="To be a planet, you need three things. Orbit the Sun. Be round. And clear your neighborhood.",
         svg=hand("1. orbit the Sun", 470, 300, 100) + check(850, 270, 1)
             + hand("2. be round", 420, 520, 100) + check(850, 490, 1)
             + hand("3. clear your orbit", 470, 740, 100, "hand red") + check(850, 710, 1, ok=False)),
    dict(bg=P["night"], text="Pluto shares its orbit with tons of icy rocks in the Kuiper belt. So it failed number three.",
         svg="".join(rock(120 + (i * 137) % 780, 250 + (i * 263) % 560, 0.8 + (i % 3) * 0.4,
                          ["#b9a7d6", "#9cc5e8", "#c9c2b8"][i % 3]) for i in range(22))
             + planet(500, 560, 90, PLUTO, face="o") + hand("Kuiper belt", 500, 930, 110, "hand orange")),
    dict(bg=P["pink"], text="Now, three facts that made me love Pluto even more.",
         svg=blob(500, 520, 320, "#ffc9dc", 2) + hand("3", 500, 640, 460, "hand pink", -6)
             + hand("facts", 500, 860, 140, "hand purple", 4) + star(240, 300, 1.3) + star(780, 330, 1.0, "#7b3fe4")),
    dict(bg=P["mint"], text="Fact one. Pluto is smaller than our Moon. Yes, our Moon!",
         svg=hand("#1", 160, 230, 150, "hand green") + planet(370, 560, 230, "#d6d6d6", face="smile")
             + '<circle class="ln" cx="270" cy="640" r="30" style="fill:#bdbdbd;stroke-width:4"/>'
             + '<circle class="ln" cx="470" cy="430" r="22" style="fill:#bdbdbd;stroke-width:4"/>'
             + planet(790, 640, 155, PLUTO, face="o")
             + hand("Moon", 370, 880, 110, "hand blue") + hand("Pluto", 790, 880, 110, "hand orange")),
    dict(bg=P["peach"], text="Fact two. It was named by an eleven year old girl from England, Venetia Burney, in nineteen thirty.",
         svg=hand("#2", 160, 230, 150, "hand orange") + girl(380, 580, 1.0) + planet(780, 470, 110, PLUTO, face="smile")
             + hand("age 11", 760, 730, 120, "hand pink", -6) + hand("1930", 760, 880, 110, "hand purple", 4)),
    dict(bg=P["night"], text="Fact three. One year on Pluto lasts two hundred forty eight Earth years. Since we found it, it hasn't even finished one lap!",
         svg=hand("#3", 160, 230, 150, "hand orange")
             + '<ellipse class="ln" cx="500" cy="560" rx="400" ry="230" style="stroke:#8fa6ff;stroke-dasharray:4 22;stroke-width:8"/>'
             + '<path class="ln" style="stroke:#ffd23f;stroke-width:10" d="M100 560 A400 230 0 0 1 680 355"/>'
             + sun(430, 560, 80) + planet(680, 355, 40, PLUTO, face="o")
             + hand("248 years", 640, 880, 130, "hand pink", -4)),
    dict(bg=P["lilac"], text="So now Pluto is a dwarf planet. Small, but famous. Honestly? Same.",
         svg=blob(650, 500, 260, "#ddd0ff", 3) + planet(650, 500, 140, PLUTO, face="smile")
             + g(650, 335, 0.8, '<path class="ln" style="fill:#ffd23f" d="M-90 0 L-70 -80 L-30 -30 L0 -100 L30 -30 L70 -80 L90 0 Z"/>')
             + me(260, 640, 0.75, "wave", "big")
             + hand("dwarf planet", 650, 760, 110, "hand purple", -3) + hand("same :)", 650, 900, 100, "hand pink", 4)
             + star(880, 250, 1.2) + star(470, 250, 0.9, "#ff8fb1")),
]
