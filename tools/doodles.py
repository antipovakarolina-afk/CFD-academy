"""Простые рисунки линией для рилсов (SVG, поле 1000×1000)."""


def g(x, y, s, body):
    return f'<g transform="translate({x},{y}) scale({s})">{body}</g>'


def hand(text, x=500, y=500, size=110, cls="hand", rot=0):
    return (f'<text class="{cls}" x="{x}" y="{y}" font-size="{size}" text-anchor="middle" '
            f'transform="rotate({rot} {x} {y})">{text}</text>')


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
