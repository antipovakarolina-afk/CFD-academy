"""Рисованный стиль, для монетизации (>60 c). Тревожность: спокойный поддерживающий тон, без вопроса зрителям.

Факты:
- Тревога — реакция «бей или беги»: миндалина (amygdala) сигналит об угрозе, выброс адреналина и кортизола →
  учащённое сердцебиение, частое дыхание, напряжение мышц.
- Мозг реагирует не только на реальную, но и на воображаемую/ожидаемую угрозу — мысли запускают ту же реакцию.
- ВОЗ (2023, данные за 2019): ~301 млн человек в мире с тревожным расстройством — самые распространённые психические расстройства.
- Balban et al., Cell Reports Medicine, 2023 (Стэнфорд): 5 мин в день «циклического вздоха» (cyclic sighing —
  двойной вдох, долгий выдох) улучшали настроение и снижали тревожность сильнее, чем медитация осознанности.
- Техника заземления 5-4-3-2-1; регулярная физическая активность снижает тревожность; избегание поддерживает тревогу,
  постепенные маленькие шаги (экспозиция) её уменьшают.
- Не медицинский совет. Тревожные расстройства хорошо лечатся.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import *  # noqa

VOICE = "af_heart"
SPEED = 0.98
MOTION_FPS = 12
P = PASTEL

SENSES = [("eye", "5 things you see"), ("hand", "4 you can touch"), ("ear", "3 you hear"), ("nose", "2 you smell"), ("mouth", "1 you taste")]

SCENES = [
    dict(bg=P["lilac"], text="What did I google today? Why does anxiety feel so real? Because your body thinks you're in danger.",
         svg=intro_search("why do i feel anxious?", "#ddd0ff")),
    dict(bg=P["peach"], text="Anxiety is your body's alarm system. A tiny part of your brain, the amygdala, spots a threat and hits the panic button.",
         svg=mv(brain_face(330, 560, 1.0, "scared"), "shake", a=5, p=0.25) + mv(alarm_clock(760, 460, 0.9), "shake", a=10, p=0.15)
             + mv(hand("RING!", 760, 220, 120, "hand red", -8), "pulse", a=0.15, p=0.25) + mv(hand("fight or flight", 500, 930, 100, "hand purple", -2), "stamp", d=2.5)),
    dict(bg=P["pink"], text="Your heart races. Your breathing speeds up. Your muscles get tense. Your body is getting ready to run.",
         svg=mv(heart(260, 420, 1.2), "pulse", a=0.25, p=0.3) + mv(lungs(720, 470, 0.75), "pulse", a=0.12, p=0.35)
             + mv(sneaker(500, 820, 0.7), "shake", a=8, p=0.2) + mv(hand("ready to run!", 500, 180, 110, "hand red", -4), "appear", d=2.0)),
    dict(bg=P["yellow"], text="Here's the tricky part. Your brain can't always tell a real lion from a scary email. Both can set off the same alarm.",
         svg=mv(lion(270, 470, 0.95), "bounce", a=20, p=0.7) + hand("=", 500, 500, 200, "hand purple") + mv(envelope(740, 470, 0.95), "shake", a=6, p=0.3)
             + mv(brain_face(500, 820, 0.55, "scared"), "shake", a=4, p=0.3)),
    dict(bg=P["blue"], text="And you're not alone. Around three hundred million people worldwide live with an anxiety disorder.",
         svg="".join(mv(person(130 + (k % 6) * 150, 330 + (k // 6) * 300, 0.33, "smile", "down"), "appear", d=round(0.2 + k * 0.1, 2)) for k in range(12))
             + mv(hand("~300,000,000", 500, 950, 130, "hand blue", -3), "stamp", d=2.0)),
    dict(bg=P["mint"], text="So what helps? Breathe in twice through your nose, then let out a long, slow breath. A Stanford study found this calms people down.",
         svg=mv(lungs(500, 520, 1.0, "#9fe0b8"), "pulse", a=0.18, p=1.6) + mv(hand("in, in...", 230, 230, 100, "hand green", -4), "appear", d=1.0)
             + mv(hand("ouuut", 780, 230, 110, "hand blue", 4), "appear", d=2.4) + mv(brain_face(500, 900, 0.45, "calm"), "bob", a=10, p=1.6)),
    dict(bg=P["yellow"], text="Or try the five, four, three, two, one trick. Notice five things you see, four you can touch, three you hear, two you smell, and one you taste.",
         svg="".join(mv(sense_icon(kind, 220, 180 + k * 170, 0.9), "appear", d=round(0.8 + k * 1.3, 1))
                     + mv(hand(label, 600, 200 + k * 170, 80, "hand purple", 0), "appear", d=round(1.0 + k * 1.3, 1)) for k, (kind, label) in enumerate(SENSES))),
    dict(bg=P["peach"], text="Move your body. Even a short walk helps your body use up all that alarm energy.",
         svg=mv(person(200, 600, 0.8, "smile", "down"), "move", x=600) + mv(sun(820, 220, 80), "spin", p=8)
             + mv(xtree(400, 520, 0.4), "bob", a=6, p=1.0) + mv(hand("just walk", 500, 940, 120, "hand orange", -3), "appear", d=1.5)),
    dict(bg=P["lilac"], text="And don't run from what scares you. Take tiny steps toward it. Each small step teaches your brain: I'm safe.",
         svg=stairs(560, 760, 1.0) + mv(person(330, 640, 0.55, "smile", "down"), "move", x=380, y=-280) + mv(star(900, 220, 1.0), "spin", p=3)
             + mv(hand("tiny steps", 500, 180, 120, "hand purple", -4), "appear", d=1.0) + mv(hand("I'm safe", 800, 330, 90, "hand green", 6), "stamp", d=3.5)),
    dict(bg=P["mint"], text="Anxiety is an alarm, not a verdict. And if it starts getting in the way of your life, talk to a doctor. It's very treatable.",
         svg=mv(brain_face(500, 480, 1.1, "calm"), "bob", a=14, p=1.4) + mv(heart(250, 260, 0.6), "pulse", a=0.12, p=0.8) + mv(heart(780, 300, 0.5, "#b79bff"), "pulse", a=0.12, p=0.9)
             + mv(hand("you're not broken", 500, 860, 100, "hand purple", -3), "appear", d=1.5) + mv(hand("it's treatable", 500, 970, 90, "hand green", 2), "appear", d=4.0)),
]
