"""What did I google today? — History of the advent calendar.

Факты: обычай отсчёта (мел на двери, свечи) — немецкие лютеране, XIX век.
Герхард Ланг (Мюнхен): мама делала календарь с 24 печеньками на картоне; первые печатные
календари Ланга ~1908, позже — с окошками. Во время Второй мировой — картон по карточкам, производство встало.
1946 — Рихард Зельмер (Штутгарт) возобновил выпуск. Фото внуков Эйзенхауэра с календарём (1950-е) — популярность в США.
1958 — первые шоколадные календари.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

SCENES = [
    dict(text="What did I google today?",
         svg=person(430, 620, 1.1, "o", "front") + phone(470, 600, 0.8) + qmarks(640, 260)),
    dict(text="Who actually invented the advent calendar?",
         svg=hand("who invented it?", 500, 260, 115) + calendar(500, 600, 110)),
    dict(text="It started in Germany, back in the eighteen hundreds.",
         svg=hand("Germany", 500, 400, 170) + hand("1800s", 500, 650, 200, "hand red", -5)),
    dict(text="Families counted down to Christmas by drawing chalk lines on the door. One line every day.",
         svg=door(360, 540, 1.1, lines=9) + hand("+1", 780, 330, 150, "hand red", 8) + hand("every day", 780, 460, 90, rot=8)),
    dict(text="Or they lit a new candle every evening.",
         svg=candle(330, 580) + candle(520, 600, 0.85) + candle(690, 620, 0.7)),
    dict(text="Then a boy from Munich, Gerhard Lang, got a gift from his mom. Twenty four little cookies stuck on a piece of cardboard.",
         svg='<rect class="ln" x="160" y="250" width="680" height="480" style="fill:#e8d2a8"/>'
             + "".join(cookie(240 + c * 104, 320 + r * 110, 1.1) for r in range(4) for c in range(6))
             + hand("mom's version", 500, 860, 110, "hand red", -4)),
    dict(text="When he grew up, he printed the first advent calendars with pictures, around nineteen oh eight. Later came the little doors.",
         svg=hand("1908", 500, 260, 200) + calendar(500, 610, 105, open_=(1, 2, 3)) + hand("doors!", 500, 960, 110, "hand red", -4)),
    dict(text="During the Second World War, cardboard was rationed, and the calendars almost disappeared.",
         svg=calendar(500, 420, 90) + '<path class="ln" style="stroke:#b3122e;stroke-width:14" d="M200 230 L800 610 M800 230 L200 610"/>'
             + person(500, 820, 0.55, "worry", "down")),
    dict(text="In nineteen forty six, a printer from Stuttgart, Richard Sellmer, brought them back.",
         svg=hand("1946", 500, 300, 200) + hand("Stuttgart", 500, 470, 110) + calendar(500, 720, 70)),
    dict(text="Then a newspaper photo of President Eisenhower's grandchildren opening one made them famous in America.",
         svg=newspaper(500, 520, 1.2, "USA")),
    dict(text="In nineteen fifty eight, chocolate moved in.",
         svg=hand("1958", 500, 300, 200) + chocolate(500, 620, 1.6)),
    dict(text="And now there are calendars with cheese, wine, makeup, and even Lego.",
         svg=hand("cheese", 320, 320, 120, rot=-6) + hand("wine", 700, 420, 120, "hand red", 5)
             + hand("makeup", 330, 620, 120, rot=4) + hand("Lego", 700, 760, 140, rot=-5)),
    dict(text="And mine? Twenty four days of nuts. Thirty grams a day. I checked.",
         svg=person(380, 560, 1.0, "smile", "front") + walnut(700, 420, 1.3) + hand("30 g ✓", 720, 720, 140, "hand red", -6)),
]
