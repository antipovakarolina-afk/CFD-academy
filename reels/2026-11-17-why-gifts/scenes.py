"""Рисованный стиль, для монетизации TikTok (ролик ДЛИННЕЕ 60 секунд).
What did I google today? — Why do we give gifts at Christmas?

Факты:
- Сатурналии (Рим, декабрь): обмен небольшими подарками — свечи (cerei), глиняные фигурки (sigillaria).
- Евангелие от Матфея: волхвы принесли золото, ладан и смирну.
- Святой Николай Мирликийский (IV век, ~1700 лет назад): легенда о трёх мешочках золота для бедной семьи,
  по поздним версиям — упали в чулки у очага; отсюда традиция чулок.
- День святого Николая, 6 декабря — во многих странах Европы дети получают подарки.
- 1823: «A Visit from St. Nicholas» («'Twas the Night Before Christmas») — сани, олени, подарки в ночь перед Рождеством.
- 1917, Канзас-Сити: в магазине кончилась папиросная бумага, стали продавать декоративную конвертную —
  начало современной подарочной бумаги.
- Dunn, Aknin, Norton (Science, 2008): траты на других повышают счастье сильнее, чем траты на себя.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.05
P = PASTEL

SCENES = [
    dict(bg=P["pink"], text="What did I google today? Why do we give each other gifts at Christmas? Turns out, it's way older than Christmas.",
         svg=intro_search("why do we give gifts?")),
    dict(bg=P["yellow"], text="It started in ancient Rome. During a winter festival called Saturnalia, people gave each other small gifts, like candles and tiny clay figures.",
         svg=hand("ancient Rome", 500, 220, 130, "hand orange", -3) + candle(300, 600, 0.9) + candle(430, 630, 0.7)
             + figurine(640, 640, 1.1) + figurine(800, 660, 0.9, "#b9a7d6") + hand("Saturnalia", 500, 930, 120, "hand red", 3)),
    dict(bg=P["night"], text="Then came the Christmas story. Three wise men followed a star, and brought baby Jesus gifts. Gold, frankincense, and myrrh.",
         svg=snow(16, 6, "#9fb3ff") + star(500, 230, 3.0) + gift(260, 640, 0.8, "#ffd23f", "#e63946")
             + gift(500, 660, 0.8, "#b79bff", "#ffd23f") + gift(740, 640, 0.8, "#2e9d5b", "#ffd23f")
             + hand("gold", 250, 850, 80, "hand orange") + hand("frankincense", 500, 930, 66, "hand purple") + hand("myrrh", 760, 850, 80, "hand green")),
    dict(bg=P["peach"], text="And then there's Saint Nicholas, a real bishop who lived about seventeen hundred years ago. Legend says he secretly gave bags of gold to a poor family.",
         svg=hand("Saint Nicholas", 500, 210, 120, "hand red", -3) + gold_bag(500, 560, 1.5) + hand("in secret", 500, 920, 110, "hand purple", 3)),
    dict(bg=P["mint"], text="The gold landed in stockings, drying by the fire. That's why we still hang stockings today!",
         svg=fireplace(500, 600, 1.1) + sock(330, 280, 0.6, "#e63946", 0, False) + sock(670, 280, 0.6, "#4fa3f7", 0, False)
             + coin(350, 150, 0.8) + coin(690, 140, 0.8) + hand("stockings!", 500, 930, 120, "hand red", -3)),
    dict(bg=P["lilac"], text="In many countries, kids still get gifts on Saint Nicholas Day, December 6.",
         svg=cal_page(500, 500, 1.3, "DEC", "6") + hand("St. Nicholas Day", 500, 880, 110, "hand purple", -3)),
    dict(bg=P["blue"], text="Then in 1823, a famous poem, 'Twas the Night Before Christmas, gave Santa his sleigh and reindeer. And gifts moved to Christmas Eve.",
         svg=scroll(380, 540, 1.0) + moon(780, 330, 90) + star(700, 560, 1.0) + star(860, 480, 0.7, "#ff8fb1")
             + hand("1823", 780, 720, 140, "hand blue", 6) + hand("the night before Christmas", 500, 950, 75, "hand purple", -2)),
    dict(bg=P["yellow"], text="Fun fact. Wrapping paper was born by accident. In 1917, a shop ran out of tissue paper, and sold fancy envelope paper instead. It sold out!",
         svg=hand("fun fact", 500, 210, 120, "hand pink", -4) + paper_roll(380, 540, 1.1) + gift(830, 620, 0.6)
             + hand("1917", 500, 820, 140, "hand red", -3) + hand("sold out!", 500, 960, 100, "hand green", 3)),
    dict(bg=P["pink"], text="And science says giving makes you happier. In one study, people who spent money on others felt happier than those who spent it on themselves.",
         svg=brain(330, 520, 1.0) + heart(720, 500, 1.4) + hand("+", 520, 540, 150, "hand red")
             + hand("giving = happier", 500, 900, 110, "hand purple", -3)),
    dict(bg=P["mint"], text="So a gift is basically a two thousand year old way of saying: I thought about you.",
         svg=gift(500, 520, 1.5, "#e63946", "#ffd23f") + heart(500, 230, 0.6) + hand("I thought about you", 500, 900, 100, "hand red", -2)),
    dict(bg=P["lilac"], text="What's the best gift you've ever given someone? Tell me in the comments!",
         svg=bubble(500, 300, 820, 220, "#fff", "best gift you gave?", 80, "hand purple")
             + gift(330, 700, 0.8) + heart(680, 690, 0.9) + hand("comment!", 500, 960, 120, "hand red", -3)),
]
