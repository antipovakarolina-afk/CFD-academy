"""Простые рисунки линией для рилсов (SVG, поле 1000×1000)."""


def g(x, y, s, body):
    return f'<g transform="translate({x},{y}) scale({s})">{body}</g>'


def hand(text, x=500, y=500, size=110, cls="hand", rot=0):
    return (f'<g class="pop"><text class="{cls}" x="{x}" y="{y}" font-size="{size}" text-anchor="middle" '
            f'transform="rotate({rot} {x} {y})">{text}</text></g>')


def person(x=500, y=520, s=1.0, mood="smile", arms="down"):
    face = {
        "smile": '<path class="ln" d="M-14 -150 q14 14 28 0"/>',
        "worry": '<path class="ln" d="M-14 -140 q14 -12 28 0"/>',
        "o": '<circle class="ln" cx="0" cy="-145" r="9"/>',
        "sly": '<path class="ln" d="M-16 -148 q20 8 30 -6"/>',
    }[mood]
    arm = {
        "down": '<path class="ln" d="M-60 -60 q-30 90 -20 170"/><path class="ln" d="M60 -60 q30 90 20 170"/>',
        "up": '<path class="ln" d="M-60 -60 q-70 -60 -90 -150"/><path class="ln" d="M60 -60 q70 -60 90 -150"/>',
        "chin": '<path class="ln" d="M-60 -60 q-30 90 -20 170"/><path class="ln" d="M60 -60 q40 40 -10 -60"/>',
        "front": '<path class="ln" d="M-60 -60 q-20 80 40 80"/><path class="ln" d="M60 -60 q20 80 -40 80"/>',
    }[arms]
    body = (
        '<path class="ln" d="M-40 -200 q40 -60 80 0 q10 60 -10 90 h-60 q-20 -30 -10 -90z"/>'
        '<circle cx="-16" cy="-175" r="6" fill="#111"/><circle cx="16" cy="-175" r="6" fill="#111"/>'
        + face +
        '<path class="ln" d="M-30 -110 q-40 20 -35 120 l5 230 M30 -110 q40 20 35 120 l-5 230"/>'
        '<path class="ln" d="M-30 240 h60 M0 120 v120"/>'
        + arm
    )
    return g(x, y, s, body)


def walnut(x, y, s=1.0):
    return g(x, y, s, '<ellipse cx="0" cy="0" rx="70" ry="60" class="ln" style="fill:#e7c9a0"/>'
                      '<path class="ln" d="M0 -60 q-15 30 0 60 q15 30 0 60" transform="translate(0,-30) scale(1,0.9)"/>'
                      '<path class="ln" d="M-40 -25 q10 10 0 25 M40 -20 q-10 15 0 30" style="stroke-width:5"/>')


def almond(x, y, s=1.0, r=0):
    return g(x, y, s, f'<path class="ln" style="fill:#d9a66b" transform="rotate({r})" '
                      'd="M0 -55 q45 30 25 75 q-25 30 -50 0 q-20 -45 25 -75z"/>')


def cashew(x, y, s=1.0, r=0):
    return g(x, y, s, f'<path class="ln" style="fill:#f1dcb0" transform="rotate({r})" '
                      'd="M-50 -20 q10 -40 50 -30 q-25 15 -10 45 q30 25 55 0 q5 45 -45 45 q-55 0 -50 -60z"/>')


def brazil(x, y, s=1.0, r=0):
    return g(x, y, s, f'<path class="ln" style="fill:#8a5a3b" transform="rotate({r})" '
                      'd="M-25 -80 q50 -10 55 20 l-5 120 q-25 25 -50 0 l-20 -110 q0 -20 20 -30z"/>')


def phone(x, y, s=1.0):
    return g(x, y, s, '<rect class="ln" x="-45" y="-80" width="90" height="160" rx="18" style="fill:#111"/>')


def calendar(x=500, y=500, cell=110, cols=6, rows=4, nums=True, open_=()):
    out = []
    x0, y0 = x - cols * cell / 2, y - rows * cell / 2
    n = 1
    for r in range(rows):
        for c in range(cols):
            cx, cy = x0 + c * cell, y0 + r * cell
            fill = "#fff" if n not in open_ else "#ffe7a3"
            out.append(f'<rect class="ln" x="{cx}" y="{cy}" width="{cell}" height="{cell}" style="fill:{fill};stroke-width:5"/>')
            if nums:
                out.append(f'<text class="hand" x="{cx + cell / 2}" y="{cy + cell * 0.68}" font-size="{cell * 0.5}" text-anchor="middle">{n}</text>')
            n += 1
    return "".join(out)


def qmarks(x, y, n=3):
    return "".join(hand("?", x + i * 70, y - (i % 2) * 40, 120, rot=(-15 + i * 15)) for i in range(n))


def door(x=500, y=520, s=1.0, lines=0):
    tally = "".join(f'<path class="ln" style="stroke:#888;stroke-width:6" d="M{-110 + i * 22} -150 v70"/>' for i in range(lines))
    return g(x, y, s, '<rect class="ln" x="-170" y="-330" width="340" height="660" rx="6" style="fill:#f3e3c8"/>'
                      '<rect class="ln" x="-120" y="-280" width="240" height="250" style="stroke-width:5"/>'
                      '<rect class="ln" x="-120" y="20" width="240" height="250" style="stroke-width:5"/>'
                      '<circle class="ln" cx="125" cy="0" r="14" style="fill:#111"/>' + tally)


def candle(x=500, y=560, s=1.0):
    return g(x, y, s, '<rect class="ln" x="-50" y="-120" width="100" height="300" style="fill:#fff"/>'
                      '<path class="ln" d="M0 -120 v-30"/>'
                      '<path class="ln" style="fill:#ffcf4a" d="M0 -230 q40 50 0 80 q-40 -30 0 -80z"/>'
                      '<path class="ln" d="M-120 180 h240"/>')


