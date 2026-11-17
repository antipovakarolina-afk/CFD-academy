"""3D-версия «Why do we give gifts at Christmas?» (тот же текст и факты, что в reels/2026-11-17-why-gifts)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from reel3d import O, L  # noqa
from doodles import PASTEL as P  # noqa

VOICE = "af_heart"
SPEED = 1.05
R, PU, GR, OR, BL, PI = "#d7263d", "#7b3fe4", "#1f9d55", "#f08a00", "#2f6fdb", "#e0457b"

SCENES = [
    dict(bg=P["pink"], text="What did I google today? Why do we give each other gifts at Christmas? Turns out, it's way older than Christmas.",
         objs=[O("phone", 500, 780, 0.85, ["why do we give gifts?"], r=(-0.1, 0, 0)), O("star", 170, 560, 0.5), O("star", 840, 520, 0.35, ["#ff8fb1"])],
         labels=[L("what did I", 500, 120, 95), L("google", 500, 250, 170, google=True), L("today?", 500, 340, 95)]),
    dict(bg=P["yellow"], text="It started in ancient Rome. During a winter festival called Saturnalia, people gave each other small gifts, like candles and tiny clay figures.",
         objs=[O("candle", 230, 700, 1.0, [1.1]), O("candle", 380, 720, 0.9, [0.8]), O("figurine", 620, 720, 1.1), O("figurine", 800, 730, 0.9, ["#b9a7d6"])],
         labels=[L("ancient Rome", 500, 120, 130, OR, -3), L("Saturnalia", 500, 950, 120, R, 3)]),
    dict(bg=P["night"], text="Then came the Christmas story. Three wise men followed a star, and brought baby Jesus gifts. Gold, frankincense, and myrrh.",
         objs=[O("snow", 500, 500, 1.0, [50, 3], spin=0), O("star", 500, 200, 1.0),
               O("gift", 230, 760, 0.8, ["#ffd23f", "#e63946"]), O("gift", 500, 780, 0.8, ["#b79bff", "#ffd23f"]), O("gift", 770, 760, 0.8, ["#2e9d5b", "#ffd23f"])],
         labels=[L("gold", 230, 870, 80, OR), L("frankincense", 500, 960, 66, "#b79bff"), L("myrrh", 770, 870, 80, "#5cc06a")]),
    dict(bg=P["peach"], text="And then there's Saint Nicholas, a real bishop who lived about seventeen hundred years ago. Legend says he secretly gave bags of gold to a poor family.",
         objs=[O("bag", 500, 700, 1.3)],
         labels=[L("Saint Nicholas", 500, 120, 120, R, -3), L("in secret", 500, 940, 110, PU, 3)]),
    dict(bg=P["mint"], text="The gold landed in stockings, drying by the fire. That's why we still hang stockings today!",
         objs=[O("fireplace", 500, 830, 1.0, spin=0.4), O("stocking", 330, 420, 0.85, ["#e63946"], z=0.7), O("stocking", 670, 420, 0.85, ["#4fa3f7"], z=0.7),
               O("coin", 360, 150, 0.8, z=0.7), O("coin", 700, 130, 0.8, z=0.7)],
         labels=[L("stockings!", 500, 960, 120, R, -3)]),
    dict(bg=P["lilac"], text="In many countries, kids still get gifts on Saint Nicholas Day, December 6.",
         objs=[O("calendar", 500, 500, 1.4, ["DEC", "6"])],
         labels=[L("St. Nicholas Day", 500, 900, 110, PU, -3)]),
    dict(bg=P["blue"], text="Then in 1823, a famous poem, 'Twas the Night Before Christmas, gave Santa his sleigh and reindeer. And gifts moved to Christmas Eve.",
         objs=[O("scroll", 360, 540, 1.1), O("moon", 790, 300, 1.0), O("star", 700, 560, 0.4), O("star", 870, 470, 0.3, ["#ff8fb1"])],
         labels=[L("1823", 790, 740, 140, BL, 6), L("the night before Christmas", 500, 960, 75, PU, -2)]),
    dict(bg=P["yellow"], text="Fun fact. Wrapping paper was born by accident. In 1917, a shop ran out of tissue paper, and sold fancy envelope paper instead. It sold out!",
         objs=[O("paperRoll", 420, 560, 1.0, r=(0.35, -0.3, 0)), O("gift", 830, 640, 0.6)],
         labels=[L("fun fact", 500, 110, 120, PI, -4), L("1917", 500, 830, 140, R, -3), L("sold out!", 500, 960, 100, GR, 3)]),
    dict(bg=P["pink"], text="And science says giving makes you happier. In one study, people who spent money on others felt happier than those who spent it on themselves.",
         objs=[O("brain", 300, 540, 0.9), O("heart", 730, 520, 1.1)],
         labels=[L("+", 520, 560, 150, R), L("giving = happier", 500, 910, 110, PU, -3)]),
    dict(bg=P["mint"], text="So a gift is basically a two thousand year old way of saying: I thought about you.",
         objs=[O("gift", 500, 650, 1.3, ["#e63946", "#ffd23f"]), O("heart", 500, 160, 0.5)],
         labels=[L("I thought about you", 500, 920, 100, R, -2)]),
    dict(bg=P["lilac"], text="What's the best gift you've ever given someone? Tell me in the comments!",
         objs=[O("gift", 330, 760, 0.75), O("heart", 690, 740, 0.8)],
         labels=[L("comment!", 500, 970, 120, R, -3)], bubble="best gift you gave?"),
]
