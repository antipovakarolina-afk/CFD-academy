"""Ретро-фэнтези аниме (90-е): полноэкранные сцены. Координаты: x -40..1040, y -480..1440 (весь кадр 1080×1920)."""
import math
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from doodles import mv  # noqa

X0, Y0, X1, Y1 = -40, -480, 1040, 1440
DEFS = '''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b0726"/><stop offset=".55" stop-color="#2b1055"/><stop offset="1" stop-color="#7a3e9d"/></linearGradient>
<linearGradient id="skyred" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#12030f"/><stop offset=".6" stop-color="#4a0d2e"/><stop offset="1" stop-color="#b8325a"/></linearGradient>
<linearGradient id="teal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05121f"/><stop offset="1" stop-color="#1b4d5c"/></linearGradient>
<radialGradient id="moon"><stop offset="0" stop-color="#fffbe6"/><stop offset=".7" stop-color="#f3e3b5"/><stop offset="1" stop-color="#d9c08a"/></radialGradient>
<radialGradient id="halo"><stop offset="0" stop-color="#fff2c4" stop-opacity=".55"/><stop offset="1" stop-color="#fff2c4" stop-opacity="0"/></radialGradient>
<radialGradient id="redhalo"><stop offset="0" stop-color="#ff3c6e" stop-opacity=".6"/><stop offset="1" stop-color="#ff3c6e" stop-opacity="0"/></radialGradient>
<radialGradient id="glowp"><stop offset="0" stop-color="#d9a6ff" stop-opacity=".9"/><stop offset="1" stop-color="#b06bff" stop-opacity="0"/></radialGradient>
<filter id="blur"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="softglow"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>'''


def sky(grad="sky"):
    return DEFS + f'<rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{Y1 - Y0}" style="fill:url(#{grad})"/>'


def stars(n=80, seed=1, ymax=700):
    r = random.Random(seed)
    out = ""
    for k in range(n):
        x, y, rr = r.uniform(X0, X1), r.uniform(Y0, ymax), r.uniform(1.2, 3.6)
        out += mv(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rr:.1f}" style="fill:#fff6e0"/>', "pulse", a=0.8, p=0.6 + (k % 5) * 0.25, d=0.05 * (k % 7))
    return out


def moon(x, y, r, red=False):
    h = "redhalo" if red else "halo"
    body = (f'<circle cx="{x}" cy="{y}" r="{r * 2.4}" style="fill:url(#{h})"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:{"#e8486f" if red else "url(#moon)"}"/>'
            f'<circle cx="{x - r * .3}" cy="{y - r * .2}" r="{r * .16}" style="fill:#000;opacity:.06"/>'
            f'<circle cx="{x + r * .35}" cy="{y + r * .3}" r="{r * .22}" style="fill:#000;opacity:.05"/>')
    return body


def clouds(y, seed=2, color="#3a1f63", op=0.85, drift=120):
    r = random.Random(seed)
    out = ""
    for k in range(5):
        cx, w = r.uniform(X0, X1), r.uniform(260, 520)
        c = (f'<ellipse cx="{cx:.0f}" cy="{y + r.uniform(-40, 40):.0f}" rx="{w / 2:.0f}" ry="{w / 7:.0f}" style="fill:{color};opacity:{op}"/>'
             f'<ellipse cx="{cx + w * .15:.0f}" cy="{y - w / 12:.0f}" rx="{w / 3.2:.0f}" ry="{w / 8:.0f}" style="fill:{color};opacity:{op}"/>')
        out += mv(c, "move", x=drift * (1 if k % 2 else -1), d=0)
    return out


def mountains(y, color="#140a2b", seed=3, h=380):
    r = random.Random(seed)
    pts, x = [f"{X0},{Y1}"], X0
    while x < X1 + 80:
        pts.append(f"{x:.0f},{y - r.uniform(0, h):.0f}")
        x += r.uniform(90, 200)
    pts.append(f"{X1 + 80},{Y1}")
    return f'<polygon points="{" ".join(pts)}" style="fill:{color}"/>'


def castle(x, y, s=1.0, color="#0a0518", windows=True):
    parts = [(-160, -260, 70, 300), (-60, -420, 80, 460), (40, -330, 70, 370), (130, -230, 60, 270)]
    out = ""
    for dx, dy, w, h in parts:
        out += f'<rect x="{dx}" y="{dy}" width="{w}" height="{h}" style="fill:{color}"/>'
        out += f'<polygon points="{dx - 12},{dy} {dx + w / 2},{dy - w * 1.3} {dx + w + 12},{dy}" style="fill:{color}"/>'
        if windows:
            out += f'<rect x="{dx + w / 2 - 7}" y="{dy + 40}" width="14" height="22" rx="7" style="fill:#ffcf6e"/>'
    out += f'<rect x="-200" y="20" width="400" height="40" style="fill:{color}"/>'
    return f'<g transform="translate({x},{y}) scale({s})">{out}</g>'


