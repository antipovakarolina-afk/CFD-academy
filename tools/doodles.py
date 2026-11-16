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
