"""Собирает рисованный анимированный рилс 9:16 из сценария.

Сценарий — Python-файл со списком SCENES: [{"text": "фраза для голоса", "svg": "<рисунок>"}].
Необязательно: VOICE = "af_heart" (голос Kokoro), SPEED = 1.08; у сцены "bg" — цвет фона.
Каждая сцена: голос (Kokoro) + рисунок, который прорисовывается на глазах + субтитры сверху.
После появления рисунок слегка «дышит» (линии дрожат, как в рисованной анимации).

    python3 tools/reel.py reels/2026-11-16-advent-nuts/scenes.py
Результат: output/<имя папки>.mp4 (без музыки; звук добавляет tools/sound.py)
"""
import base64
import html
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1920
KOKORO = ROOT / "assets/voices/kokoro"
PAUSE = 0.3          # пауза после каждой фразы, сек
WORDS_PER_CAPTION = 5
FPS_INTRO = 24       # кадров/с, пока рисунок прорисовывается
INTRO = 1.0          # сколько секунд длится прорисовка (не больше 60% сцены)
BOIL = 0.25          # как часто «дрожат» линии, сек
FONTS = [base64.b64encode((ROOT / "assets/fonts" / f).read_bytes()).decode()
         for f in ("Caveat-Bold.woff2", "PTSerif-Regular.woff2")]

PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Hand;src:url(data:font/woff2;base64,%(hand)s)}
@font-face{font-family:Cap;src:url(data:font/woff2;base64,%(cap_font)s)}
html,body{margin:0;width:%(w)dpx;height:%(h)dpx;background:%(bg)s;overflow:hidden}
#cap{position:absolute;top:300px;left:90px;right:90px;text-align:center;font:44px/1.25 Cap,serif;color:#111}
svg{position:absolute;left:40px;top:480px;width:1000px;height:1000px}
.hand{font-family:Hand,cursive;fill:#111}
.red{fill:#d7263d}.blue{fill:#2f6fdb}.green{fill:#1f9d55}.purple{fill:#7b3fe4}.orange{fill:#f08a00}.pink{fill:#e0457b}
.ln{fill:none;stroke:#111;stroke-width:7;stroke-linecap:round;stroke-linejoin:round}
.pop{transform-box:fill-box;transform-origin:center}
.dark #cap{color:#f4f4f4}.dark .hand{fill:#f4f4f4}.dark .ln{stroke:#f4f4f4}.dark .red{fill:#ff5a6e}
.hand.blue{fill:#2f6fdb}.hand.green{fill:#1f9d55}.hand.purple{fill:#7b3fe4}.hand.orange{fill:#f08a00}.hand.pink{fill:#e0457b}.dark .hand.blue{fill:#7fb0ff}.dark .hand.pink{fill:#ff7fae}.dark .hand.purple{fill:#b79bff}.dark .hand.orange{fill:#ffaa33}
</style></head><body class="%(mode)s"><div id="cap"></div>
<svg viewBox="0 0 1000 1000"><defs><filter id="wob"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="1"/>
<feDisplacementMap in="SourceGraphic" scale="9"/></filter></defs><g id="art" filter="url(#wob)">%(svg)s</g></svg>
<script>
const SHAPES = ['path','rect','circle','ellipse','line','polyline','polygon'];
function setup(win) {
  const art = document.getElementById('art');
  const items = [];
  (function walk(n) {
    for (const c of n.children) {
      if (c.classList.contains('pop')) items.push(c);
      else if (SHAPES.includes(c.tagName)) items.push(c);
      else if (c.tagName === 'text') items.push(c);
      else walk(c);
    }
  })(art);
  const n = items.length, d = Math.min(0.45, win * 0.6);
  items.forEach((e, i) => {
    const start = n > 1 ? (i / (n - 1)) * (win - d) : 0;
    const opt = {duration: d * 1000, delay: start * 1000, fill: 'both', easing: 'ease-out'};
    if (e.classList.contains('pop')) {
      e.animate([{opacity: 0, transform: 'scale(0.3)'}, {opacity: 1, transform: 'scale(1.12)', offset: 0.7},
                 {opacity: 1, transform: 'scale(1)'}], opt);
    } else if (e.classList.contains('ln') && e.getTotalLength) {
      const L = e.getTotalLength() + 2;
      e.style.strokeDasharray = L;
      e.animate([{strokeDashoffset: L}, {strokeDashoffset: 0}], opt);
      if (getComputedStyle(e).fill !== 'none')
        e.animate([{fillOpacity: 0}, {fillOpacity: 1}], {...opt, delay: (start + d * 0.6) * 1000});
    } else {
      e.animate([{opacity: 0}, {opacity: 1}], opt);
    }
  });
}
function frame(t, cap, seed) {
  document.getAnimations().forEach(a => { a.currentTime = t * 1000; });
  document.getElementById('cap').innerHTML = cap;
  document.getElementById('turb').setAttribute('seed', seed);
}
</script></body></html>"""


def mode(bg: str) -> str:
    """тёмный фон -> светлый текст и линии"""
    h = bg.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "dark" if 0.299 * r + 0.587 * g + 0.114 * b < 110 else ""


GOOGLE = ["#4285F4", "#EA4335", "#FBBC05", "#4285F4", "#34A853", "#EA4335"]


def cap_html(text: str) -> str:
    """субтитр в HTML; слово google — в цветах Google"""
    import re
    def paint(m):
        w = m.group(0)
        return "".join(f'<span style="color:{GOOGLE[i % 6]}">{c}</span>' for i, c in enumerate(w[:6])) + w[6:]
    return re.sub(r"(?i)google\w*", paint, html.escape(text))


def chunks(text: str):
    words = text.split()
    return [" ".join(words[i:i + WORDS_PER_CAPTION]) for i in range(0, len(words), WORDS_PER_CAPTION)]


def main(spec_path: str) -> None:
    spec_path = Path(spec_path).resolve()
    name = spec_path.parent.name
    s = importlib.util.spec_from_file_location("scenes", spec_path)
    mod = importlib.util.module_from_spec(s)
    s.loader.exec_module(mod)
    voice = getattr(mod, "VOICE", "af_heart")
    speed = getattr(mod, "SPEED", 1.08)

    work = ROOT / "output" / f".work-{name}"
    work.mkdir(parents=True, exist_ok=True)
    for old in work.glob("s*.png"):
        old.unlink()

    from kokoro_onnx import Kokoro
    from playwright.sync_api import sync_playwright
    tts = Kokoro(str(KOKORO / "kokoro-v1.0.onnx"), str(KOKORO / "voices-v1.0.bin"))
    lang = "en-gb" if voice.startswith("b") else "en-us"

    frames, audio, scenes, t0 = [], [], [], 0.0
    with sync_playwright() as p:
        page = p.chromium.launch(executable_path="/opt/pw-browsers/chromium",
                                 args=["--no-sandbox"]).new_page(viewport={"width": W, "height": H})
        for i, sc in enumerate(mod.SCENES):
            if getattr(mod, "NO_VOICE", False):           # без голоса: тишина заданной длины, без субтитров
                sr = 24000
                a = np.zeros(int(sr * sc.get("dur", 4.0)), np.float32)
            else:
                v = sc.get("voice", voice)                  # у сцены может быть свой голос (диалоги)
                a, sr = tts.create(sc["text"], voice=v, speed=sc.get("speed", speed),
                                   lang="en-gb" if v.startswith("b") else "en-us")
            a = np.concatenate([a, np.zeros(int(sr * PAUSE), np.float32)])
            audio.append(a)
            dur = len(a) / sr
            scenes.append({"start": round(t0, 3), "dur": round(dur, 3)})
            t0 += dur

            parts = [""] if getattr(mod, "NO_VOICE", False) else chunks(sc["text"])
            total = max(1, sum(len(c) for c in parts))
            bounds = np.cumsum([dur * max(1, len(c)) / max(1, sum(max(1, len(x)) for x in parts)) for c in parts])

            def cap_at(t):
                return int(min(np.searchsorted(bounds, t, side="right"), len(parts) - 1))

            page.set_content(PAGE % dict(hand=FONTS[0], cap_font=FONTS[1], w=W, h=H, svg=sc["svg"], bg=sc.get("bg", "#fff"), mode=mode(sc.get("bg", "#fff"))))
            page.evaluate("document.fonts.ready")
            intro = min(INTRO, dur * 0.6)
            page.evaluate(f"setup({intro})")

            shots = {}

            def shot(t, cap, seed, key=None):
                if key is not None and key in shots:
                    return shots[key]
                png = work / f"s{i:02}_{len(shots):03}.png"
                page.evaluate("([t, c, s]) => frame(t, c, s)", [t, cap_html(parts[cap]), seed])
                page.screenshot(path=str(png))
                shots[key if key is not None else ("intro", t)] = png
                return png

            t = 0.0
            step = 1 / FPS_INTRO
            while t < intro:                                   # прорисовка
                frames.append((shot(t, cap_at(t), 1), step))
                t += step
            k = 0
            while t < dur - 1e-6:                              # «дыхание» линий + смена субтитров
                d = min(BOIL, dur - t)
                c = cap_at(t)
                seed = 1 + k % 3
                frames.append((shot(100.0, c, seed, key=(c, seed)), d))
                t += d
                k += 1
            print(f"сцена {i + 1}/{len(mod.SCENES)}: {dur:.1f} c, {len(shots)} картинок")

    (work / "scenes.json").write_text(json.dumps(scenes))
    lst = work / "frames.txt"
    lst.write_text("".join(f"file '{f}'\nduration {d:.4f}\n" for f, d in frames) + f"file '{frames[-1][0]}'\n")
    voice_wav = work / "voice.wav"
    sf.write(voice_wav, np.concatenate(audio), sr)

    out = ROOT / "output" / f"{name}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(voice_wav),
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", "-movflags", "+faststart", str(out)], check=True)
    print("Готово:", out)


if __name__ == "__main__":
    main(sys.argv[1])