def cliff(x, y, w=700, color="#0d0620"):
    return f'<path d="M{x - w / 2} {Y1} L{x - w / 2} {y + 60} Q{x - w / 4} {y - 20} {x} {y} Q{x + w / 4} {y + 10} {x + w / 2} {y + 80} L{x + w / 2} {Y1} Z" style="fill:{color}"/>'


def hooded(x, y, s=1.0, cape="#1a0f33", trim="#7f5af0", eyes="#ff3c8e", wind=True):
    """свой персонаж: фигура в капюшоне со светящимися глазами (не участник группы)"""
    capeflap = ('<path d="M-60 -120 Q-180 40 -240 330 Q-120 300 -40 340 Z" style="fill:%s"/>' % cape)
    body = (f'<path d="M-90 -170 Q0 -260 90 -170 L130 340 Q0 370 -130 340 Z" style="fill:{cape}"/>'
            f'<path d="M-90 -170 Q0 -260 90 -170 L130 340 Q0 370 -130 340 Z" style="fill:none;stroke:{trim};stroke-width:5"/>'
            f'<path d="M-70 -190 Q0 -300 70 -190 Q70 -100 0 -80 Q-70 -100 -70 -190 Z" style="fill:#07030f"/>'
            f'<ellipse cx="-24" cy="-160" rx="14" ry="6" style="fill:{eyes}" filter="url(#softglow)"/>'
            f'<ellipse cx="24" cy="-160" rx="14" ry="6" style="fill:{eyes}" filter="url(#softglow)"/>'
            f'<path d="M-6 -60 h12 v380 h-12z" style="fill:{trim};opacity:.6"/>')
    cf = mv(capeflap, "wiggle", a=6, p=0.7) if wind else capeflap
    return f'<g transform="translate({x},{y}) scale({s})">{cf}{body}</g>'


def anime_eye(x, y, s=1.0, iris="#b06bff", sigil=True):
    sig = ""
    if sigil:
        sig = mv(f'<g><circle cx="0" cy="0" r="62" style="fill:none;stroke:#ffe9a8;stroke-width:3"/>'
                 + "".join(f'<path d="M0 -62 L0 -40" transform="rotate({k * 45})" style="stroke:#ffe9a8;stroke-width:4"/>' for k in range(8))
                 + '<polygon points="0,-40 35,20 -35,20" style="fill:none;stroke:#ffe9a8;stroke-width:3"/></g>', "spin", p=6)
    return (f'<g transform="translate({x},{y}) scale({s})">'
            '<path d="M-360 0 Q0 -230 360 0 Q0 200 -360 0 Z" style="fill:#f3e9ff"/>'
            f'<circle cx="0" cy="0" r="150" style="fill:{iris}"/><circle cx="0" cy="0" r="150" style="fill:url(#glowp);opacity:.6"/>'
            '<circle cx="0" cy="0" r="70" style="fill:#120624"/>' + sig +
            '<ellipse cx="-55" cy="-60" rx="38" ry="26" style="fill:#fff"/><circle cx="60" cy="50" r="14" style="fill:#fff"/>'
            '<path d="M-380 0 Q0 -260 380 0" style="fill:none;stroke:#07030f;stroke-width:26;stroke-linecap:round"/>'
            '<path d="M-330 -60 l-60 -50 M-250 -110 l-40 -70 M330 -60 l60 -50" style="stroke:#07030f;stroke-width:12;stroke-linecap:round"/>'
            '</g>')


def magic_circle(x, y, r=320, color="#ffd27a"):
    ring = "".join(f'<text x="0" y="{-r + 52}" font-size="44" text-anchor="middle" transform="rotate({k * 22.5})" '
                   f'style="fill:{color};font-family:serif">{"ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊ"[k]}</text>' for k in range(16))
    outer = mv(f'<g transform="translate({x},{y})"><circle r="{r}" style="fill:none;stroke:{color};stroke-width:6"/>'
               f'<circle r="{r - 70}" style="fill:none;stroke:{color};stroke-width:3"/>{ring}</g>', "spin", p=10)
    inner = mv(f'<g transform="translate({x},{y})">'
               + "".join(f'<polygon points="0,{-r * .62} {r * .54},{r * .31} {-r * .54},{r * .31}" transform="rotate({k * 60})" '
                         f'style="fill:none;stroke:{color};stroke-width:4"/>' for k in range(2))
               + f'<circle r="{r * .22}" style="fill:{color};opacity:.25"/></g>', "spin", p=-6)
    glow = mv(f'<circle cx="{x}" cy="{y}" r="{r * 1.1}" style="fill:url(#glowp);opacity:.55"/>', "pulse", a=0.12, p=0.5)
    return glow + f'<g filter="url(#softglow)">{outer}{inner}</g>'