def cookie(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#f0d39b;stroke-width:5" d="M-30 0 q0 -25 30 -25 q30 0 30 25 q0 25 -30 25 q-30 0 -30 -25z"/>')


def newspaper(x=500, y=520, s=1.0, title="NEWS"):
    rows = "".join(f'<path class="ln" style="stroke-width:5" d="M60 {-60 + i * 50} h170"/>' for i in range(6))
    return g(x, y, s, '<rect class="ln" x="-260" y="-260" width="520" height="560" style="fill:#fff"/>'
                      f'<text class="hand" x="0" y="-170" font-size="90" text-anchor="middle">{title}</text>'
                      '<rect class="ln" x="-220" y="-100" width="250" height="230" style="fill:#e9e9e9;stroke-width:5"/>'
                      '<circle class="ln" cx="-150" cy="0" r="25"/><circle class="ln" cx="-60" cy="10" r="20"/>'
                      '<rect class="ln" x="-120" y="50" width="70" height="50" style="fill:#ffe7a3;stroke-width:5"/>'
                      + rows + '<path class="ln" style="stroke-width:5" d="M-220 200 h450 M-220 250 h450"/>')


def chocolate(x, y, s=1.0):
    cells = "".join(f'<rect x="{-60 + c * 60}" y="{-90 + r * 60}" width="56" height="56" rx="6" style="fill:#7b4a2c"/>'
                    for r in range(3) for c in range(2))
    return g(x, y, s, '<rect class="ln" x="-70" y="-100" width="140" height="190" rx="10" style="fill:#5a3420"/>' + cells)


# ---------- цвет ----------
PASTEL = {"blue": "#e6f0ff", "yellow": "#fff4cc", "pink": "#ffe3ee", "mint": "#dff6ea", "lilac": "#eee6ff",
          "peach": "#ffe9d9", "night": "#1d2340"}


def blob(x, y, r, color, k=0):
    """мягкое цветное пятно-подложка неправильной формы"""
    import math
    pts = []
    for i in range(10):
        a = i / 10 * 2 * math.pi
        rr = r * (0.85 + 0.15 * math.sin(3 * a + k))
        pts.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    d = f"M{pts[0][0]:.0f} {pts[0][1]:.0f} " + " ".join(
        f"Q{(pts[i][0] + pts[(i + 1) % 10][0]) / 2 + 0:.0f} {(pts[i][1] + pts[(i + 1) % 10][1]) / 2:.0f} "
        f"{pts[(i + 1) % 10][0]:.0f} {pts[(i + 1) % 10][1]:.0f}" for i in range(10)) + "Z"
    return f'<path d="{d}" style="fill:{color}"/>'


def planet(x, y, r, color, ring=None, face=None, stripes=None):
    out = f'<circle class="ln" cx="{x}" cy="{y}" r="{r}" style="fill:{color}"/>'
    if stripes:
        out += "".join(f'<path class="ln" style="stroke:{stripes};stroke-width:{max(3, r // 12)}" '
                       f'd="M{x - r * 0.85} {y + o * r} q{r * 0.85} {r * 0.15} {r * 1.7} 0"/>' for o in (-0.35, 0.05, 0.4))
    if ring:
        out += (f'<ellipse class="ln" cx="{x}" cy="{y}" rx="{r * 1.7}" ry="{r * 0.45}" '
                f'style="stroke:{ring};stroke-width:{max(5, r // 8)}" transform="rotate(-15 {x} {y})"/>')
    if face:
        e = r * 0.28
        out += (f'<circle cx="{x - e}" cy="{y - e * 0.4}" r="{max(4, r * 0.07)}" style="fill:#111"/>'
                f'<circle cx="{x + e}" cy="{y - e * 0.4}" r="{max(4, r * 0.07)}" style="fill:#111"/>')
        mouth = {"smile": f"M{x - e} {y + e * 0.6} q{e} {e * 0.9} {e * 2} 0",
                 "sad": f"M{x - e} {y + e * 1.1} q{e} {-e * 0.9} {e * 2} 0",
                 "o": None}[face]
        out += (f'<path class="ln" d="{mouth}"/>' if mouth else
                f'<circle class="ln" cx="{x}" cy="{y + e * 0.8}" r="{e * 0.3}"/>')
    return out


def sun(x, y, r=110):
    import math
    rays = "".join(f'<path class="ln" style="stroke:#f08a00" d="M{x + (r + 20) * math.cos(a):.0f} {y + (r + 20) * math.sin(a):.0f} '
                   f'L{x + (r + 70) * math.cos(a):.0f} {y + (r + 70) * math.sin(a):.0f}"/>'
                   for a in [i * math.pi / 6 for i in range(12)])
    return f'<circle class="ln" cx="{x}" cy="{y}" r="{r}" style="fill:#ffd23f"/>' + rays


def star(x, y, s=1.0, color="#ffd23f"):
    return g(x, y, s, f'<path class="ln" style="fill:{color};stroke-width:5" '
                      'd="M0 -30 L8 -8 L30 0 L8 8 L0 30 L-8 8 L-30 0 L-8 -8Z"/>')


def check(x, y, s=1.0, ok=True):
    if ok:
        return g(x, y, s, '<path class="ln" style="stroke:#1f9d55;stroke-width:14" d="M-35 0 L-10 28 L40 -32"/>')
    return g(x, y, s, '<path class="ln" style="stroke:#d7263d;stroke-width:14" d="M-30 -30 L30 30 M30 -30 L-30 30"/>')


def rock(x, y, s=1.0, color="#b9a7d6"):
    return g(x, y, s, f'<path class="ln" style="fill:{color};stroke-width:5" d="M-20 -10 q10 -18 30 -8 q15 12 2 26 q-20 10 -34 -2 q-8 -8 2 -16z"/>')


def girl(x=500, y=520, s=1.0, dress="#e0457b", hair="#7a4a2a"):
    head = (f'<circle class="ln" cx="-62" cy="-190" r="26" style="fill:{hair}"/>'
            f'<circle class="ln" cx="62" cy="-190" r="26" style="fill:{hair}"/>')
    body = (f'<path class="ln" style="fill:{dress}" d="M-35 -110 L-90 140 H90 L35 -110 Z"/>'
            '<path class="ln" d="M-30 140 v100 M30 140 v100 M-45 240 h30 M15 240 h30"/>')
    return g(x, y, s, head + body) + person(x, y, s, "smile", "down").replace('class="ln" d="M-30 -110', 'class="ln" style="opacity:0" d="M-30 -110', 1)


# ---------- героиня блога (оригинальный персонаж) ----------
GOOGLE = ["#4285F4", "#EA4335", "#FBBC05", "#4285F4", "#34A853", "#EA4335"]


def google_word(x=500, y=500, size=150, rot=0, word="google"):
    spans = "".join(f'<tspan style="fill:{GOOGLE[i % 6]}">{ch}</tspan>' for i, ch in enumerate(word))
    return (f'<g class="pop"><text class="hand" x="{x}" y="{y}" font-size="{size}" text-anchor="middle" '
            f'transform="rotate({rot} {x} {y})">{spans}</text></g>')


def me(x=500, y=620, s=1.0, pose="phone", mood="smile",
       hair="#1f2a5a", skin="#f7d9c4", sweater="#5b8def", stripe="#ff8fb1", skirt="#3b2a4a", shoes="#7a1f3d"):
    """Героиня: тёмно-синее каре с чёлкой, заколка-звёздочка, большие глаза, свитер в полоску."""
    mouth = {
        "smile": '<path class="ln" style="stroke-width:6" d="M-20 -182 q20 18 40 0"/>',
        "big": '<path class="ln" style="fill:#c0392b;stroke-width:6" d="M-24 -186 q24 34 48 0 z"/>',
        "o": '<ellipse class="ln" style="fill:#7a2230;stroke-width:5" cx="0" cy="-178" rx="10" ry="13"/>',
        "worry": '<path class="ln" style="stroke-width:6" d="M-18 -172 q18 -14 36 0"/>',
    }[mood]
    stripes = ""
    for yy in (-75, -30, 15):
        hw = 62 + (yy + 118) / 178 * 23
        stripes += f'<path class="ln" style="stroke:{stripe};stroke-width:16;stroke-linecap:butt" d="M{-hw + 6:.0f} {yy} H{hw - 6:.0f}"/>'
    arms = {
        "phone": ('<path class="ln" d="M-62 -105 Q-105 -20 -22 -25"/><path class="ln" d="M62 -105 Q105 -20 22 -25"/>'
                  '<rect class="ln" x="-26" y="-95" width="52" height="88" rx="10" style="fill:#222"/>'
                  f'<circle cx="-22" cy="-25" r="13" style="fill:{skin}" class="ln"/><circle cx="22" cy="-25" r="13" style="fill:{skin}" class="ln"/>'),
        "wave": ('<path class="ln" d="M-62 -105 Q-100 -10 -92 55"/>'
                 '<path class="ln" d="M62 -105 Q140 -150 135 -250"/>'
                 f'<circle class="ln" cx="135" cy="-262" r="16" style="fill:{skin}"/>'),
        "think": ('<path class="ln" d="M-62 -105 Q-100 -10 -92 55"/>'
                  '<path class="ln" d="M62 -105 Q120 -60 40 -150"/>'
                  f'<circle class="ln" cx="40" cy="-155" r="15" style="fill:{skin}"/>'),
        "down": '<path class="ln" d="M-62 -105 Q-100 -10 -92 55"/><path class="ln" d="M62 -105 Q100 -10 92 55"/>',
    }[pose]
    body = (
        # волосы сзади (каре)
        f'<path class="ln" style="fill:{hair}" d="M-122 -135 Q-135 -255 -100 -305 Q0 -385 100 -305 Q135 -255 122 -135 '
        'Q60 -118 0 -128 Q-60 -118 -122 -135 Z"/>'
        # шея, свитер, юбка, ноги, туфли
        '<path class="ln" d="M-14 -140 v26 M14 -140 v26"/>'
        f'<path class="ln" style="fill:{sweater}" d="M-62 -118 Q0 -130 62 -118 L85 60 H-85 Z"/>' + stripes +
        f'<path class="ln" style="fill:{skirt}" d="M-85 60 L-100 135 H100 L85 60 Z"/>'
        '<path class="ln" d="M-40 135 v115 M40 135 v115"/>'
        f'<ellipse class="ln" cx="-52" cy="256" rx="30" ry="13" style="fill:{shoes}"/>'
        f'<ellipse class="ln" cx="52" cy="256" rx="30" ry="13" style="fill:{shoes}"/>'
        # лицо
        f'<ellipse class="ln" cx="0" cy="-222" rx="82" ry="90" style="fill:{skin}"/>'
        '<circle cx="-50" cy="-190" r="13" style="fill:#ff9fb3;opacity:.7"/><circle cx="50" cy="-190" r="13" style="fill:#ff9fb3;opacity:.7"/>'
        '<ellipse cx="-32" cy="-218" rx="14" ry="19" style="fill:#111"/><ellipse cx="32" cy="-218" rx="14" ry="19" style="fill:#111"/>'
        '<circle cx="-27" cy="-225" r="5" style="fill:#fff"/><circle cx="37" cy="-225" r="5" style="fill:#fff"/>'
        + mouth +
        # чёлка и заколка
        f'<path class="ln" style="fill:{hair}" d="M-90 -245 Q-85 -325 0 -326 Q85 -325 90 -245 Q66 -268 44 -252 '
        'Q22 -274 0 -256 Q-22 -274 -44 -252 Q-66 -268 -90 -245 Z"/>'
        '<path class="ln" style="fill:#ffd23f;stroke-width:4" d="M62 -300 l7 -16 l7 16 l17 2 l-13 11 l4 17 l-15 -9 l-15 9 l4 -17 l-13 -11z"/>'
        + arms
    )
    return g(x, y, s, body)


# ---------- зима и ёлка ----------
def xtree(x=500, y=560, s=1.0, star_col="#ffd23f", balls=True, lights=False, face=None, red_star=False):
    import math
    tiers = ('<path class="ln" style="fill:#2e9d5b" d="M0 -300 L-110 -120 H110 Z"/>'
             '<path class="ln" style="fill:#25894f" d="M0 -200 L-160 20 H160 Z"/>'
             '<path class="ln" style="fill:#1f7a45" d="M0 -80 L-210 170 H210 Z"/>'
             '<rect class="ln" x="-30" y="170" width="60" height="70" style="fill:#8a5a3b"/>')
    deco = ""
    if balls:
        cols = ["#e63946", "#ffd23f", "#4fa3f7", "#ff8fb1", "#b79bff", "#f08a00"]
        pts = [(-50, -150), (40, -170), (-90, -20), (10, -40), (90, 0), (-140, 130), (-40, 100), (60, 120), (150, 140)]
        deco += "".join(f'<circle class="ln" cx="{px}" cy="{py}" r="18" style="fill:{cols[i % 6]};stroke-width:5"/>'
                        for i, (px, py) in enumerate(pts))
    if lights:
        deco += '<path class="ln" style="stroke:#7a5a2a;stroke-width:4" d="M-95 -140 Q0 -100 95 -140 M-140 0 Q0 50 140 0 M-185 120 Q0 180 185 120"/>'
        bulbs = [(-60, -126), (0, -118), (60, -126), (-100, 16), (-35, 34), (35, 34), (100, 16),
                 (-140, 142), (-70, 160), (0, 166), (70, 160), (140, 142)]
        bc = ["#ffd23f", "#ff5a6e", "#7fd3ff", "#9cff8f"]
        deco += "".join(f'<circle cx="{bx}" cy="{by}" r="11" style="fill:{bc[i % 4]}"/>' for i, (bx, by) in enumerate(bulbs))
    if face:
        deco += planet(0, -40, 1, "#000")[:0]  # (оставлено для единообразия)
        deco += ('<circle cx="-40" cy="40" r="9" style="fill:#111"/><circle cx="40" cy="40" r="9" style="fill:#111"/>'
                 + {"smile": '<path class="ln" d="M-30 70 q30 26 60 0"/>',
                    "angry": '<path class="ln" d="M-30 85 q30 -22 60 0"/><path class="ln" d="M-60 18 l35 12 M60 18 l-35 12"/>',
                    "o": '<circle class="ln" cx="0" cy="78" r="12"/>'}[face])
    pts = [(0, -360 + 50 * math.sin(i * math.pi / 5 + math.pi / 2) * 0 - 50 * (1 if i % 2 == 0 else 0.45) * math.cos(i * math.pi / 5)) for i in range(10)]
    star = " ".join(f"{(50 if i % 2 == 0 else 22) * math.sin(i * math.pi / 5):.0f},{-360 - (50 if i % 2 == 0 else 22) * math.cos(i * math.pi / 5):.0f}"
                    for i in range(10))
    sc = "#e63946" if red_star else star_col
    return g(x, y, s, tiers + deco + f'<polygon class="ln" points="{star}" style="fill:{sc};stroke-width:5"/>')


def branch(x, y, s=1.0, r=0):
    needles = "".join(f'<path class="ln" style="stroke:#2e9d5b;stroke-width:6" d="M{i * 30} 0 l18 -28 M{i * 30} 0 l18 28"/>' for i in range(8))
    return g(x, y, s, f'<g transform="rotate({r})"><path class="ln" style="stroke:#7a4a2a;stroke-width:9" d="M-10 0 H250"/>{needles}</g>')


def snow(n=26, seed=3, color="#ffffff", area=(40, 40, 960, 960)):
    import random
    rnd = random.Random(seed)
    out = ""
    for _ in range(n):
        x, y, r = rnd.uniform(area[0], area[2]), rnd.uniform(area[1], area[3]), rnd.uniform(5, 13)
        out += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}" style="fill:{color};opacity:.85"/>'
    return out


def mandarin(x, y, s=1.0):
    return g(x, y, s, '<circle class="ln" cx="0" cy="0" r="55" style="fill:#ff9f1c"/>'
                      '<path class="ln" style="fill:#2e9d5b;stroke-width:5" d="M0 -55 q20 -30 45 -20 q-20 25 -45 20z"/>'
                      '<circle cx="-18" cy="-15" r="6" style="fill:#ffd08a"/>')


def bulb(x, y, s=1.0, color="#ffd23f"):
    return g(x, y, s, f'<path class="ln" style="fill:{color}" d="M-45 -10 a45 45 0 1 1 90 0 q0 30 -22 50 h-46 q-22 -20 -22 -50z"/>'
                      '<rect class="ln" x="-24" y="40" width="48" height="36" rx="6" style="fill:#b0b0b0"/>'
                      '<path class="ln" style="stroke:#f08a00;stroke-width:5" d="M-80 -60 l-25 -20 M80 -60 l25 -20 M0 -85 v-30"/>')


def crown(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#ffd23f" d="M-90 0 L-70 -80 L-30 -30 L0 -100 L30 -30 L70 -80 L90 0 Z"/>'
                      '<circle cx="0" cy="-30" r="10" style="fill:#e63946"/>')


def tinsel(x, y, s=1.0):
    strands = "".join(f'<path class="ln" style="stroke:#c9ced6;stroke-width:5" d="M{i * 14 - 100} 0 q{6 if i % 2 else -6} 60 0 {120 + (i % 3) * 20}"/>' for i in range(15))
    return g(x, y, s, '<path class="ln" style="stroke:#9aa1ab;stroke-width:8" d="M-110 0 H110"/>' + strands)


