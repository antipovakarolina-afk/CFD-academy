"""Элементы для тёмного стиля «инфографика» (SVG, поле 1000×1000).

Обёртка `item(...)` — элемент, который появляется (плавно всплывает) по очереди.
`count(...)` — число, которое «набегает». `bars(...)` — растущие столбцы.
Классы: s — светящаяся линия, d — линия, которая прорисовывается, a — акцентный цвет.
"""
import math

WHITE = "#e8eefc"
MUTED = "#8ea3c8"
YELLOW = "#ffc845"
GREEN = "#3ddc84"
RED = "#ff5a5f"
BLUE = "#5aa9ff"
PURPLE = "#b48cff"
CARD = "rgba(255,255,255,0.045)"
EDGE = "rgba(150,180,240,0.35)"


def item(body, dx=0, dy=0):
    """элемент появляется по очереди"""
    return f'<g class="in"><g transform="translate({dx},{dy})">{body}</g></g>'


def text(t, x, y, size=48, color=WHITE, font="sans", anchor="middle", weight=800, spacing=0):
    fam = "Mono" if font == "mono" else "Sans"
    return (f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" '
            f'style="font-family:{fam};font-weight:{weight};fill:{color};letter-spacing:{spacing}em">{t}</text>')


def label(t, x, y, color=MUTED, size=24, anchor="middle"):
    return text(t.upper(), x, y, size, color, "mono", anchor, 500, 0.18)


def count(to, x, y, size=150, color=YELLOW, prefix="", suffix="", dec=0, start=0, font="mono", anchor="middle"):
    fam = "Mono" if font == "mono" else "Sans"
    return (f'<text class="count" data-to="{to}" data-from="{start}" data-dec="{dec}" data-prefix="{prefix}" '
            f'data-suffix="{suffix}" x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" '
            f'style="font-family:{fam};font-weight:800;fill:{color}">{prefix}{to}{suffix}</text>')


