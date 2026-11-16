"""Рисованный стиль. What did I google today? — How long can you survive without sleep?

Факты (нейробиология, общеизвестные исследования):
- 1964: Рэнди Гарднер, 17 лет, не спал 264 часа (~11 дней); наблюдал исследователь сна Уильям Демент.
  Были галлюцинации, проблемы с речью и памятью. Guinness перестал регистрировать такие рекорды из-за опасности.
- Williamson & Feyer (2000): 17–19 ч без сна ≈ эффект 0,05% алкоголя в крови; Dawson & Reid (1997): ~24 ч ≈ 0,10%
  (лимит для вождения в большинстве штатов США — 0,08%).
- Микросон — «выключения» на секунды, человек их не замечает.
- Глимфатическая система: во сне мозг активнее выводит отходы (в т.ч. бета‑амилоид) — Xie et al., 2013, на мышах.
- Rechtschaffen (1980‑е): крысы при полном лишении сна погибали примерно за 2–3 недели.
- Точный предел для людей неизвестен (опыты неэтичны). Взрослым рекомендуют 7+ часов сна (AASM).
Не медицинский совет; не призываем повторять.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 1.1
P = PASTEL

SCENES = [
    dict(bg=P["lilac"], text="What did I google today? How long can you survive without sleep? The answer is kind of scary.",
         svg=intro_search("how long without sleep?", "#ddd0ff")),
    dict(bg=P["yellow"], text="The record. In 1964, a seventeen year old student named Randy Gardner stayed awake for 264 hours. That's eleven days!",
         svg=hand("record", 500, 200, 130, "hand purple", -4) + calendar(500, 470, 90, cols=6, rows=2, open_=tuple(range(1, 12)))
             + hand("264 hours", 500, 760, 170, "hand red", -3) + hand("1964", 820, 930, 110, "hand blue", 6)),
    dict(bg=P["peach"], text="By the end, he was seeing things that weren't there, and he struggled to speak. Record books stopped accepting this record. It's too dangerous.",
         svg=tired_eye(500, 430, 1.6, 0.25) + hand("hallucinations", 500, 720, 120, "hand purple", -3)
             + hand("too dangerous", 500, 900, 110, "hand red", 3)),
    dict(bg=P["yellow"], text="Science fact. After about 18 hours awake, your brain works like you had a drink. After 24 hours, it's like being over the legal driving limit.",
         svg=clock12(250, 360, 1.0) + hand("18 h", 250, 560, 110, "hand orange") + glass(250, 790, 0.8)
             + clock12(750, 360, 1.0) + hand("24 h", 750, 560, 110, "hand red") + glass(690, 790, 0.8) + glass(810, 790, 0.8)),
    dict(bg=P["blue"], text="And your brain starts taking micro sleeps. It switches off for a few seconds, and you don't even notice. Imagine that while driving.",
         svg=car(500, 560, 1.3, "#e63946") + zzz(720, 360, 1.0) + hand("micro sleep", 500, 260, 120, "hand blue", -3)
             + hand("a few seconds", 500, 860, 110, "hand red", 3)),
    dict(bg=P["mint"], text="Neuroscience fact. While you sleep, your brain literally washes itself, flushing out waste that builds up during the day.",
         svg=brain(500, 520, 1.4) + drops(500, 520, 1.2, 8) + hand("brain wash", 500, 220, 130, "hand green", -3)
             + hand("cleans waste", 500, 900, 110, "hand blue", 3)),
    dict(bg=P["pink"], text="In experiments in the 1980s, rats kept awake completely, died within about two to three weeks.",
         svg=mouse(400, 560, 1.4) + calendar(500, 840, 55, cols=7, rows=3, open_=tuple(range(1, 22)))
             + hand("2–3 weeks", 760, 330, 120, "hand red", 6)),
    dict(bg=P["night"], text="So how long can humans last? Nobody knows exactly, and no scientist will test it. Adults need at least 7 hours. Please don't try this.",
         svg=snow(16, 4, "#9fb3ff") + moon(500, 380, 110) + bed(500, 700, 1.0) + zzz(650, 560, 0.8, "hand")
             + hand("7+ hours", 500, 940, 130, "hand orange", -3)),
    dict(bg=P["lilac"], text="What's the longest you've ever stayed awake? Tell me in the comments, in hours!",
         svg=bubble(500, 300, 820, 220, "#fff", "your record? __ hours", 80, "hand purple")
             + clock12(330, 690, 0.9) + tired_eye(700, 690, 0.9, 0.3) + hand("comment!", 500, 960, 120, "hand red", -3)),
]