def clock12(x, y, s=1.0):
    return g(x, y, s, '<circle class="ln" cx="0" cy="0" r="90" style="fill:#fff"/>'
                      '<path class="ln" d="M0 0 V-62 M0 0 V-45" style="stroke-width:9"/>'
                      + "".join(f'<circle cx="{75 * __import__("math").sin(i * 0.5236):.0f}" cy="{-75 * __import__("math").cos(i * 0.5236):.0f}" r="5" style="fill:#111"/>' for i in range(12)))


# ---------- заставка без персонажа ----------
def intro_search(query="", bg_blob="#cfe0ff"):
    """Начало каждого ролика: «what did I google today?» + телефон с поисковой строкой."""
    q = (f'<g class="pop"><text class="hand" x="482" y="738" font-size="{min(36, int(560 / max(1, len(query))))}" text-anchor="middle">{query}</text></g>'
         if query else "")
    return (blob(500, 640, 330, bg_blob)
            + hand("what did I", 500, 150, 95) + google_word(500, 290, 170) + hand("today?", 500, 400, 95)
            + '<rect class="ln" x="300" y="470" width="400" height="500" rx="46" style="fill:#fff"/>'
            + '<rect class="ln" x="335" y="690" width="330" height="70" rx="35" style="fill:#f4f6fa;stroke-width:5"/>'
            + '<circle class="ln" cx="640" cy="725" r="15" style="stroke-width:5"/><path class="ln" style="stroke-width:5" d="M651 736 l12 12"/>'
            + google_word(500, 640, 90)
            + '<path class="ln" style="stroke:#c9ced6;stroke-width:6" d="M350 810 h300 M350 850 h240 M350 890 h270"/>'
            + q + star(200, 560, 1.2) + star(820, 520, 0.9, "#ff8fb1") + qmarks(760, 850))


# ---------- техника, деньги, кафе ----------
NV_GREEN = "#76b900"


def mug(x, y, s=1.0, color="#e63946", face="smile", steam=True):
    f = {"smile": '<path class="ln" style="stroke-width:5" d="M-18 10 q18 16 36 0"/>',
         "o": '<circle class="ln" style="stroke-width:5" cx="0" cy="16" r="8"/>',
         "think": '<path class="ln" style="stroke-width:5" d="M-16 16 h32"/>'}[face]
    st = ('<path class="ln" style="stroke:#9aa1ab;stroke-width:5" d="M-20 -70 q-10 -20 0 -40 M10 -70 q-10 -20 0 -40"/>'
          if steam else "")
    return g(x, y, s, f'<path class="ln" style="fill:{color}" d="M-55 -55 h110 l-10 120 h-90 z"/>'
                      '<path class="ln" d="M55 -30 q40 0 35 35 q-5 30 -40 25"/>'
                      '<circle cx="-18" cy="-12" r="6" style="fill:#111"/><circle cx="18" cy="-12" r="6" style="fill:#111"/>'
                      + f + st)


def diner(x=500, y=600, s=1.0):
    return g(x, y, s, '<rect class="ln" x="-330" y="-260" width="660" height="70" rx="30" style="fill:#e63946"/>'
                      '<rect class="ln" x="-330" y="-190" width="90" height="330" style="fill:#e63946"/>'
                      '<rect class="ln" x="240" y="-190" width="90" height="330" style="fill:#e63946"/>'
                      '<rect class="ln" x="-230" y="20" width="460" height="40" style="fill:#f4e3c1"/>'
                      '<path class="ln" d="M0 60 v130 M-60 190 h120"/>')


def chip(x, y, s=1.0, label="", color=NV_GREEN, mark=None):
    pins = "".join(f'<path class="ln" style="stroke-width:6" d="M{-75 + i * 30} -100 v-28 M{-75 + i * 30} 100 v28 '
                   f'M-100 {-75 + i * 30} h-28 M100 {-75 + i * 30} h28"/>' for i in range(6))
    lab = (f'<text class="hand" x="0" y="22" font-size="{70 if len(label) < 5 else 46}" text-anchor="middle" '
           f'style="fill:#fff">{label}</text>' if label else "")
    m = ""
    if mark is True:
        m = '<path class="ln" style="stroke:#1f9d55;stroke-width:18" d="M60 120 L100 165 L190 60"/>'
    elif mark is False:
        m = '<path class="ln" style="stroke:#d7263d;stroke-width:18" d="M-150 -150 L150 150 M150 -150 L-150 150"/>'
    return g(x, y, s, pins + f'<rect class="ln" x="-100" y="-100" width="200" height="200" rx="18" style="fill:#2b2d33"/>'
                             f'<rect x="-70" y="-70" width="140" height="140" rx="10" style="fill:{color}"/>' + lab + m)


def moneybag(x, y, s=1.0, text="$"):
    return g(x, y, s, '<path class="ln" style="fill:#c9a659" d="M-40 -110 h80 l-20 30 q110 60 90 150 q-10 50 -110 50 '
                      'q-100 0 -110 -50 q-20 -90 90 -150z"/>'
                      '<path class="ln" style="stroke:#8a6d2b;stroke-width:8" d="M-30 -80 h60"/>'
                      f'<text class="hand" x="0" y="60" font-size="110" text-anchor="middle" style="fill:#fff">{text}</text>')


def screen_cube(x, y, s=1.0):
    return g(x, y, s, '<rect class="ln" x="-200" y="-140" width="400" height="260" rx="16" style="fill:#2b2d33"/>'
                      '<path class="ln" d="M-40 160 h80 M0 120 v40"/>'
                      '<path class="ln" style="fill:#4fa3f7;stroke:#fff;stroke-width:5" d="M0 -90 l70 35 l-70 35 l-70 -35z"/>'
                      '<path class="ln" style="fill:#2f6fdb;stroke:#fff;stroke-width:5" d="M-70 -55 v70 l70 35 v-70z"/>'
                      '<path class="ln" style="fill:#7fb0ff;stroke:#fff;stroke-width:5" d="M70 -55 v70 l-70 35 v-70z"/>')


def plates(x, y, s=1.0):
    return g(x, y, s, "".join(f'<ellipse class="ln" cx="0" cy="{-i * 28}" rx="120" ry="28" style="fill:#fff"/>' for i in range(5))
             + "".join(f'<circle class="ln" cx="{cx}" cy="{cy}" r="{r}" style="fill:#cfe8ff;stroke-width:4"/>'
                       for cx, cy, r in [(-110, -170, 22), (-60, -210, 14), (90, -190, 26), (130, -240, 12)]))


def brain(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#ff9fb3" d="M-120 20 q-40 -80 30 -120 q20 -60 90 -40 q70 -40 110 20 '
                      'q70 20 40 100 q20 70 -60 80 q-40 40 -100 10 q-80 20 -110 -50z"/>'
                      '<path class="ln" style="stroke-width:5" d="M0 -130 q-20 60 10 150 M-70 -60 q40 10 50 50 M70 -40 q-40 20 -40 60"/>')


def chart_up(x, y, s=1.0, color=NV_GREEN):
    return g(x, y, s, '<path class="ln" d="M-200 150 H220 M-200 150 V-170"/>'
                      f'<path class="ln" style="stroke:{color};stroke-width:16" d="M-180 120 L-90 70 L-20 95 L60 -10 L120 10 L200 -150"/>'
                      f'<path class="ln" style="fill:{color};stroke:{color}" d="M200 -150 l-50 10 l35 40z"/>')


# ---------- кубики и прочее ----------
def cube(x, y, a=80, top="#6cc24a", left="#8b5a2b", right="#6e4520"):
    h = a * 0.5
    return (f'<path class="ln" style="fill:{top};stroke-width:5" d="M{x} {y - h} l{a} {h} l{-a} {h} l{-a} {-h}z"/>'
            f'<path class="ln" style="fill:{left};stroke-width:5" d="M{x - a} {y} l{a} {h} v{a} l{-a} {-h}z"/>'
            f'<path class="ln" style="fill:{right};stroke-width:5" d="M{x + a} {y} l{-a} {h} v{a} l{a} {-h}z"/>')


def pickaxe(x, y, s=1.0, r=-30):
    return g(x, y, s, f'<g transform="rotate({r})"><path class="ln" style="stroke:#8a5a3b;stroke-width:22" d="M0 -10 V220"/>'
                      '<path class="ln" style="fill:#9fd8e8" d="M-150 30 Q0 -90 150 30 Q0 -40 -150 30z"/></g>')


def pig(x, y, s=1.0, tall=False):
    sx, sy = (0.6, 1.9) if tall else (1, 1)
    body = (f'<g transform="scale({sx},{sy})">'
            '<rect class="ln" x="-120" y="-70" width="240" height="140" rx="40" style="fill:#ffb3c7"/>'
            '<path class="ln" d="M-80 70 v50 M-30 70 v50 M30 70 v50 M80 70 v50" style="stroke-width:12"/></g>')
    hx = 0 if tall else 140
    hy = -150 if tall else -40
    head = (f'<circle class="ln" cx="{hx}" cy="{hy}" r="60" style="fill:#ffb3c7"/>'
            f'<ellipse class="ln" cx="{hx}" cy="{hy + 15}" rx="26" ry="18" style="fill:#ff8fb1;stroke-width:5"/>'
            f'<circle cx="{hx - 8}" cy="{hy + 15}" r="4" style="fill:#111"/><circle cx="{hx + 8}" cy="{hy + 15}" r="4" style="fill:#111"/>'
            f'<circle cx="{hx - 22}" cy="{hy - 18}" r="7" style="fill:#111"/><circle cx="{hx + 22}" cy="{hy - 18}" r="7" style="fill:#111"/>')
    return g(x, y, s, body + head)


def cat_sleep(x, y, s=1.0, color="#f3a95e"):
    return g(x, y, s, f'<path class="ln" style="fill:{color}" d="M-170 60 q0 -130 150 -130 q150 0 150 130 z"/>'
                      f'<circle class="ln" cx="130" cy="10" r="65" style="fill:{color}"/>'
                      f'<path class="ln" style="fill:{color}" d="M85 -35 l10 -50 l35 35z M175 -35 l-10 -50 l-35 35z"/>'
                      '<path class="ln" style="stroke-width:5" d="M100 5 q12 10 22 0 M140 5 q12 10 22 0"/>'
                      f'<path class="ln" style="stroke:{color};stroke-width:22" d="M-170 50 q-60 -10 -40 -80"/>'
                      '<text class="hand" x="230" y="-80" font-size="70">z</text><text class="hand" x="270" y="-140" font-size="90">Z</text>')


def mic(x, y, s=1.0):
    return g(x, y, s, '<rect class="ln" x="-40" y="-120" width="80" height="130" rx="40" style="fill:#9aa1ab"/>'
                      '<path class="ln" d="M-65 -20 q0 80 65 80 q65 0 65 -80 M0 60 v60 M-50 120 h100"/>')


def earth(x, y, r=90):
    return (f'<circle class="ln" cx="{x}" cy="{y}" r="{r}" style="fill:#4fa3f7"/>'
            f'<path class="ln" style="fill:#5cc06a;stroke-width:5" d="M{x - r * 0.6} {y - r * 0.3} q{r * 0.3} {-r * 0.5} {r * 0.6} {-r * 0.2} '
            f'q{r * 0.2} {r * 0.4} {-r * 0.1} {r * 0.6} q{-r * 0.4} {r * 0.1} {-r * 0.5} {-r * 0.4}z"/>'
            f'<path class="ln" style="fill:#5cc06a;stroke-width:5" d="M{x + r * 0.2} {y + r * 0.2} q{r * 0.4} {-r * 0.2} {r * 0.5} {r * 0.2} '
            f'q{-r * 0.1} {r * 0.4} {-r * 0.4} {r * 0.3}z"/>')


def bubble(x, y, w=520, h=200, color="#fff", text="", size=80, cls="hand"):
    return (f'<path class="ln" style="fill:{color}" d="M{x - w / 2} {y - h / 2} h{w} v{h} h{-w * 0.55} l-60 70 l10 -70 h{-w * 0.45 + 50} z"/>'
            + hand(text, x, y + size * 0.3, size, cls))


