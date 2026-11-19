"""Ретро-фэнтези аниме видеоряд ~42 c, БЕЗ звука: песню «Dark Signs» (Sleep Token) автор добавляет в приложении
из лицензированной библиотеки. Свой персонаж (не участники группы), без текста песни."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from anime import *  # noqa
from doodles import mv  # noqa

NO_VOICE = True
PAUSE, INTRO, MOTION_FPS, WOBBLE, BOIL = 0.0, 0.25, 15, 0, 0.5
D = 3.0

SCENES = [
    dict(bg="#0b0726", dur=D, text="", svg=sky() + stars(110, 1) + mv(moon(500, 300, 230), "pulse", a=0.03, p=1.2) + clouds(560, 2) + mountains(1250, "#140a2b") + title("DARK SIGNS", 1130, 110, sub="FAN VISUAL")),
    dict(bg="#0b0726", dur=D, text="", svg=sky() + stars(80, 2) + moon(760, 80, 140) + clouds(250, 3, op=.7) + mountains(1000, "#1d0f3a", 4, 300) + cliff(380, 760, 900) + castle(380, 760, 1.0) + fireflies(14, 1)),
    dict(bg="#0b0726", dur=D, text="", svg=sky() + stars(60, 3) + moon(500, 140, 260) + cliff(500, 980, 1300) + hooded(500, 700, 1.25) + clouds(1100, 4, "#2b1055", .6, 200)),
    dict(bg="#120624", dur=D, text="", svg=sky("sky") + mv(anime_eye(500, 480, 1.25), "pulse", a=0.04, p=0.8)),
    dict(bg="#0b0726", dur=D, text="", svg=sky() + stars(50, 5) + magic_circle(500, 520, 380) + hooded(500, 1180, 0.9, wind=False)),
    dict(bg="#05121f", dur=D, text="", svg=sky("teal") + mountains(1100, "#06202b", 6, 250) + crystal(220, 900, 1.0) + crystal(800, 820, 1.3, "#a28bff") + crystal(520, 1050, 0.8)
         + fireflies(30, 2, "#bff6ff") + mv(crystal(500, 450, 1.6, "#ffd6ff"), "bob", a=24, p=1.0)),
    dict(bg="#0b0726", dur=D, text="", svg=sky() + stars(30, 6) + rain(80, 1) + lightning(650, -200) + mountains(1200, "#0a0518", 7, 400) + castle(300, 1000, 0.8) + mv('<rect x="-40" y="-480" width="1080" height="1920" style="fill:#f4ecff"/>', "flash", a=0.85, p=1.4, d=0.3)),
    dict(bg="#0b0726", dur=D, text="", svg=sky() + moon(820, -60, 160) + speedlines(50, 2, "#c9a7ff") + bridge(950) + mv(hooded(120, 760, 0.7), "move", x=820) + rain(40, 2)),
    dict(bg="#12030f", dur=D, text="", svg=sky("skyred") + moon(500, 100, 200, red=True) + clouds(420, 8, "#2a0618", .9, 160) + mv(dragon(500, 420, 1.4), "bob", a=30, p=1.5) + mountains(1250, "#0a0308", 9, 350)),
    dict(bg="#0b0726", dur=D, text="", svg=sky() + speedlines(70, 3, "#ffd27a") + magic_circle(500, 480, 460, "#ff9fd8") + mv('<circle cx="500" cy="480" r="120" style="fill:#fff" filter="url(#softglow)"/>', "pulse", a=0.35, p=0.3)),
    dict(bg="#12030f", dur=D, text="", svg=sky("skyred") + stars(40, 9) + moon(500, 200, 260, red=True) + cliff(500, 1000, 1300, "#0a0308") + hooded(500, 720, 1.2, eyes="#ffdd66")),
    dict(bg="#0b0726", dur=D, text="", svg=sky() + stars(70, 10) + moon(500, 380, 300) + petals(55, 3) + mountains(1300, "#140a2b", 11, 300)),
    dict(bg="#120624", dur=D, text="", svg=sky() + mv(anime_eye(500, 480, 1.1, "#ff3c8e"), "pulse", a=0.05, p=0.4) + speedlines(40, 4, "#ff8fc7")),
    dict(bg="#0b0726", dur=D, text="", svg=sky() + stars(120, 12) + mv(moon(500, 380, 250), "pulse", a=0.04, p=1.4) + hooded(500, 1000, 0.6) + petals(25, 5, "#c9a7ff") + title("DARK SIGNS", 1260, 100)),
]
