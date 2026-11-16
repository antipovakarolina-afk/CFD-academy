"""Тёмный стиль. Why is Christmas on December 25?

Факты:
- В Библии дата рождения Иисуса не указана.
- Первое записанное празднование 25 декабря — Рим, 336 г. (Хронограф 354 года).
- Одна из версий: близость к зимнему солнцестоянию (~21 декабря) и римским праздникам (Сатурналии, Sol Invictus).
- «Xmas»: X — греческая буква «хи» (Χ), первая буква слова Χριστός (Христос); сокращение используется веками.
- Красный Санта существовал до рекламы Coca-Cola (Хэддон Сандблом, 1931).
- 16 декабря 1965, «Джемини‑6»: астронавты сыграли «Jingle Bells» на губной гармошке — первая песня в космосе.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from dark import *  # noqa

VOICE = "af_heart"
SPEED = 1.12
MUSIC = "dark"
ACCENT = "#ff5a5f"

SCENES = [
    dict(title="WHY DECEMBER 25?", sub="christmas, explained",
         text="Christmas is everywhere right now. But why *December 25?* The Bible never actually gives a date.",
         svg=snowfall(16) + item(i_cal(500, 470, 1.4, "DEC", "25")) + item(pill("WHY?", 500, 880, YELLOW, 44))),
    dict(title="THE BIBLE", sub="date of birth: unknown",
         text="Not the day, not even the month. *No date at all.*",
         svg=snowfall(10, 2) + item(i_book(500, 420, 1.3)) + item(card(220, 700, 560, 180, "date of birth", RED)
             + text("? ? ?", 500, 840, 90, RED, "mono"))),
    dict(title="ROME · 336 AD", sub="the first record",
         text="The first record of Christmas on December 25 comes from *Rome,* in the year *336.*",
         svg=item(card(170, 100, 660, 330, "first record", YELLOW) + count(336, 500, 340, 170, YELLOW, "", " AD", 0, 0))
             + item(i_cal(500, 700, 0.9, "DEC", "25"))),
    dict(title="ONE THEORY", sub="the winter solstice",
         text="One theory: it's right after the *winter solstice.* The darkest days are over, and the light comes back.",
         svg=item(i_sun(500, 380, 1.3)) + item(pill("DEC 21 · SHORTEST DAY", 500, 700, BLUE, 34))
             + item(arrow(500, 760, 500, 860, YELLOW, 8)) + item(pill("THE LIGHT COMES BACK", 500, 930, YELLOW, 34))),
    dict(title="XMAS", sub="it's not disrespectful",
         text="And writing *Xmas* isn't lazy or rude. The X is the Greek letter *Chi,* the first letter of Christ in Greek.",
         svg=item(text("XMAS", 500, 330, 190, WHITE, "sans")) + item(arrow(500, 400, 500, 520, YELLOW, 8))
             + item(card(190, 560, 620, 330, "greek letter", YELLOW) + text("X = Chi", 500, 775, 100, YELLOW, "mono"))),
    dict(title="MYTH", sub="coca-cola and santa",
         text="Bonus myth: *Coca-Cola* did not invent the red Santa. He was already wearing red years before their 1931 ads.",
         svg=item(i_hat(330, 470, 1.2)) + item(i_bottle_soda(720, 470, 1.1))
             + item(pill("MYTH", 500, 860, RED, 48))),
    dict(title="SPACE · 1965", sub="the first song in space",
         text="And *Jingle Bells* was the first song ever played in *space.* Two astronauts, a harmonica, and some tiny bells. 1965.",
         svg=snowfall(8, 4) + item(i_rocket(330, 470, 1.1)) + item(i_bell(700, 380, 0.9)) + item(i_music(720, 720, 1.0))
             + item(text("1965", 500, 960, 90, YELLOW, "mono"))),
    dict(title="YOUR TURN", sub="comment below",
         text="What's *your* favorite Christmas tradition? Tell me in the comments!",
         svg=snowfall(14, 9) + item(i_hat(330, 470, 1.0)) + item(i_bell(700, 430, 0.85))
             + item(pill("COMMENT ↓", 500, 860, YELLOW, 44))),
]