# ---------- микромир ----------
def bacterium(x, y, s=1.0, color="#7ed957", r=0, face="smile"):
    f = {"smile": '<circle cx="-18" cy="-6" r="6" style="fill:#111"/><circle cx="18" cy="-6" r="6" style="fill:#111"/>'
                  '<path class="ln" style="stroke-width:5" d="M-14 12 q14 12 28 0"/>',
         "o": '<circle cx="-18" cy="-6" r="6" style="fill:#111"/><circle cx="18" cy="-6" r="6" style="fill:#111"/>'
              '<circle class="ln" style="stroke-width:5" cx="0" cy="16" r="7"/>',
         None: ""}[face]
    return g(x, y, s, f'<g transform="rotate({r})">'
                      f'<path class="ln" style="stroke-width:5" d="M90 0 q30 -20 50 0 q20 20 45 0"/>'
                      f'<rect class="ln" x="-95" y="-48" width="190" height="96" rx="48" style="fill:{color}"/>'
                      f'<circle cx="-50" cy="20" r="8" style="fill:#ffffff;opacity:.5"/><circle cx="45" cy="-22" r="6" style="fill:#ffffff;opacity:.5"/>'
                      f'</g>{f}')


def virus(x, y, r=70, color="#e0457b", face=None):
    import math
    spikes = "".join(f'<path class="ln" style="stroke-width:6" d="M{x + r * math.cos(a):.0f} {y + r * math.sin(a):.0f} '
                     f'L{x + (r + 28) * math.cos(a):.0f} {y + (r + 28) * math.sin(a):.0f}"/>'
                     f'<circle class="ln" style="fill:{color};stroke-width:5" cx="{x + (r + 34) * math.cos(a):.0f}" cy="{y + (r + 34) * math.sin(a):.0f}" r="10"/>'
                     for a in [i * math.pi / 6 for i in range(12)])
    f = ""
    if face:
        f = (f'<circle cx="{x - r * 0.3}" cy="{y - r * 0.1}" r="{r * 0.09}" style="fill:#111"/><circle cx="{x + r * 0.3}" cy="{y - r * 0.1}" r="{r * 0.09}" style="fill:#111"/>'
             + (f'<path class="ln" style="stroke-width:5" d="M{x - r * 0.3} {y + r * 0.3} l{r * 0.15} {-r * 0.12} l{r * 0.15} {r * 0.12} l{r * 0.15} {-r * 0.12} l{r * 0.15} {r * 0.12}"/>'
                if face == "evil" else f'<path class="ln" style="stroke-width:5" d="M{x - r * 0.25} {y + r * 0.25} q{r * 0.25} {r * 0.25} {r * 0.5} 0"/>'))
    return spikes + f'<circle class="ln" cx="{x}" cy="{y}" r="{r}" style="fill:{color}"/>' + f


def phage(x, y, s=1.0, color="#7b3fe4"):
    return g(x, y, s, f'<path class="ln" style="fill:{color}" d="M0 -150 l55 32 v64 l-55 32 l-55 -32 v-64z"/>'
                      '<rect class="ln" x="-14" y="-22" width="28" height="120" style="fill:#c9ced6"/>'
                      '<path class="ln" style="stroke-width:6" d="M-14 98 l-60 50 l-20 50 M14 98 l60 50 l20 50 M-6 98 l-25 70 M6 98 l25 70"/>'
                      '<circle cx="-18" cy="-90" r="7" style="fill:#fff"/><circle cx="18" cy="-90" r="7" style="fill:#fff"/>'
                      '<circle cx="-18" cy="-90" r="3.5" style="fill:#111"/><circle cx="18" cy="-90" r="3.5" style="fill:#111"/>')


def dna(x, y, s=1.0, a="#4fa3f7", b="#ff8fb1", hl=()):
    import math
    out = ""
    for i in range(14):
        yy = -260 + i * 40
        dx = 90 * math.sin(i * 0.55)
        col = "#ffd23f" if i in hl else "#c9ced6"
        out += f'<path class="ln" style="stroke:{col};stroke-width:10" d="M{-dx:.0f} {yy} L{dx:.0f} {yy}"/>'
    p1 = " ".join(f"{90 * math.sin(i * 0.55):.0f},{-260 + i * 40}" for i in range(14))
    p2 = " ".join(f"{-90 * math.sin(i * 0.55):.0f},{-260 + i * 40}" for i in range(14))
    out += f'<polyline class="ln" points="{p1}" style="stroke:{a};stroke-width:14"/><polyline class="ln" points="{p2}" style="stroke:{b};stroke-width:14"/>'
    return g(x, y, s, out)


def petri(x, y, s=1.0):
    return g(x, y, s, '<ellipse class="ln" cx="0" cy="0" rx="230" ry="90" style="fill:#f3f7ea"/>'
                      '<path class="ln" style="fill:#c7e6a3;stroke-width:5" d="M-60 -20 q30 -40 70 -10 q40 10 20 40 q-40 30 -80 10 q-30 -15 -10 -40z"/>'
                      '<circle cx="-120" cy="10" r="14" style="fill:#e8d27a"/><circle cx="110" cy="-20" r="10" style="fill:#e8d27a"/>'
                      '<circle cx="130" cy="30" r="8" style="fill:#e8d27a"/>'
                      '<ellipse class="ln" cx="0" cy="25" rx="230" ry="90" style="stroke-width:5"/>')


def balance(x, y, s=1.0, left="", right=""):
    return g(x, y, s, '<path class="ln" d="M0 -150 V150 M-120 150 h240 M-260 -120 H260" style="stroke-width:10"/>'
                      '<path class="ln" d="M-220 -120 l-60 120 h120 z M220 -120 l-60 120 h120 z" style="fill:#fff;stroke-width:6"/>'
                      + left + right)


# ---------- свет и электричество ----------
def skyline(x=500, y=700, s=1.0, lit=True, seed=1):
    import random
    rnd = random.Random(seed)
    out, bx = "", -420
    for w, h in [(140, 360), (110, 250), (160, 470), (120, 300), (150, 410), (110, 230), (130, 340)]:
        out += f'<rect class="ln" x="{bx}" y="{-h}" width="{w}" height="{h}" style="fill:#2b2f45;stroke-width:5"/>'
        for wy in range(-h + 30, -30, 55):
            for wx in range(bx + 20, bx + w - 30, 40):
                on = lit and rnd.random() > 0.25
                out += f'<rect x="{wx}" y="{wy}" width="20" height="28" style="fill:{"#ffd23f" if on else "#3b4060"}"/>'
        bx += w
    return g(x, y, s, out)


def curtains(x=500, y=560, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#c0283d" d="M-380 -380 h340 q-60 200 -20 760 h-320z"/>'
                      '<path class="ln" style="fill:#c0283d" d="M380 -380 h-340 q60 200 20 760 h320z"/>'
                      '<rect class="ln" x="-400" y="-420" width="800" height="60" style="fill:#8a1c2c"/>'
                      '<rect class="ln" x="-400" y="380" width="800" height="40" style="fill:#5a3a2a"/>')


def powerline(x=500, y=600, s=1.0, tree=False, spark=False):
    out = ('<path class="ln" style="stroke-width:10" d="M-300 300 L-260 -250 L-220 300 M-330 -200 h140 M-300 -130 h80"/>'
           '<path class="ln" style="stroke-width:10" d="M300 300 L260 -250 L220 300 M330 -200 h-140 M300 -130 h-80"/>'
           '<path class="ln" style="stroke-width:5" d="M-320 -200 Q0 -120 320 -200 M-180 -200 Q0 -110 180 -200"/>')
    if tree:
        out += ('<rect class="ln" x="-20" y="0" width="40" height="300" style="fill:#8a5a3b"/>'
                '<circle class="ln" cx="0" cy="-60" r="110" style="fill:#2e9d5b"/><circle class="ln" cx="-60" cy="-20" r="70" style="fill:#25894f"/>')
    if spark:
        out += '<path class="ln" style="fill:#ffd23f;stroke:#f08a00" d="M0 -190 l25 45 l-15 0 l25 45 l-55 -55 l20 0 z"/>'
    return g(x, y, s, out)


def wave(x=500, y=500, s=1.0, color="#4fa3f7", bad=False):
    import math
    pts = " ".join(f"{-300 + i * 10},{(math.sin(i * 0.35) * (40 + (i * 2.2 if bad else 0))):.0f}" for i in range(61))
    return g(x, y, s, f'<polyline class="ln" points="{pts}" style="stroke:{color};stroke-width:10"/>')


def flashlight(x, y, s=1.0, r=-20):
    return g(x, y, s, f'<g transform="rotate({r})"><rect class="ln" x="-40" y="-20" width="80" height="200" rx="14" style="fill:#4fa3f7"/>'
                      '<path class="ln" style="fill:#c9ced6" d="M-60 -90 h120 l-20 70 h-80z"/>'
                      '<path style="fill:#ffe98a;opacity:.7" d="M-55 -95 L-200 -380 H200 L55 -95z"/></g>')


def powerbank(x, y, s=1.0):
    return g(x, y, s, '<rect class="ln" x="-70" y="-120" width="140" height="240" rx="22" style="fill:#2b2d33"/>'
                      '<rect x="-40" y="60" width="80" height="20" rx="6" style="fill:#1f9d55"/>'
                      '<path class="ln" style="fill:#ffd23f;stroke:#ffd23f" d="M5 -70 l-35 60 h28 l-10 50 l40 -65 h-28 z"/>')


def bottle(x, y, s=1.0):
    return g(x, y, s, '<rect class="ln" x="-22" y="-150" width="44" height="40" rx="6" style="fill:#4fa3f7"/>'
                      '<path class="ln" style="fill:#d9efff" d="M-22 -110 q-40 30 -40 80 v170 q0 20 20 20 h84 q20 0 20 -20 v-170 q0 -50 -40 -80z"/>'
                      '<path style="fill:#9cd2ff" d="M-58 20 h116 v120 q0 18 -18 18 h-80 q-18 0 -18 -18z"/>')


def candle_x(x, y, s=1.0):
    return candle(x, y, s) + check(x, y + 20 * s, 2.0 * s, ok=False)


# ---------- Рождество (рисованные) ----------
def cal_page(x, y, s=1.0, month="DEC", day="25", color="#e63946"):
    return g(x, y, s, f'<rect class="ln" x="-150" y="-170" width="300" height="320" rx="24" style="fill:#fff"/>'
                      f'<path class="ln" style="fill:{color}" d="M-150 -100 v-46 q0 -24 24 -24 h252 q24 0 24 24 v46z"/>'
                      '<path class="ln" d="M-80 -195 v50 M80 -195 v50"/>') + \
        hand(month, x, y - 118 * s, 60 * s, "hand") .replace('class="hand"', 'class="hand" style="fill:#fff"') + \
        hand(day, x, y + 90 * s, 190 * s, "hand")


def open_book(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#fff6e0" d="M0 -110 q-110 -40 -220 0 v250 q110 -40 220 0z"/>'
                      '<path class="ln" style="fill:#fff6e0" d="M0 -110 q110 -40 220 0 v250 q-110 -40 -220 0z"/>'
                      '<path class="ln" style="stroke:#c9b48a;stroke-width:5" d="M-180 -60 q80 -25 150 0 M-180 -10 q80 -25 150 0 M30 -60 q80 -25 150 0 M30 -10 q80 -25 150 0"/>')


def santa_hat(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#e63946" d="M-150 60 Q-60 -200 120 -150 Q60 -100 90 60 Z"/>'
                      '<rect class="ln" x="-180" y="40" width="300" height="70" rx="35" style="fill:#fff"/>'
                      '<circle class="ln" cx="135" cy="-150" r="34" style="fill:#fff"/>')


