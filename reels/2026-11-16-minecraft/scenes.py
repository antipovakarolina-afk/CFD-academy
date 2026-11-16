"""What did I google today? — Minecraft facts.

Факты (сверено 16.11.2026):
- Первую версию Маркус Перссон (Notch) сделал примерно за неделю, вышла 17 мая 2009.
- Крипер — ошибка в коде: Notch делал свинью, перепутал размеры, вышло высокое узкое существо (Notch, 2009/2012).
- Звуки гаста — кот композитора C418 (Даниэля Розенфельда), который сердится, когда его будят (AMA C418).
- Мир Minecraft ~60 млн блоков в ширину (1 блок = 1 м) → ~3,6 млрд км², ≈ 7 площадей Земли (510 млн км²).
- 2014: Microsoft купила Mojang за $2,5 млрд.
- Самая продаваемая игра: 350+ млн копий (Mojang, апрель 2025; на Minecraft Live 2026 называли 425+ млн).
Персонажей и графику игры не копируем — только наши рисунки.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.1
P = PASTEL
GRASS = dict(top="#6cc24a", left="#8b5a2b", right="#6e4520")
STONE = dict(top="#b8bcc4", left="#8d929b", right="#73787f")
GOLD = dict(top="#ffd23f", left="#e0a800", right="#c48f00")

SCENES = [
    dict(bg=P["mint"], text="What did I google today? Minecraft facts. And number two is my favorite.",
         svg=intro_search("minecraft facts")),
    dict(bg=P["yellow"], text="Fact one. The first version was made by one guy, Markus Persson, in about a week. May two thousand nine.",
         svg=hand("#1", 150, 200, 150, "hand green") + calendar(500, 420, 80, cols=7, rows=1, open_=(1, 2, 3, 4, 5, 6, 7))
             + hand("about 1 week", 500, 590, 120, "hand red", -3) + cube(380, 790, 70, **GRASS) + cube(520, 790, 70, **STONE)
             + cube(450, 720, 70, **GRASS) + hand("2009", 800, 860, 120, "hand purple", 6)),
    dict(bg=P["pink"], text="Fact two. The famous green monster was a coding mistake! He tried to make a pig, mixed up the sizes, and got this tall weird thing.",
         svg=hand("#2", 150, 200, 150, "hand pink") + pig(300, 600, 0.9) + '<path class="ln" style="stroke-width:9" d="M520 600 h110 M600 570 l30 30 l-30 30"/>'
             + pig(780, 640, 0.75, tall=True) + hand("oops!", 780, 220, 130, "hand red", 8) + hand("a pig... kind of", 500, 940, 90, "hand purple", -2)),
    dict(bg=P["night"], text="Fact three. The creepy sounds of the floating ghost monster? That's the composer's cat. Grumpy, because someone woke it up.",
         svg=hand("#3", 150, 200, 150, "hand orange") + cat_sleep(420, 620, 1.2) + mic(830, 420, 0.9)
             + hand("real cat sounds", 500, 900, 105, "hand pink", -3)),
    dict(bg=P["blue"], text="Fact four. A Minecraft world is about sixty million blocks wide. That's around seven times the surface of the Earth!",
         svg=hand("#4", 150, 200, 150, "hand blue")
             + "".join(cube(260 + c * 120 + (r % 2) * 60, 360 + r * 60, 60, **(GRASS if (r + c) % 3 else STONE)) for r in range(5) for c in range(5))
             + earth(820, 830, 75) + hand("x7", 650, 860, 130, "hand red", 6) + hand("60,000,000 blocks wide", 500, 980, 75, "hand")),
    dict(bg=P["peach"], text="Fact five. In twenty fourteen, Microsoft bought it for two and a half billion dollars.",
         svg=hand("#5", 150, 200, 150, "hand orange") + moneybag(500, 520, 1.6, "$") + hand("$2.5 billion", 500, 860, 140, "hand green", -3)
             + hand("2014", 820, 300, 120, "hand purple", 8)),
    dict(bg=P["lilac"], text="Bonus: it's the best selling video game ever. More than three hundred fifty million copies!",
         svg=crown(500, 230, 1.3) + cube(500, 470, 130, **GOLD) + hand("350,000,000+", 500, 820, 130, "hand purple", -3)
             + star(200, 330, 1.3) + star(820, 400, 1.0, "#ff8fb1") + pickaxe(190, 640, 0.6, -30)),
    dict(bg=P["yellow"], text="So, which fact surprised you the most? Tell me in the comments!",
         svg=bubble(500, 330, 800, 220, "#fff", "which one? 1, 2, 3, 4, 5?", 70, "hand purple")
             + cube(330, 700, 90, **GRASS) + cube(510, 700, 90, **STONE) + cube(420, 640, 90, **GOLD)
             + pickaxe(760, 700, 0.7, 25) + hand("comment!", 500, 960, 120, "hand red", -3)),
]