def card(x, y, w, h, title=None, accent=None, r=26):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" style="fill:{CARD};stroke:{accent or EDGE};stroke-width:3"/>'
    if accent:
        out += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" style="fill:none;stroke:{accent};stroke-width:3;filter:url(#glow);opacity:.6"/>'
    if title:
        out += label(title, x + 30, y + 50, MUTED, 22, "start")
    return out


def pill(t, x, y, color=YELLOW, size=30):
    w = len(t) * size * 0.68 + 50
    return (f'<rect x="{x - w / 2}" y="{y - size}" width="{w}" height="{size * 1.6}" rx="{size * 0.8}" '
            f'style="fill:none;stroke:{color};stroke-width:3"/>' + text(t, x, y + size * 0.3, size, color, "mono", "middle", 800))


def bars(x, y, w, h, values, labels=(), colors=None, fmt_prefix="", fmt_suffix="", maxv=None):
    """столбцы от базовой линии y (низ) вверх; подписи сверху «набегают»"""
    n = len(values)
    maxv = maxv or max(values)
    gap = w / n
    bw = gap * 0.55
    out = f'<path class="s" d="M{x} {y} H{x + w}"/>'
    for i, v in enumerate(values):
        bh = h * v / maxv
        cx = x + gap * i + gap / 2
        col = (colors or [BLUE])[i % len(colors or [BLUE])]
        out += (f'<rect class="bar" x="{cx - bw / 2}" y="{y - bh}" width="{bw}" height="{bh}" rx="10" '
                f'style="fill:{col};opacity:.9"/>')
        out += count(v, cx, y - bh - 24, 44, col, fmt_prefix, fmt_suffix)
        if i < len(labels):
            out += label(labels[i], cx, y + 50, MUTED, 24)
    return out


def arrow(x1, y1, x2, y2, color=WHITE, w=6):
    a = math.atan2(y2 - y1, x2 - x1)
    hx1, hy1 = x2 - 30 * math.cos(a - 0.45), y2 - 30 * math.sin(a - 0.45)
    hx2, hy2 = x2 - 30 * math.cos(a + 0.45), y2 - 30 * math.sin(a + 0.45)
    return (f'<path class="s d" style="stroke:{color};stroke-width:{w}" d="M{x1} {y1} L{x2} {y2}"/>'
            f'<path class="s" style="stroke:{color};stroke-width:{w}" d="M{hx1:.0f} {hy1:.0f} L{x2} {y2} L{hx2:.0f} {hy2:.0f}"/>')


# ---------- иконки (линии со свечением) ----------
def g(x, y, s, body):
    return f'<g transform="translate({x},{y}) scale({s})">{body}</g>'


def i_bulb(x, y, s=1.0, on=True):
    glow = f'<circle cx="0" cy="-20" r="120" style="fill:{YELLOW};opacity:.12"/>' if on else ""
    col = YELLOW if on else MUTED
    return g(x, y, s, glow + f'<path class="s d" style="stroke:{col}" d="M-50 10 a60 60 0 1 1 100 0 q-20 25 -20 50 h-60 q0 -25 -20 -50z"/>'
                            f'<path class="s" style="stroke:{col}" d="M-28 80 h56 M-22 100 h44"/>')


def i_city(x, y, s=1.0, lit=True, seed=3):
    import random
    rnd = random.Random(seed)
    out, bx = "", -360
    for w, h in [(110, 300), (90, 200), (130, 400), (100, 260), (120, 340), (90, 180)]:
        out += f'<rect class="s d" x="{bx}" y="{-h}" width="{w}" height="{h}" style="stroke-width:4"/>'
        for wy in range(-h + 30, -30, 50):
            for wx in range(bx + 18, bx + w - 26, 34):
                on = lit and rnd.random() > 0.3
                out += f'<rect x="{wx}" y="{wy}" width="14" height="22" style="fill:{YELLOW if on else "rgba(255,255,255,.07)"}"/>'
        bx += w + 12
    out += f'<path class="s" d="M-400 0 H400"/>'
    return g(x, y, s, out)


def i_tower(x, y, s=1.0, color=WHITE):
    return g(x, y, s, f'<path class="s d" style="stroke:{color}" d="M-60 200 L-20 -200 L20 -200 L60 200 M-35 -60 H35 M-48 60 H48 '
                      f'M-90 -150 H90 M-70 -100 H70 M-35 -60 L48 60 M35 -60 L-48 60"/>')


def i_plug(x, y, s=1.0, color=WHITE):
    return g(x, y, s, f'<path class="s d" style="stroke:{color}" d="M-60 -40 h120 v60 a60 60 0 0 1 -120 0z M-30 -40 v-60 M30 -40 v-60 M0 80 v120"/>')


def i_battery(x, y, s=1.0, level=0.8, color=GREEN):
    return g(x, y, s, f'<rect class="s" x="-70" y="-130" width="140" height="260" rx="20"/><rect class="s" x="-30" y="-150" width="60" height="20" rx="6"/>'
                      f'<rect class="bar" x="-50" y="{110 - 220 * level}" width="100" height="{220 * level}" rx="10" style="fill:{color}"/>')


def i_flashlight(x, y, s=1.0):
    return g(x, y, s, f'<path style="fill:{YELLOW};opacity:.15" d="M-50 -90 L-180 -360 H180 L50 -90z"/>'
                      '<path class="s d" d="M-55 -90 h110 l-20 70 h-70z M-35 -20 v200 h70 v-200"/>')


def i_bottle(x, y, s=1.0):
    return g(x, y, s, f'<path class="s d" d="M-22 -150 h44 v40 q40 30 40 80 v170 q0 20 -20 20 h-84 q-20 0 -20 -20 v-170 q0 -50 40 -80z"/>'
                      f'<path style="fill:{BLUE};opacity:.35" d="M-56 20 h112 v116 q0 14 -14 14 h-84 q-14 0 -14 -14z"/>')


def i_phone(x, y, s=1.0, color=WHITE):
    return g(x, y, s, f'<rect class="s d" style="stroke:{color}" x="-70" y="-130" width="140" height="260" rx="22"/><path class="s" d="M-20 105 h40"/>')


def i_stage(x, y, s=1.0):
    return g(x, y, s, f'<path class="s d" d="M-380 -300 H380 M-380 300 H380"/>'
                      f'<path class="s d" style="stroke:{RED}" d="M-380 -300 q60 300 0 600 M-330 -300 q60 300 0 600 M380 -300 q-60 300 0 600 M330 -300 q-60 300 0 600"/>'
                      f'<path style="fill:{YELLOW};opacity:.0" d="M-80 -300 L-200 300 H200 L80 -300z"/>')


def i_tree(x, y, s=1.0):
    return g(x, y, s, f'<path class="s d" style="stroke:{GREEN}" d="M0 -220 L-130 0 H-60 L-150 140 H150 L60 0 H130 Z M0 140 V230"/>')


def sine(x, y, w=700, amp=50, periods=4, color=BLUE, grow=0.0, width=6):
    pts = []
    for i in range(141):
        t = i / 140
        a = amp * (1 + grow * t * 3)
        pts.append(f"{x + w * t:.0f},{y + a * math.sin(t * periods * 2 * math.pi):.0f}")
    return f'<polyline class="s d" points="{" ".join(pts)}" style="stroke:{color};stroke-width:{width}"/>'


def scale_balance(x, y, s=1.0, left="", right="", tilt=0):
    return g(x, y, s, f'<path class="s d" d="M0 -180 V200 M-120 200 H120"/>'
                      f'<g transform="rotate({tilt} 0 -180)"><path class="s d" d="M-300 -180 H300 M-300 -180 l-60 120 M-300 -180 l60 120 '
                      f'M300 -180 l-60 120 M300 -180 l60 120 M-370 -60 h140 M230 -60 h140"/>'
                      f'<g transform="translate(-300,-120)">{left}</g><g transform="translate(300,-120)">{right}</g></g>')


def checklist(x, y, items, gap=110, size=52):
    out = ""
    for i, (txt, ok) in enumerate(items):
        yy = y + i * gap
        col = GREEN if ok else RED
        mark = (f'<path class="s" style="stroke:{col};stroke-width:8" d="M{x} {yy - 12} l18 22 l34 -42"/>' if ok else
                f'<path class="s" style="stroke:{col};stroke-width:8" d="M{x} {yy - 30} l40 40 M{x + 40} {yy - 30} l-40 40"/>')
        out += item(mark + text(txt, x + 80, yy + 8, size, WHITE, "sans", "start", 800))
    return out


# ---------- праздник ----------
def i_cal(x, y, s=1.0, month="DEC", day="25", color=RED):
    return g(x, y, s, f'<rect x="-150" y="-170" width="300" height="320" rx="26" style="fill:{CARD};stroke:{EDGE};stroke-width:3"/>'
                      f'<path d="M-150 -104 v-40 a26 26 0 0 1 26 -26 h248 a26 26 0 0 1 26 26 v40z" style="fill:{color}"/>'
                      f'<path class="s" d="M-80 -195 v50 M80 -195 v50"/>'
                      + text(month, 0, -118, 40, "#fff", "mono", "middle", 800, 0.2)
                      + text(day, 0, 95, 170, WHITE, "sans", "middle", 800))


def i_book(x, y, s=1.0, color=WHITE):
    return g(x, y, s, f'<path class="s d" style="stroke:{color}" d="M0 -120 q-110 -40 -220 0 v260 q110 -40 220 0 q110 -40 220 0 v-260 q-110 -40 -220 0 v260"/>')


def i_sun(x, y, s=1.0, color=YELLOW):
    rays = "".join(f'<path class="s" style="stroke:{color}" d="M{110 * math.cos(a):.0f} {110 * math.sin(a):.0f} L{160 * math.cos(a):.0f} {160 * math.sin(a):.0f}"/>'
                   for a in [k * math.pi / 6 for k in range(12)])
    return g(x, y, s, f'<circle cx="0" cy="0" r="85" style="fill:{color};opacity:.15"/><circle class="s d" style="stroke:{color}" cx="0" cy="0" r="80"/>' + rays)


def i_snowflake(x, y, s=1.0, color="#cfe3ff"):
    arms = ""
    for k in range(6):
        a = k * math.pi / 3
        c, sn = math.cos(a), math.sin(a)
        arms += (f'<path class="s" style="stroke:{color};stroke-width:4" d="M0 0 L{60 * c:.0f} {60 * sn:.0f} '
                 f'M{35 * c:.0f} {35 * sn:.0f} L{35 * c + 18 * math.cos(a + 0.8):.0f} {35 * sn + 18 * math.sin(a + 0.8):.0f} '
                 f'M{35 * c:.0f} {35 * sn:.0f} L{35 * c + 18 * math.cos(a - 0.8):.0f} {35 * sn + 18 * math.sin(a - 0.8):.0f}"/>')
    return g(x, y, s, arms)


def snowfall(n=14, seed=7, area=(0, 0, 1000, 1000)):
    import random
    r = random.Random(seed)
    return "".join(i_snowflake(r.uniform(area[0], area[2]), r.uniform(area[1], area[3]), r.uniform(0.15, 0.35), "rgba(200,220,255,.35)")
                   for _ in range(n))


def i_hat(x, y, s=1.0):
    return g(x, y, s, f'<path class="s d" style="stroke:{RED}" d="M-150 60 Q-60 -200 120 -150 Q60 -100 90 60"/>'
                      f'<rect class="s" x="-180" y="50" width="300" height="60" rx="30"/><circle class="s" cx="140" cy="-150" r="30"/>')


def i_bottle_soda(x, y, s=1.0, color=RED):
    return g(x, y, s, f'<path class="s d" style="stroke:{color}" d="M-25 -200 h50 v60 q45 40 45 100 q-20 50 0 100 q0 70 -20 130 h-100 q-20 -60 -20 -130 q20 -50 0 -100 q0 -60 45 -100z"/>')


def i_rocket(x, y, s=1.0, r=-30):
    return g(x, y, s, f'<g transform="rotate({r})"><path class="s d" d="M0 -220 q80 90 60 260 h-120 q-20 -170 60 -260z"/>'
                      f'<circle class="s" cx="0" cy="-60" r="34" style="stroke:{BLUE}"/>'
                      f'<path class="s" d="M-60 0 l-60 90 l60 -20 M60 0 l60 90 l-60 -20"/>'
                      f'<path style="fill:{YELLOW};opacity:.8" d="M-40 50 q40 160 80 0z"/></g>')


def i_bell(x, y, s=1.0, color=YELLOW):
    return g(x, y, s, f'<path class="s d" style="stroke:{color}" d="M-110 80 q20 -20 25 -110 q5 -90 85 -100 q80 10 85 100 q5 90 25 110z"/>'
                      f'<circle class="s" style="stroke:{color}" cx="0" cy="105" r="22"/><path class="s" style="stroke:{color}" d="M0 -130 v-30"/>')


def i_music(x, y, s=1.0, color=GREEN):
    return g(x, y, s, f'<path class="s d" style="stroke:{color}" d="M-40 60 v-170 l120 -30 v170"/>'
                      f'<circle class="s" style="stroke:{color}" cx="-65" cy="60" r="26"/><circle class="s" style="stroke:{color}" cx="55" cy="30" r="26"/>')