def soda(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#c0283d" d="M-25 -200 h50 v60 q45 40 45 100 q-20 50 0 100 q0 70 -20 130 h-100 q-20 -60 -20 -130 q20 -50 0 -100 q0 -60 45 -100z"/>'
                      '<rect class="ln" x="-28" y="-225" width="56" height="28" rx="6" style="fill:#d9d9d9"/>'
                      '<path class="ln" style="stroke:#fff;stroke-width:8" d="M-55 0 q55 -25 110 0"/>')


def rocket(x, y, s=1.0, r=-30):
    return g(x, y, s, f'<g transform="rotate({r})">'
                      '<path class="ln" style="fill:#ffb347" d="M-40 50 q40 170 80 0z"/>'
                      '<path class="ln" style="fill:#e63946" d="M-60 0 l-60 90 l60 -20z M60 0 l60 90 l-60 -20z"/>'
                      '<path class="ln" style="fill:#fff" d="M0 -220 q80 90 60 260 h-120 q-20 -170 60 -260z"/>'
                      '<circle class="ln" cx="0" cy="-60" r="34" style="fill:#7fd3ff"/></g>')


def jingle_bell(x, y, s=1.0, color="#ffd23f"):
    return g(x, y, s, f'<path class="ln" style="fill:{color}" d="M-110 80 q20 -20 25 -110 q5 -90 85 -100 q80 10 85 100 q5 90 25 110z"/>'
                      '<circle class="ln" cx="0" cy="105" r="24" style="fill:#f08a00"/>'
                      '<path class="ln" style="fill:#2e9d5b;stroke-width:5" d="M0 -130 q-50 -40 -80 -10 q40 20 80 10 q50 -40 80 -10 q-40 20 -80 10z"/>')


def note(x, y, s=1.0, color="#7b3fe4"):
    return g(x, y, s, f'<path class="ln" style="stroke:{color};stroke-width:10" d="M-40 60 v-170 l120 -30 v170"/>'
                      f'<ellipse class="ln" cx="-65" cy="62" rx="30" ry="24" style="fill:{color}"/><ellipse class="ln" cx="55" cy="32" rx="30" ry="24" style="fill:{color}"/>')


# ---------- смешные подарки ----------
def gift(x, y, s=1.0, box="#e63946", ribbon="#ffd23f"):
    return g(x, y, s, f'<rect class="ln" x="-110" y="-60" width="220" height="170" style="fill:{box}"/>'
                      f'<rect class="ln" x="-125" y="-100" width="250" height="50" style="fill:{box}"/>'
                      f'<path class="ln" style="stroke:{ribbon};stroke-width:20" d="M0 -100 V110"/>'
                      f'<path class="ln" style="fill:{ribbon}" d="M0 -100 q-70 -70 -90 -20 q20 30 90 20 q70 -70 90 -20 q-20 30 -90 20z"/>')


def sock(x, y, s=1.0, color="#4fa3f7", r=0, face=True):
    f = ('<circle class="ln" cx="0" cy="-60" r="48" style="fill:#c98b5a"/>'
         '<path class="ln" style="fill:#8a5a3b" d="M-46 -82 q-30 -10 -24 40 q16 -10 22 -24z M46 -82 q30 -10 24 40 q-16 -10 -22 -24z"/>'
         '<circle cx="-16" cy="-66" r="6" style="fill:#111"/><circle cx="16" cy="-66" r="6" style="fill:#111"/>'
         '<ellipse cx="0" cy="-48" rx="10" ry="7" style="fill:#111"/><path class="ln" style="stroke-width:4" d="M-12 -34 q12 10 24 0"/>') if face else ""
    return g(x, y, s, f'<g transform="rotate({r})"><path class="ln" style="fill:{color}" d="M-60 -180 h120 v200 q0 40 40 50 q60 15 50 70 q-10 50 -80 40 '
                      'q-90 -10 -120 -60 q-10 -20 -10 -60z"/>'
                      '<rect class="ln" x="-60" y="-200" width="120" height="40" style="fill:#fff"/>' + f + '</g>')


def gummy(x, y, s=1.0, color="#ff5a6e"):
    return g(x, y, s, f'<g style="opacity:.92">'
                      f'<circle class="ln" cx="-45" cy="-150" r="28" style="fill:{color}"/><circle class="ln" cx="45" cy="-150" r="28" style="fill:{color}"/>'
                      f'<circle class="ln" cx="0" cy="-100" r="70" style="fill:{color}"/>'
                      f'<ellipse class="ln" cx="0" cy="40" rx="90" ry="110" style="fill:{color}"/>'
                      f'<ellipse class="ln" cx="-95" cy="0" rx="30" ry="45" style="fill:{color}"/><ellipse class="ln" cx="95" cy="0" rx="30" ry="45" style="fill:{color}"/>'
                      f'<ellipse class="ln" cx="-55" cy="140" rx="38" ry="30" style="fill:{color}"/><ellipse class="ln" cx="55" cy="140" rx="38" ry="30" style="fill:{color}"/>'
                      '<circle cx="-25" cy="-110" r="7" style="fill:#111"/><circle cx="25" cy="-110" r="7" style="fill:#111"/>'
                      '<path class="ln" style="stroke-width:5" d="M-14 -80 q14 12 28 0"/>'
                      '<ellipse cx="-40" cy="10" rx="18" ry="30" style="fill:#fff;opacity:.4"/></g>')


def coal(x, y, s=1.0, wrapper=True):
    w = ('<path class="ln" style="fill:#ff8fb1" d="M-140 0 l-60 -50 v100z M140 0 l60 -50 v100z"/>' if wrapper else "")
    return g(x, y, s, w + '<path class="ln" style="fill:#2b2b30" d="M-140 -10 l40 -70 l90 -20 l80 30 l60 60 l-20 70 l-90 30 l-110 -20 z"/>'
                          '<path class="ln" style="stroke:#55555e;stroke-width:5" d="M-60 -50 l40 30 M30 -40 l30 50 M-90 30 l50 -10"/>')


def toilet(x, y, s=1.0):
    return g(x, y, s, '<rect class="ln" x="60" y="-260" width="110" height="170" rx="16" style="fill:#fff"/>'
                      '<path class="ln" style="fill:#fff" d="M-170 -90 h340 q0 120 -120 150 v90 h-100 v-90 q-120 -30 -120 -150z"/>'
                      '<ellipse class="ln" cx="0" cy="-90" rx="170" ry="40" style="fill:#e9f2ff"/>')


def golf_set(x, y, s=1.0):
    return g(x, y, s, '<ellipse class="ln" cx="0" cy="40" rx="220" ry="50" style="fill:#5cc06a"/>'
                      '<ellipse cx="90" cy="40" rx="24" ry="9" style="fill:#2b2b30"/>'
                      '<path class="ln" style="stroke-width:6" d="M90 40 V-120"/><path class="ln" style="fill:#e63946" d="M90 -120 l70 25 l-70 25z"/>'
                      '<circle class="ln" cx="-60" cy="25" r="14" style="fill:#fff;stroke-width:4"/>'
                      '<path class="ln" style="stroke:#9aa1ab;stroke-width:9" d="M-200 -180 L-90 10"/><path class="ln" style="fill:#9aa1ab" d="M-100 0 h50 v22 h-60z"/>')


def pet_rock(x, y, s=1.0, box=True):
    b = ('<path class="ln" style="fill:#e8c48f" d="M-200 30 h400 v150 h-400z"/>'
         '<path class="ln" style="fill:#f4dcb0" d="M-200 30 l40 -60 h320 l40 60z"/>' if box else "")
    return g(x, y, s, b + '<path class="ln" style="fill:#a9a39a" d="M-140 40 q-20 -110 70 -140 q110 -30 170 40 q50 70 -20 110 q-110 30 -220 -10z"/>'
                          '<circle class="ln" cx="-30" cy="-40" r="28" style="fill:#fff;stroke-width:5"/><circle cx="-24" cy="-34" r="12" style="fill:#111"/>'
                          '<circle class="ln" cx="45" cy="-45" r="28" style="fill:#fff;stroke-width:5"/><circle cx="51" cy="-39" r="12" style="fill:#111"/>'
                          '<path class="ln" style="stroke-width:5" d="M-10 10 q20 14 40 0"/>')


def cat(x, y, s=1.0, color="#f3a95e"):
    return g(x, y, s, f'<ellipse class="ln" cx="0" cy="60" rx="90" ry="110" style="fill:{color}"/>'
                      f'<circle class="ln" cx="0" cy="-90" r="70" style="fill:{color}"/>'
                      f'<path class="ln" style="fill:{color}" d="M-60 -125 l5 -70 l45 45z M60 -125 l-5 -70 l-45 45z"/>'
                      '<circle cx="-24" cy="-95" r="8" style="fill:#111"/><circle cx="24" cy="-95" r="8" style="fill:#111"/>'
                      '<path class="ln" style="stroke-width:5" d="M-12 -70 q12 10 24 0 M-80 -80 h40 M40 -80 h40"/>'
                      f'<path class="ln" style="stroke:{color};stroke-width:22" d="M80 130 q90 -20 60 -110"/>')


# ---------- сон ----------
def bed(x, y, s=1.0, color="#4fa3f7"):
    return g(x, y, s, '<path class="ln" style="stroke-width:10" d="M-260 -120 V120 M260 -20 V120"/>'
                      f'<rect class="ln" x="-260" y="-20" width="520" height="90" rx="14" style="fill:{color}"/>'
                      '<rect class="ln" x="-240" y="-70" width="150" height="60" rx="26" style="fill:#fff"/>'
                      f'<path class="ln" style="fill:{color}" d="M-80 -20 q160 -60 340 0 v30 h-340z"/>')


def moon(x, y, r=80, color="#ffd23f"):
    return f'<path class="ln" style="fill:{color}" d="M{x} {y - r} a{r} {r} 0 1 0 {r * 0.9} {r * 1.45} a{r * 0.8} {r * 0.8} 0 1 1 {-r * 0.9} {-r * 1.45}z"/>'


def zzz(x, y, s=1.0, cls="hand blue"):
    return (hand("z", x, y, 70 * s, cls, -10) + hand("z", x + 45 * s, y - 55 * s, 95 * s, cls, -10)
            + hand("Z", x + 105 * s, y - 130 * s, 125 * s, cls, -10))


def tired_eye(x, y, s=1.0, open_=0.3):
    h = 60 * open_
    return g(x, y, s, f'<path class="ln" style="fill:#fff" d="M-120 0 q120 {-2 * h - 10} 240 0 q-120 {2 * h + 10} -240 0z"/>'
                      f'<circle cx="0" cy="0" r="{max(8, h * 0.9)}" style="fill:#4fa3f7"/><circle cx="0" cy="0" r="{max(4, h * 0.45)}" style="fill:#111"/>'
                      '<path class="ln" style="fill:#c9b8e8" d="M-125 0 q125 -95 250 0 q-125 -40 -250 0z"/>'
                      '<path class="ln" style="stroke:#e0457b;stroke-width:4" d="M-90 35 q15 -10 25 -2 M70 30 q15 -8 22 4"/>')


def glass(x, y, s=1.0, fill="#ffb347"):
    return g(x, y, s, f'<path style="fill:{fill};opacity:.85" d="M-62 -40 h124 l-14 150 h-96z"/>'
                      '<path class="ln" d="M-75 -120 h150 l-20 240 h-110z"/>'
                      '<path class="ln" style="fill:#fff;stroke-width:5" d="M-62 -40 q30 -25 62 0 q30 -25 62 0"/>')