def crystal(x, y, s=1.0, color="#7fe7ff"):
    return (f'<g transform="translate({x},{y}) scale({s})" filter="url(#softglow)">'
            f'<polygon points="0,-180 70,-40 40,160 -40,160 -70,-40" style="fill:{color};opacity:.85"/>'
            '<polygon points="0,-180 70,-40 0,0" style="fill:#fff;opacity:.45"/><polygon points="0,0 40,160 -40,160" style="fill:#0b3a52;opacity:.35"/></g>')


def fireflies(n=24, seed=4, color="#ffe9a8", area=(X0, 200, X1, 1300)):
    r = random.Random(seed)
    return "".join(mv(f'<circle cx="{r.uniform(area[0], area[2]):.0f}" cy="{r.uniform(area[1], area[3]):.0f}" r="{r.uniform(4, 9):.0f}" '
                      f'style="fill:{color}" filter="url(#softglow)"/>', "rise", a=r.uniform(80, 200), x=r.uniform(-40, 40), p=r.uniform(1.6, 3.2), d=r.uniform(0, 2))
                   for _ in range(n))


def rain(n=70, seed=5):
    r = random.Random(seed)
    return "".join(mv(f'<path d="M{r.uniform(X0, X1 + 300):.0f} {r.uniform(Y0 - 300, Y1):.0f} l-40 120" style="stroke:#9fb8ff;stroke-width:3;opacity:.5"/>',
                      "travel", x=-160, y=480, p=r.uniform(0.35, 0.6), d=r.uniform(0, .6)) for _ in range(n))


def lightning(x, y):
    return mv(f'<path d="M{x} {y} l-60 220 l70 -10 l-90 260 l160 -320 l-80 10 l60 -160z" style="fill:#fff7d6" filter="url(#softglow)"/>', "pulse", a=0.3, p=0.12)


def dragon(x, y, s=1.0, eyes="#ff3c6e"):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            '<path d="M-420 60 Q-200 -220 0 -60 Q200 -220 420 60 Q260 -10 120 40 Q60 -20 0 30 Q-60 -20 -120 40 Q-260 -10 -420 60z" style="fill:#08030f;opacity:.92"/>'
            '<path d="M-40 -60 Q0 -140 40 -60 Q30 40 0 60 Q-30 40 -40 -60z" style="fill:#08030f"/>'
            f'<ellipse cx="-16" cy="-40" rx="12" ry="5" style="fill:{eyes}" filter="url(#softglow)"/><ellipse cx="16" cy="-40" rx="12" ry="5" style="fill:{eyes}" filter="url(#softglow)"/></g>')


def bridge(y):
    planks = "".join(f'<rect x="{X0 + k * 60}" y="{y}" width="50" height="22" style="fill:#120a24"/>' for k in range(19))
    return planks + f'<path d="M{X0} {y - 60} Q500 {y + 40} {X1} {y - 60}" style="fill:none;stroke:#120a24;stroke-width:6"/>'


def speedlines(n=40, seed=6, color="#ffffff"):
    r = random.Random(seed)
    out = ""
    for _ in range(n):
        a = r.uniform(0, 6.28)
        r1, r2 = r.uniform(380, 520), r.uniform(900, 1300)
        out += (f'<path d="M{500 + r1 * math.cos(a):.0f} {480 + r1 * math.sin(a):.0f} L{500 + r2 * math.cos(a):.0f} {480 + r2 * math.sin(a):.0f}" '
                f'style="stroke:{color};stroke-width:{r.uniform(2, 7):.0f};opacity:.35"/>')
    return mv(out, "pulse", a=0.04, p=0.15)


def petals(n=40, seed=7, color="#ff8fc7"):
    r = random.Random(seed)
    return "".join(mv(f'<ellipse cx="{r.uniform(X0, X1):.0f}" cy="{r.uniform(600, Y1):.0f}" rx="10" ry="5" style="fill:{color};opacity:.85" '
                      f'transform="rotate({r.uniform(0, 180):.0f})"/>', "rise", a=r.uniform(300, 700), x=r.uniform(-120, 120), p=r.uniform(2, 3.6), d=r.uniform(0, 2))
                   for _ in range(n))


def title(text, y=1150, size=120, color="#f5e6ff", sub=""):
    t = (f'<text x="500" y="{y}" font-size="{size}" text-anchor="middle" '
         f'style="font-family:Georgia,serif;letter-spacing:.18em;fill:{color};font-weight:700" filter="url(#softglow)">{text}</text>')
    if sub:
        t += f'<text x="500" y="{y + 80}" font-size="40" text-anchor="middle" style="font-family:Georgia,serif;letter-spacing:.4em;fill:#c9a7ff">{sub}</text>'
    return mv(t, "appear", d=0.6)
