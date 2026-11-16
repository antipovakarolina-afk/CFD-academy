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
       hair="#3b2a22", skin="#f7dccb", coat="#1c1b20", lips="#e48a90", iris="#8fb3d9", nails="#7a1730"):
    """Героиня — автор блога: тёмно-каштановые волосы, собранные назад, лёгкая чёлка-шторка
    и пряди у лица, серо-голубые глаза, розовые губы, золотые серёжки-колечки,
    чёрное пальто с высоким воротником и поясом, бордовый маникюр."""
    mouth = {
        "smile": f'<path class="ln" style="fill:{lips};stroke-width:3.5" d="M-22 -168 q22 20 44 0 q-22 7 -44 0z"/>',
        "big": f'<path class="ln" style="fill:{lips};stroke-width:3.5" d="M-24 -180 q24 -4 48 0 q-24 32 -48 0z"/>'
               '<path d="M-17 -167 q17 -2 34 0 l-3 6 q-14 -1 -28 0z" style="fill:#fff"/>',
        "o": f'<ellipse class="ln" style="fill:{lips};stroke-width:3.5" cx="0" cy="-162" rx="11" ry="12"/>'
             '<ellipse cx="0" cy="-161" rx="5" ry="6" style="fill:#7a2230"/>',
        "worry": f'<path class="ln" style="fill:{lips};stroke-width:3.5" d="M-18 -160 q18 -12 36 0 q-18 8 -36 0z"/>',
    }[mood]
    def eye(ex):
        o = 1 if ex > 0 else -1          # ресничка — наружу
        return (f'<ellipse cx="{ex}" cy="-198" rx="15" ry="16" style="fill:#fff"/>'
                f'<circle cx="{ex}" cy="-196" r="11" style="fill:{iris}"/>'
                f'<circle cx="{ex}" cy="-196" r="5.5" style="fill:#111"/>'
                f'<circle cx="{ex + 4}" cy="-201" r="3.5" style="fill:#fff"/>'
                f'<path class="ln" style="stroke-width:4" d="M{ex - 16} -203 Q{ex} -218 {ex + 16} -203"/>'
                f'<path class="ln" style="stroke-width:3" d="M{ex + 15 * o} -206 l{7 * o} -5"/>')
    hands = lambda pts: "".join(
        f'<circle class="ln" cx="{hx}" cy="{hy}" r="14" style="fill:{skin}"/>'
        f'<circle cx="{hx + 6}" cy="{hy - 9}" r="4" style="fill:{nails}"/><circle cx="{hx - 5}" cy="{hy - 10}" r="4" style="fill:{nails}"/>'
        for hx, hy in pts)
    sleeve = f'style="stroke:{coat};stroke-width:22"'
    arms = {
        "phone": (f'<path class="ln" {sleeve} d="M-62 -100 Q-105 -20 -24 -28"/><path class="ln" {sleeve} d="M62 -100 Q105 -20 24 -28"/>'
                  '<rect class="ln" x="-28" y="-100" width="56" height="92" rx="12" style="fill:#c9c5bd"/>'
                  '<circle cx="-12" cy="-84" r="6" style="fill:#333"/><circle cx="4" cy="-84" r="6" style="fill:#333"/><circle cx="-4" cy="-70" r="6" style="fill:#333"/>'
                  + hands([(-22, -28), (22, -28)])),
        "wave": (f'<path class="ln" {sleeve} d="M-62 -100 Q-100 -10 -92 50"/>'
                 f'<path class="ln" {sleeve} d="M62 -100 Q140 -150 135 -245"/>' + hands([(-92, 60), (135, -258)])),
        "think": (f'<path class="ln" {sleeve} d="M-62 -100 Q-100 -10 -92 50"/>'
                  f'<path class="ln" {sleeve} d="M62 -100 Q120 -60 45 -150"/>' + hands([(-92, 60), (42, -156)])),
        "down": (f'<path class="ln" {sleeve} d="M-62 -100 Q-100 -10 -92 50"/><path class="ln" {sleeve} d="M62 -100 Q100 -10 92 50"/>'
                 + hands([(-92, 60), (92, 60)])),
    }[pose]
    body = (
        # хвост сзади и волосы за головой
        f'<path class="ln" style="fill:{hair}" d="M70 -300 Q150 -290 140 -200 Q135 -150 110 -120 Q120 -190 90 -250 Z"/>'
        f'<path class="ln" style="fill:{hair}" d="M-96 -170 Q-118 -260 -90 -305 Q0 -375 90 -305 Q118 -260 96 -170 Z"/>'
        # ноги, туфли, пальто с поясом и воротником
        '<path class="ln" style="stroke:#2a2a30;stroke-width:12" d="M-35 130 v115 M35 130 v115"/>'
        '<ellipse class="ln" cx="-46" cy="252" rx="28" ry="12" style="fill:#111"/><ellipse class="ln" cx="46" cy="252" rx="28" ry="12" style="fill:#111"/>'
        f'<path class="ln" style="fill:{coat}" d="M-60 -118 Q0 -128 60 -118 L95 140 H-95 Z"/>'
        '<path class="ln" style="stroke:#55545e;stroke-width:5" d="M0 -110 L6 140"/>'
        '<path class="ln" style="stroke:#55545e;stroke-width:12" d="M-78 30 H80"/>'
        f'<path class="ln" style="fill:{coat};stroke:#55545e;stroke-width:5" d="M-48 -150 L-62 -100 L-8 -60 L-20 -130 Z"/>'
        f'<path class="ln" style="fill:{coat};stroke:#55545e;stroke-width:5" d="M48 -150 L62 -100 L8 -60 L20 -130 Z"/>'
        # шея и лицо
        f'<path class="ln" style="fill:{skin}" d="M-18 -150 v30 h36 v-30z"/>'
        f'<ellipse class="ln" cx="0" cy="-222" rx="80" ry="90" style="fill:{skin}"/>'
        '<circle cx="-50" cy="-176" r="13" style="fill:#ff9fb3;opacity:.55"/><circle cx="50" cy="-176" r="13" style="fill:#ff9fb3;opacity:.55"/>'
        + eye(-32) + eye(32) +
        '<path class="ln" style="stroke-width:4" d="M-2 -186 q5 10 -2 13"/>'
        + mouth +
        # серёжки-колечки
        '<circle class="ln" cx="-80" cy="-188" r="9" style="stroke:#d4a537;stroke-width:4"/>'
        '<circle class="ln" cx="80" cy="-188" r="9" style="stroke:#d4a537;stroke-width:4"/>'
        # пряди у лица и чёлка-шторка
        f'<path class="ln" style="fill:{hair};stroke-width:5" d="M-86 -255 Q-104 -190 -92 -125 Q-80 -175 -66 -228 Z"/>'
        f'<path class="ln" style="fill:{hair};stroke-width:5" d="M86 -255 Q104 -190 92 -125 Q80 -175 66 -228 Z"/>'
        f'<path class="ln" style="fill:{hair}" d="M0 -330 Q-92 -328 -90 -240 Q-88 -205 -78 -196 Q-74 -228 -62 -224 '
        'Q-54 -250 -40 -236 Q-28 -258 -14 -244 Q-6 -280 0 -300 Z"/>'
        f'<path class="ln" style="fill:{hair}" d="M0 -330 Q92 -328 90 -240 Q88 -205 78 -196 Q74 -228 62 -224 '
        'Q54 -250 40 -236 Q28 -258 14 -244 Q6 -280 0 -300 Z"/>'
        f'<path class="ln" style="stroke:#5a4034;stroke-width:3" d="M-40 -300 q-6 30 -10 50 M10 -305 q-4 30 -6 48 M45 -295 q4 25 6 45"/>'
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