def car(x, y, s=1.0, color="#e63946"):
    return g(x, y, s, f'<path class="ln" style="fill:{color}" d="M-220 40 v-60 q0 -20 20 -25 l60 -10 l50 -70 h170 l60 70 l60 10 q20 5 20 25 v60z"/>'
                      '<path class="ln" style="fill:#cfe8ff" d="M-80 -60 l40 -55 h70 v55z M50 -60 v-55 h50 l45 55z"/>'
                      '<circle class="ln" cx="-130" cy="45" r="42" style="fill:#333"/><circle class="ln" cx="140" cy="45" r="42" style="fill:#333"/>')


def mouse(x, y, s=1.0, color="#c9c2b8", face="o"):
    eyes = ('<path class="ln" style="stroke-width:5" d="M60 -40 q8 6 16 0"/>' if face == "sleep"
            else '<circle cx="68" cy="-40" r="7" style="fill:#111"/>')
    return g(x, y, s, f'<path class="ln" style="stroke:{color};stroke-width:9" d="M-110 20 q-80 10 -90 -60"/>'
                      f'<ellipse class="ln" cx="-10" cy="0" rx="110" ry="65" style="fill:{color}"/>'
                      f'<path class="ln" style="fill:{color}" d="M60 -60 q60 20 60 60 q-40 20 -70 0z"/>'
                      f'<circle class="ln" cx="40" cy="-70" r="32" style="fill:#ffb3c7"/>' + eyes
                      + '<circle cx="118" cy="0" r="8" style="fill:#e0457b"/>')


def drops(x, y, s=1.0, n=7, color="#4fa3f7"):
    import random
    r = random.Random(3)
    return "".join(g(x + r.uniform(-200, 200) * s, y + r.uniform(-150, 150) * s, 0.5 * s,
                     f'<path class="ln" style="fill:{color};stroke-width:5" d="M0 -40 q35 45 0 70 q-35 -25 0 -70z"/>') for _ in range(n))


# ---------- история подарков ----------
def fireplace(x, y, s=1.0):
    return g(x, y, s, '<rect class="ln" x="-300" y="-260" width="600" height="60" rx="10" style="fill:#b5653a"/>'
                      '<rect class="ln" x="-260" y="-200" width="520" height="330" style="fill:#c97b4a"/>'
                      '<path class="ln" style="fill:#2b2230" d="M-150 130 v-170 q150 -110 300 0 v170z"/>'
                      '<path class="ln" style="fill:#ff8c2b" d="M-70 130 q-20 -80 30 -120 q0 50 30 60 q10 -60 50 -90 q40 70 20 150z"/>'
                      '<path class="ln" style="fill:#ffd23f;stroke-width:4" d="M-30 130 q-5 -40 20 -60 q20 30 30 60z"/>'
                      '<path class="ln" style="stroke:#8a4a2a;stroke-width:4" d="M-260 -120 h520 M-260 -40 h110 M150 -40 h110 M-260 40 h110 M150 40 h110"/>')


def coin(x, y, s=1.0):
    return g(x, y, s, '<circle class="ln" cx="0" cy="0" r="38" style="fill:#ffd23f"/><circle class="ln" cx="0" cy="0" r="24" style="stroke:#e0a800;stroke-width:4"/>')


def gold_bag(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#c9a659" d="M-40 -110 h80 l-20 30 q110 60 90 150 q-10 50 -110 50 q-100 0 -110 -50 q-20 -90 90 -150z"/>'
                      '<path class="ln" style="stroke:#8a6d2b;stroke-width:8" d="M-30 -80 h60"/>') + coin(x + 70 * s, y + 110 * s, 0.7 * s) + coin(x - 80 * s, y + 120 * s, 0.6 * s)


def figurine(x, y, s=1.0, color="#c98b5a"):
    return g(x, y, s, f'<circle class="ln" cx="0" cy="-90" r="34" style="fill:{color}"/>'
                      f'<path class="ln" style="fill:{color}" d="M-45 -50 h90 l25 150 h-140z"/>'
                      '<circle cx="-12" cy="-94" r="5" style="fill:#111"/><circle cx="12" cy="-94" r="5" style="fill:#111"/>')


def scroll(x, y, s=1.0, lines=5):
    ls = "".join(f'<path class="ln" style="stroke:#9a8a6a;stroke-width:5" d="M-140 {-120 + i * 55} h{280 - (i % 2) * 70}"/>' for i in range(lines))
    return g(x, y, s, '<rect class="ln" x="-180" y="-200" width="360" height="400" style="fill:#fff4d6"/>'
                      '<rect class="ln" x="-200" y="-230" width="400" height="50" rx="25" style="fill:#e8d2a8"/>'
                      '<rect class="ln" x="-200" y="180" width="400" height="50" rx="25" style="fill:#e8d2a8"/>' + ls)


def paper_roll(x, y, s=1.0, color="#e63946", dots="#ffd23f"):
    pat = "".join(f'<circle cx="{-120 + (i % 6) * 48}" cy="{-50 + (i // 6) * 50}" r="9" style="fill:{dots}"/>' for i in range(18))
    return g(x, y, s, f'<rect class="ln" x="-160" y="-90" width="320" height="180" style="fill:{color}"/>' + pat
                      + f'<ellipse class="ln" cx="-160" cy="0" rx="40" ry="90" style="fill:{color}"/>'
                      '<ellipse class="ln" cx="-160" cy="0" rx="14" ry="34" style="fill:#fff"/>'
                      f'<path class="ln" style="fill:{color}" d="M160 -90 l180 40 v180 l-180 -40z"/>')


def heart(x, y, s=1.0, color="#e0457b"):
    return g(x, y, s, f'<path class="ln" style="fill:{color}" d="M0 80 C-160 -20 -110 -150 0 -80 C110 -150 160 -20 0 80z"/>')


# ---------- мозг и навыки ----------
def neuron(x, y, s=1.0, myelin=0, color="#ff9fb3", sheath="#ffd23f"):
    """нейрон: тело с дендритами и длинный аксон; myelin — сколько сегментов оболочки (0..6)"""
    import math
    den = "".join(f'<path class="ln" style="stroke-width:7" d="M{-300 + 60 * math.cos(a):.0f} {60 * math.sin(a):.0f} '
                  f'q{70 * math.cos(a + .4):.0f} {70 * math.sin(a + .4):.0f} {130 * math.cos(a):.0f} {130 * math.sin(a):.0f}"/>'
                  for a in [math.pi * (0.55 + k * 0.18) for k in range(6)])
    seg = "".join(f'<rect class="ln" x="{-210 + k * 75}" y="-26" width="62" height="52" rx="24" style="fill:{sheath};stroke-width:5"/>'
                  for k in range(int(myelin)))
    return g(x, y, s, den + '<path class="ln" style="stroke-width:9" d="M-240 0 H250"/>' + seg
             + f'<circle class="ln" cx="-300" cy="0" r="70" style="fill:{color}"/><circle cx="-300" cy="0" r="22" style="fill:#d4567a"/>'
             + '<path class="ln" style="stroke-width:7" d="M250 0 l50 -40 M250 0 l60 0 M250 0 l50 40"/>')


def signal(x, y, s=1.0, color="#ffb347"):
    return g(x, y, s, f'<path class="ln" style="fill:{color};stroke:#f08a00" d="M0 -40 l25 35 l-12 0 l20 45 l-45 -50 l14 0z"/>')


def dirt_path(x, y, s=1.0):
    import random
    r = random.Random(1)
    grass = "".join(f'<path class="ln" style="stroke:#3fa35a;stroke-width:5" d="M{r.uniform(-380, 380):.0f} {r.uniform(-120, 120):.0f} l-8 -26 M{0} {0} l0 0"/>' for _ in range(40))
    return g(x, y, s, '<rect class="ln" x="-400" y="-140" width="800" height="280" rx="30" style="fill:#7ed957"/>' + grass
             + '<path class="ln" style="fill:#c9a27a;stroke-width:5" d="M-400 30 q200 -60 400 -10 q200 50 400 -20 v40 q-200 70 -400 20 q-200 -50 -400 10z"/>')


def highway(x, y, s=1.0):
    dashes = "".join(f'<rect x="{-380 + k * 110}" y="-6" width="60" height="12" style="fill:#ffd23f"/>' for k in range(8))
    return g(x, y, s, '<rect class="ln" x="-400" y="-110" width="800" height="220" style="fill:#4a4a52"/>' + dashes
             + '<path class="ln" style="stroke:#fff;stroke-width:8" d="M-400 -90 H400 M-400 90 H400"/>')


def snail(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#c9e2a0" d="M-160 60 q-20 -50 40 -50 h170 q60 0 70 -60 l14 -40 l10 44 q10 90 -80 106z"/>'
                      '<circle class="ln" cx="-20" cy="-40" r="90" style="fill:#d9a066"/>'
                      '<path class="ln" style="stroke-width:6" d="M-20 -40 m-55 0 a55 55 0 1 1 55 55 a35 35 0 1 1 -35 -35 a18 18 0 1 1 18 18"/>'
                      '<path class="ln" style="stroke-width:5" d="M110 -70 l-10 -50 M130 -70 l10 -50"/>'
                      '<circle cx="98" cy="-124" r="9" style="fill:#111"/><circle cx="142" cy="-124" r="9" style="fill:#111"/>')


def bar_pair(x, y, s=1.0, a_label="", b_label="", a_h=1.0, b_h=1.0, a_col="#7ed957", b_col="#c9ced6", a_n=7, b_n=1):
    a = "".join(f'<rect class="ln" x="{-330 + k * 42}" y="{-200 * a_h}" width="34" height="{200 * a_h}" style="fill:{a_col};stroke-width:4"/>' for k in range(a_n))
    b = "".join(f'<rect class="ln" x="{80 + k * 42}" y="{-200 * b_h}" width="{34 if b_n > 1 else 240}" height="{200 * b_h}" style="fill:{b_col};stroke-width:4"/>' for k in range(b_n))
    return g(x, y, s, a + b + '<path class="ln" d="M-360 0 H360"/>') + hand(a_label, x - 180 * s, y + 80 * s, 70 * s, "hand green") + hand(b_label, x + 200 * s, y + 80 * s, 70 * s, "hand")


# ---------- движение ----------
def mv(svg, kind, a=10, p=1.6, d="", x=0, y=0):
    """обёртка движения: bob / wiggle / pulse / spin / move / travel / rise / grow / appear.
    a — размах (px, градусы или доля для pulse), p — период (с), d — задержка (с; пусто = после прорисовки),
    x, y — смещение для move/travel/rise."""
    return f'<g class="mv" data-kind="{kind}" data-a="{a}" data-p="{p}" data-d="{d}" data-x="{x}" data-y="{y}">{svg}</g>'


# ---------- детские песенки ----------
def happy_star(x, y, s=1.0, color="#ffd23f"):
    import math
    pts = " ".join(f"{(150 if i % 2 == 0 else 62) * math.sin(i * math.pi / 5):.0f},{-(150 if i % 2 == 0 else 62) * math.cos(i * math.pi / 5):.0f}" for i in range(10))
    return g(x, y, s, f'<polygon class="ln" points="{pts}" style="fill:{color}"/>'
                      '<circle cx="-28" cy="-10" r="10" style="fill:#111"/><circle cx="28" cy="-10" r="10" style="fill:#111"/>'
                      '<circle cx="-24" cy="-14" r="3.5" style="fill:#fff"/><circle cx="32" cy="-14" r="3.5" style="fill:#fff"/>'
                      '<path class="ln" style="stroke-width:6" d="M-24 18 q24 22 48 0"/>'
                      '<circle cx="-50" cy="14" r="11" style="fill:#ff9fb3;opacity:.6"/><circle cx="50" cy="14" r="11" style="fill:#ff9fb3;opacity:.6"/>')


def diamond(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#bfe6ff" d="M-150 -40 L-80 -120 H80 L150 -40 L0 160 Z"/>'
                      '<path class="ln" style="fill:#9fd6ff;stroke-width:5" d="M-150 -40 H150 M-80 -120 L-40 -40 L0 160 L40 -40 L80 -120 M-40 -40 L0 -120 L40 -40"/>'
                      '<path style="fill:#fff;opacity:.8" d="M-100 -60 l20 -30 h30 l-25 30z"/>')


def sparkle(x, y, s=1.0, color="#fff6c8"):
    return g(x, y, s, f'<path style="fill:{color}" d="M0 -40 Q6 -6 40 0 Q6 6 0 40 Q-6 6 -40 0 Q-6 -6 0 -40z"/>')


# ---------- запахи и ИИ ----------
def nose(x, y, s=1.0, color="#ffcfb3", robot=False, face=None):
    body = (f'<path class="ln" style="fill:{"#c9ced6" if robot else color}" d="M-20 -200 q-30 120 -110 220 q-40 60 20 80 q40 10 60 -20 '
            'q50 40 100 0 q20 30 60 20 q60 -20 20 -80 q-80 -100 -110 -220 z"/>'
            '<ellipse cx="-50" cy="80" rx="22" ry="14" style="fill:#5a3a3a"/><ellipse cx="50" cy="80" rx="22" ry="14" style="fill:#5a3a3a"/>')
    if robot:
        body += ('<path class="ln" style="stroke:#4fa3f7;stroke-width:5" d="M-10 -150 v80 h-40 v60 M10 -150 v60 h50 v50"/>'
                 '<circle cx="-50" cy="-10" r="10" style="fill:#4fa3f7"/><circle cx="60" cy="-40" r="10" style="fill:#4fa3f7"/>'
                 '<circle class="ln" cx="0" cy="-200" r="16" style="fill:#ffd23f"/>')
    if face:
        eyes = ('<ellipse cx="-34" cy="-70" rx="16" ry="20" style="fill:#fff" class="ln"/><ellipse cx="34" cy="-70" rx="16" ry="20" style="fill:#fff" class="ln"/>'
                '<circle cx="-30" cy="-66" r="8" style="fill:#111"/><circle cx="38" cy="-66" r="8" style="fill:#111"/>')
        if face == "happy":
            eyes = '<path class="ln" style="stroke-width:6" d="M-50 -66 q16 -18 32 0 M18 -66 q16 -18 32 0"/>'
        mouth = {"smile": '<path class="ln" style="stroke-width:6" d="M-30 130 q30 24 60 0"/>',
                 "happy": '<path class="ln" style="fill:#e0457b;stroke-width:5" d="M-34 126 q34 40 68 0z"/>',
                 "o": '<circle class="ln" cx="0" cy="136" r="14" style="fill:#7a2230"/>',
                 "sad": '<path class="ln" style="stroke-width:6" d="M-28 140 q28 -20 56 0"/>'}[face if face in ("smile", "happy", "o", "sad") else "smile"]
        body += eyes + mouth + '<circle cx="-70" cy="-20" r="14" style="fill:#ff9fb3;opacity:.6"/><circle cx="70" cy="-20" r="14" style="fill:#ff9fb3;opacity:.6"/>'
    return g(x, y, s, body)


def molecule(x, y, s=1.0):
    atoms = [(0, 0, 40, "#e63946"), (-110, -60, 30, "#4fa3f7"), (110, -50, 32, "#2b2b30"), (-90, 90, 28, "#7ed957"), (100, 90, 30, "#ffd23f"), (0, -140, 26, "#b79bff")]
    bonds = "".join(f'<path class="ln" style="stroke-width:9" d="M0 0 L{ax} {ay}"/>' for ax, ay, _, _ in atoms[1:])
    return g(x, y, s, bonds + "".join(f'<circle class="ln" cx="{ax}" cy="{ay}" r="{r}" style="fill:{c}"/>' for ax, ay, r, c in atoms))


def perfume(x, y, s=1.0, color="#ff8fc7"):
    return g(x, y, s, f'<rect class="ln" x="-90" y="-60" width="180" height="200" rx="40" style="fill:{color};fill-opacity:.85"/>'
                      '<rect class="ln" x="-30" y="-110" width="60" height="50" style="fill:#e8e8ee"/>'
                      '<rect class="ln" x="-45" y="-160" width="90" height="50" rx="12" style="fill:#d4a537"/>'
                      '<path style="fill:#fff;opacity:.5" d="M-60 -30 q10 -20 30 -20 v120 q-30 0 -30 -30z"/>')


def sneaker(x, y, s=1.0, color="#4fa3f7"):
    return g(x, y, s, f'<path class="ln" style="fill:{color}" d="M-200 60 v-60 q0 -40 40 -60 l60 -30 q30 40 70 40 l120 50 q90 20 110 60 v20z"/>'
                      '<rect class="ln" x="-205" y="60" width="410" height="40" rx="18" style="fill:#fff"/>'
                      '<path class="ln" style="stroke-width:5" d="M-110 -70 l40 20 M-90 -85 l40 20 M-70 -100 l40 20"/>')


def magnifier(x, y, s=1.0):
    return g(x, y, s, '<circle class="ln" cx="0" cy="0" r="90" style="fill:#cfe8ff;fill-opacity:.6;stroke-width:12"/>'
                      '<path class="ln" style="stroke-width:26" d="M64 64 L170 170"/>')


def paper(x, y, s=1.0, title="Science"):
    lines = "".join(f'<path class="ln" style="stroke:#c9ced6;stroke-width:8" d="M-110 {-30 + k * 40} h{220 - (k % 2) * 60}"/>' for k in range(5))
    return g(x, y, s, '<rect class="ln" x="-150" y="-200" width="300" height="400" style="fill:#fff"/>'
                      f'<text class="hand" x="0" y="-110" font-size="70" text-anchor="middle" style="fill:#d7263d">{title}</text>' + lines)


def flower(x, y, s=1.0, color="#ff8fc7"):
    petals = "".join(f'<ellipse class="ln" cx="0" cy="-55" rx="30" ry="48" transform="rotate({k * 60})" style="fill:{color};stroke-width:5"/>' for k in range(6))
    return g(x, y, s, '<path class="ln" style="stroke:#2e9d5b;stroke-width:10" d="M0 40 V200"/>' + petals + '<circle class="ln" cx="0" cy="0" r="32" style="fill:#ffd23f"/>')


def mist(x, y, n=8, dx=260, color="#ffc6e5"):
    return "".join(mv(f'<circle cx="{x}" cy="{y + (k % 3 - 1) * 14}" r="{10 + k % 4 * 5}" style="fill:{color}"/>', "travel", x=dx, y=(k % 5 - 2) * 40, p=0.9, d=round(k * 0.11, 2)) for k in range(n))


def coin_rain(n=14, seed=2, top=-200, bottom=1100):
    import random
    r = random.Random(seed)
    return "".join(mv(g(r.uniform(60, 940), top, 1, '<circle class="ln" r="30" style="fill:#ffd23f;stroke-width:5"/><text class="hand" y="14" font-size="40" text-anchor="middle">$</text>'),
                      "fall", a=r.uniform(-360, 360), x=r.uniform(-60, 60), y=bottom - top, p=r.uniform(1.1, 1.8), d=round(r.uniform(0, 1.5), 2)) for _ in range(n))


def thought(x, y, s=1.0, inner=""):
    return g(x, y, s, '<ellipse class="ln" cx="0" cy="0" rx="190" ry="140" style="fill:#fff"/>'
                      '<circle class="ln" cx="-150" cy="170" r="30" style="fill:#fff"/><circle class="ln" cx="-200" cy="230" r="16" style="fill:#fff"/>') + inner


def apple(x, y, s=1.0):
    return g(x, y, s, '<circle class="ln" cx="0" cy="0" r="40" style="fill:#e63946"/><path class="ln" style="stroke-width:6" d="M0 -40 v-18"/>'
                      '<path class="ln" style="fill:#2e9d5b;stroke-width:4" d="M4 -50 q25 -15 34 5 q-20 8 -34 -5z"/>')


# ---------- эмоции и тело ----------
def brain_face(x, y, s=1.0, mood="smile", color="#ff9fb3"):
    eyes = {"smile": '<circle cx="-40" cy="-10" r="11" style="fill:#111"/><circle cx="40" cy="-10" r="11" style="fill:#111"/>'
                     '<circle cx="-36" cy="-14" r="4" style="fill:#fff"/><circle cx="44" cy="-14" r="4" style="fill:#fff"/>',
            "scared": '<circle class="ln" cx="-40" cy="-14" r="20" style="fill:#fff;stroke-width:5"/><circle class="ln" cx="40" cy="-14" r="20" style="fill:#fff;stroke-width:5"/>'
                      '<circle cx="-40" cy="-14" r="7" style="fill:#111"/><circle cx="40" cy="-14" r="7" style="fill:#111"/>',
            "calm": '<path class="ln" style="stroke-width:6" d="M-56 -8 q16 12 32 0 M24 -8 q16 12 32 0"/>'}[mood]
    mouth = {"smile": '<path class="ln" style="stroke-width:6" d="M-24 36 q24 22 48 0"/>',
             "scared": '<path class="ln" style="fill:#7a2230;stroke-width:5" d="M-26 50 q26 -30 52 0 q-26 14 -52 0z"/>',
             "calm": '<path class="ln" style="stroke-width:6" d="M-20 40 q20 14 40 0"/>'}[mood]
    sweat = ('<path class="ln" style="fill:#9cd2ff;stroke-width:4" d="M110 -70 q14 24 0 34 q-14 -10 0 -34z"/>' if mood == "scared" else "")
    head = (f'<path class="ln" style="fill:{color}" d="M-150 40 q-40 -90 30 -130 q20 -70 100 -55 q70 -45 130 10 q80 0 70 90 q40 60 -20 110 q-40 50 -130 40 q-90 20 -140 -20 q-60 -10 -40 -45z"/>'
            '<path class="ln" style="stroke-width:5" d="M-90 -110 q20 30 60 20 M10 -150 q-10 40 30 50 M90 -100 q-30 20 -10 50"/>')
    return g(x, y, s, head + eyes + mouth + sweat +
                                     '<circle cx="-75" cy="22" r="14" style="fill:#ff6f91;opacity:.5"/><circle cx="75" cy="22" r="14" style="fill:#ff6f91;opacity:.5"/>')


def alarm_clock(x, y, s=1.0):
    return g(x, y, s, '<circle class="ln" cx="-80" cy="-120" r="44" style="fill:#ffd23f"/><circle class="ln" cx="80" cy="-120" r="44" style="fill:#ffd23f"/>'
                      '<circle class="ln" cx="0" cy="0" r="130" style="fill:#e63946"/><circle class="ln" cx="0" cy="0" r="100" style="fill:#fff"/>'
                      '<path class="ln" style="stroke-width:9" d="M0 0 V-70 M0 0 L50 30"/>'
                      '<path class="ln" style="stroke-width:8" d="M-80 130 l-30 40 M80 130 l30 40"/>')


def lion(x, y, s=1.0):
    mane = "".join(f'<ellipse class="ln" cx="0" cy="-125" rx="36" ry="60" transform="rotate({k * 30})" style="fill:#d9822b;stroke-width:5"/>' for k in range(12))
    return g(x, y, s, mane + '<circle class="ln" cx="0" cy="0" r="110" style="fill:#f2b35b"/>'
                      '<circle cx="-38" cy="-20" r="11" style="fill:#111"/><circle cx="38" cy="-20" r="11" style="fill:#111"/>'
                      '<path class="ln" style="fill:#7a2230" d="M-40 40 q40 50 80 0 z"/><path class="ln" style="fill:#5a3a2a" d="M-20 10 h40 l-20 22z"/>'
                      '<path class="ln" style="stroke-width:6" d="M-60 -60 l30 14 M60 -60 l-30 14"/>')


def envelope(x, y, s=1.0, color="#fff"):
    return g(x, y, s, f'<rect class="ln" x="-150" y="-100" width="300" height="200" rx="12" style="fill:{color}"/>'
                      '<path class="ln" d="M-150 -100 L0 20 L150 -100"/>'
                      '<circle class="ln" cx="150" cy="-100" r="40" style="fill:#e63946"/><text class="hand" x="150" y="-86" font-size="50" text-anchor="middle" style="fill:#fff">!</text>')


def lungs(x, y, s=1.0, color="#ff9fb3"):
    return g(x, y, s, '<path class="ln" style="stroke-width:12" d="M0 -200 V-40 M0 -40 q-40 10 -70 40 M0 -40 q40 10 70 40"/>'
                      f'<path class="ln" style="fill:{color}" d="M-40 -120 q-150 -40 -160 140 q0 120 110 110 q60 -10 60 -100z"/>'
                      f'<path class="ln" style="fill:{color}" d="M40 -120 q150 -40 160 140 q0 120 -110 110 q-60 -10 -60 -100z"/>')


def stairs(x, y, s=1.0, n=5, color="#b79bff"):
    return g(x, y, s, "".join(f'<rect class="ln" x="{-250 + k * 100}" y="{-k * 70}" width="100" height="{70 + k * 70}" style="fill:{color};stroke-width:5"/>' for k in range(n)))


def sense_icon(kind, x, y, s=1.0):
    icons = {"eye": '<path class="ln" style="fill:#fff" d="M-70 0 q70 -60 140 0 q-70 60 -140 0z"/><circle cx="0" cy="0" r="24" style="fill:#4fa3f7"/><circle cx="0" cy="0" r="10" style="fill:#111"/>',
             "hand": '<path class="ln" style="fill:#ffcfb3" d="M-40 60 v-90 q0 -16 14 -16 q14 0 14 16 v50 v-80 q0 -16 14 -16 q14 0 14 16 v80 v-70 q0 -16 14 -16 q14 0 14 16 v90 q0 50 -50 50 h-20 q-30 0 -48 -30z"/>',
             "ear": '<path class="ln" style="fill:#ffcfb3" d="M-30 60 q-40 -40 -30 -90 q20 -60 80 -40 q50 20 30 80 q-14 30 -40 30 q-14 0 -14 20 q0 30 -26 0z"/>',
             "nose": '<path class="ln" style="fill:#ffcfb3" d="M-10 -70 q-20 60 -50 100 q-20 30 10 40 q20 6 30 -10 q24 20 50 0 q10 16 30 10 q30 -10 10 -40 q-30 -40 -50 -100z"/>',
             "mouth": '<path class="ln" style="fill:#e58a90" d="M-70 0 q35 -36 70 -10 q35 -26 70 10 q-70 60 -140 0z"/>'}
    return g(x, y, s, icons[kind])


# ---------- Дублин ----------
def spire(x, y, s=1.0, h=900, lit=False):
    top = (f'<circle cx="0" cy="{-h}" r="40" style="fill:#fff6c8;opacity:.8"/>'
           f'<circle cx="0" cy="{-h}" r="90" style="fill:#fff6c8;opacity:.25"/>' if lit else "")
    return g(x, y, s, f'<path class="ln" style="fill:#d9dee6;stroke-width:5" d="M-24 0 L-2 {-h} L2 {-h} L24 0 Z"/>'
                      f'<path style="fill:#fff;opacity:.6" d="M-10 0 L-1 {-h + 30} L2 {-h + 30} L-2 0z"/>'
                      f'<rect class="ln" x="-60" y="0" width="120" height="30" style="fill:#9aa1ab;stroke-width:5"/>' + top)


def pillar(x, y, s=1.0, broken=False):
    col = ('<rect class="ln" x="-45" y="-380" width="90" height="380" style="fill:#c9c2b8"/>' if not broken else
           '<path class="ln" style="fill:#c9c2b8" d="M-45 0 V-190 l20 -20 l15 15 l25 -25 l15 20 l15 -10 V0z"/>')
    statue = ('' if broken else '<rect class="ln" x="-70" y="-410" width="140" height="30" style="fill:#b0a89c"/>'
              '<circle class="ln" cx="0" cy="-470" r="22" style="fill:#8d929b"/><path class="ln" style="fill:#8d929b" d="M-25 -448 h50 l10 40 h-70z"/>'
              '<path class="ln" style="fill:#2b2b30" d="M-24 -490 q24 -18 48 0 z"/>')
    return g(x, y, s, '<rect class="ln" x="-110" y="0" width="220" height="70" style="fill:#b0a89c"/>' + col + statue)


def boom(x, y, s=1.0):
    import math
    pts = " ".join(f"{(150 if k % 2 == 0 else 70) * math.cos(k * math.pi / 8):.0f},{(150 if k % 2 == 0 else 70) * math.sin(k * math.pi / 8):.0f}" for k in range(16))
    return g(x, y, s, f'<polygon class="ln" points="{pts}" style="fill:#ffb347"/>'
                      f'<polygon points="{" ".join(p for p in pts.split())}" transform="scale(.55)" style="fill:#ffe066"/>'
                      '<text class="hand" x="0" y="22" font-size="70" text-anchor="middle" style="fill:#d7263d">BOOM</text>')


def street(y=900, seed=3):
    import random
    r = random.Random(seed)
    out, x = "", -40
    cols = ["#e8c9a0", "#c9a7f5", "#9fd6c8", "#f2b8a0", "#cfd8e8"]
    while x < 1040:
        w, h = r.uniform(110, 170), r.uniform(220, 380)
        out += f'<rect class="ln" x="{x:.0f}" y="{y - h:.0f}" width="{w:.0f}" height="{h:.0f}" style="fill:{r.choice(cols)};stroke-width:5"/>'
        for wy in range(int(y - h + 30), int(y - 40), 60):
            for wx in range(int(x + 18), int(x + w - 30), 40):
                out += f'<rect class="ln" x="{wx}" y="{wy}" width="22" height="32" style="fill:#fff;stroke-width:3"/>'
        x += w
    return out + f'<rect class="ln" x="-40" y="{y}" width="1080" height="80" style="fill:#9aa1ab"/>'


def bigben(x, y, s=1.0, h=640):
    return g(x, y, s, f'<rect class="ln" x="-50" y="{-h}" width="100" height="{h}" style="fill:#d9b26b"/>'
                      f'<circle class="ln" cx="0" cy="{-h + 120}" r="38" style="fill:#fff"/>'
                      f'<path class="ln" style="fill:#4a6b4a" d="M-56 {-h} L0 {-h - 110} L56 {-h} Z"/>')


def stiletto(x, y, s=1.0, color="#e63946"):
    return g(x, y, s, f'<path class="ln" style="fill:{color}" d="M-160 40 q0 -50 40 -60 q80 -10 140 -80 q30 -30 60 0 l60 120 q-20 20 -40 20 z"/>'
                      '<path class="ln" style="fill:#2b2b30" d="M120 40 l10 110 l14 0 l-4 -110z"/>')


def liffey(y=880):
    waves = "".join(f'<path class="ln" style="stroke:#fff;stroke-width:5" d="M{x} {y + 40} q30 -20 60 0 q30 20 60 0"/>' for x in range(-40, 1040, 160))
    return f'<rect x="-40" y="{y}" width="1080" height="140" style="fill:#5b8fd6"/>' + waves


# ---------- история Ирландии ----------
def potato(x, y, s=1.0, rotten=False):
    col = "#7a6a4a" if rotten else "#c9a066"
    spots = ('<circle cx="-30" cy="-10" r="16" style="fill:#3b2f1f"/><circle cx="25" cy="15" r="20" style="fill:#3b2f1f"/><circle cx="40" cy="-25" r="10" style="fill:#3b2f1f"/>'
             if rotten else '<circle cx="-30" cy="-10" r="5" style="fill:#8a6a3a"/><circle cx="25" cy="15" r="5" style="fill:#8a6a3a"/><circle cx="40" cy="-25" r="4" style="fill:#8a6a3a"/>')
    return g(x, y, s, f'<path class="ln" style="fill:{col}" d="M-90 0 q0 -60 70 -66 q90 -6 110 50 q14 60 -60 76 q-120 20 -120 -60z"/>' + spots)


def crescent_star(x, y, s=1.0, color="#fff", stroke=True):
    import math
    st = " ".join(f"{70 + (34 if k % 2 == 0 else 14) * math.sin(k * math.pi / 5):.0f},{-(34 if k % 2 == 0 else 14) * math.cos(k * math.pi / 5):.0f}" for k in range(10))
    ln = 'class="ln" ' if stroke else ""
    return g(x, y, s, f'<path {ln}style="fill:{color};stroke-width:5" d="M30 -70 a75 75 0 1 0 0 140 a60 60 0 1 1 0 -140z"/>'
                      f'<polygon {ln}points="{st}" style="fill:{color};stroke-width:4"/>')


def shield(x, y, s=1.0, inner=""):
    return g(x, y, s, '<path class="ln" style="fill:#2f6fdb" d="M-170 -200 H170 V20 Q170 170 0 230 Q-170 170 -170 20 Z"/>'
                      '<path class="ln" style="fill:none;stroke:#ffd23f;stroke-width:8" d="M-150 -180 H150 V20 Q150 150 0 205 Q-150 150 -150 20 Z"/>') + inner


def ship(x, y, s=1.0, flag=""):
    return g(x, y, s, '<path class="ln" style="fill:#8a5a3b" d="M-200 0 H200 L150 90 H-150 Z"/>'
                      '<path class="ln" style="stroke-width:10" d="M-40 0 V-260 M80 0 V-200"/>'
                      '<path class="ln" style="fill:#fff6e0" d="M-40 -250 q110 60 0 220z M80 -190 q80 50 0 170z"/>'
                      '<path class="ln" style="fill:#e63946" d="M-40 -260 l60 15 l-60 15z"/>') + flag


def sea(y=820, color="#5b8fd6"):
    waves = "".join(mv(f'<path class="ln" style="stroke:#fff;stroke-width:5" d="M{x} {y + 50} q30 -20 60 0 q30 20 60 0"/>', "bob", a=8, p=0.9, d=0.1 * (x % 5)) for x in range(-40, 1040, 160))
    return f'<rect x="-40" y="{y}" width="1080" height="260" style="fill:{color}"/>' + waves


def crown(x, y, s=1.0):
    return g(x, y, s, '<path class="ln" style="fill:#ffd23f" d="M-110 40 L-120 -70 L-60 -10 L0 -90 L60 -10 L120 -70 L110 40 Z"/>'
                      '<circle cx="0" cy="-20" r="12" style="fill:#e63946"/><circle cx="-70" cy="10" r="9" style="fill:#4fa3f7"/><circle cx="70" cy="10" r="9" style="fill:#4fa3f7"/>')


def kindred_feathers(x, y, s=1.0):
    import math
    out = ""
    for k in range(9):
        a = -math.pi / 2 + (k - 4) * 0.16
        fx = 150 * math.cos(a + math.pi / 2) * 0.0 + (k - 4) * 55
        out += (f'<path class="ln" style="fill:#c9ced6" d="M{fx} 0 q-24 -220 0 -{380 + (4 - abs(k - 4)) * 30} q24 {200 + (4 - abs(k - 4)) * 30} 0 {380 + (4 - abs(k - 4)) * 30}z" '
                f'transform="rotate({(k - 4) * 4} {fx} 0)"/>')
    return g(x, y, s, out + '<rect class="ln" x="-280" y="0" width="560" height="30" style="fill:#9aa1ab"/>')
