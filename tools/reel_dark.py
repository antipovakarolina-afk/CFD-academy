"""Тёмный стиль «инфографика»: сборка рилса 9:16.

Сценарий — scenes.py со списком SCENES: [{"title": "ЗАГОЛОВОК", "sub": "подзаголовок",
"text": "фраза для голоса, *выделенные* слова в звёздочках", "svg": "<графика из tools/dark.py>"}].
Необязательно: VOICE, SPEED.

    python3 tools/reel_dark.py reels/<папка>/scenes.py
Результат: output/<папка>.mp4 (звук добавляет tools/sound.py)
"""
import base64
import html
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1920
KOKORO = ROOT / "assets/voices/kokoro"
PAUSE = 0.25
FPS = 24
INTRO = 1.2
WORDS = 3            # слов в субтитре
F = {k: base64.b64encode((ROOT / "assets/fonts" / f).read_bytes()).decode() for k, f in
     {"sans": "Inter-ExtraBold.woff2", "sans6": "Inter-SemiBold.woff2", "mono": "JetBrainsMono-Medium.woff2",
      "mono8": "JetBrainsMono-ExtraBold.woff2"}.items()}

PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Sans;font-weight:800;src:url(data:font/woff2;base64,%(sans)s)}
@font-face{font-family:Sans;font-weight:600;src:url(data:font/woff2;base64,%(sans6)s)}
@font-face{font-family:Mono;font-weight:500;src:url(data:font/woff2;base64,%(mono)s)}
@font-face{font-family:Mono;font-weight:800;src:url(data:font/woff2;base64,%(mono8)s)}
html,body{margin:0;width:1080px;height:1920px;overflow:hidden;
 background:radial-gradient(ellipse at 50%% 38%%,#16233f 0%%,#0b1222 55%%,#05080f 100%%)}
#grid{position:absolute;inset:0}
#top{position:absolute;top:110px;width:100%%;text-align:center;font:500 24px Mono;letter-spacing:.3em;color:#7f93b8}
#top b{display:block;width:46px;height:4px;margin:18px auto 0;background:%(acc)s;border-radius:2px}
#title{position:absolute;top:205px;left:60px;right:60px;text-align:center;font:800 66px/1.05 Sans;color:#fff;letter-spacing:.01em}
#sub{position:absolute;top:290px;width:100%%;text-align:center;font:500 26px Mono;letter-spacing:.2em;color:%(acc)s}
svg#art{position:absolute;left:40px;top:390px;width:1000px;height:1000px;overflow:visible}
#cap{position:absolute;top:1450px;left:70px;right:70px;text-align:center;font:800 78px/1.1 Sans;color:#fff;
 text-shadow:0 0 24px rgba(0,0,0,.6)}
#cap .h{color:#ffc845}
.s{fill:none;stroke:#e8eefc;stroke-width:5;stroke-linecap:round;stroke-linejoin:round;filter:url(#glow)}
.in{transform-box:fill-box;transform-origin:center}
.bar{transform-box:fill-box;transform-origin:bottom}
</style></head><body>
<svg id="grid" width="1080" height="1920"><defs><pattern id="p" width="60" height="60" patternUnits="userSpaceOnUse">
<path d="M60 0H0V60" fill="none" stroke="rgba(120,160,255,.07)" stroke-width="1.5"/></pattern></defs>
<rect width="1080" height="1920" fill="url(#p)"/></svg>
<div id="top">WHAT DID I GOOGLE TODAY<b></b></div><div id="title">%(title)s</div><div id="sub">%(sub)s</div>
<svg id="art" viewBox="0 0 1000 1000"><defs><filter id="glow" filterUnits="userSpaceOnUse" x="-200" y="-200" width="1400" height="1400">
<feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<g id="root">%(svg)s</g></svg>
<div id="cap"></div>
<script>
let counters = [];
function setup(win) {
  const head = ['title', 'sub'].map(id => document.getElementById(id));
  head.forEach((e, i) => e.animate([{opacity: 0, transform: 'translateY(-20px)'}, {opacity: 1, transform: 'none'}],
    {duration: 350, delay: i * 120, fill: 'both', easing: 'ease-out'}));
  const items = [...document.querySelectorAll('#root .in')];
  const n = items.length, d = 0.45;
  items.forEach((e, i) => {
    const st = 0.15 + (n > 1 ? i / (n - 1) * (win - d - 0.15) : 0);
    e.animate([{opacity: 0, transform: 'translateY(40px) scale(.96)'}, {opacity: 1, transform: 'none'}],
      {duration: d * 1000, delay: st * 1000, fill: 'both', easing: 'cubic-bezier(.2,.8,.2,1)'});
    e.dataset.st = st;
  });
  document.querySelectorAll('#root .d').forEach(e => {
    if (!e.getTotalLength) return;
    const L = e.getTotalLength() + 2, p = e.closest('.in');
    const st = p ? parseFloat(p.dataset.st) : 0.1;
    e.style.strokeDasharray = L;
    e.animate([{strokeDashoffset: L}, {strokeDashoffset: 0}], {duration: 700, delay: st * 1000, fill: 'both', easing: 'ease-in-out'});
  });
  document.querySelectorAll('#root .bar').forEach(e => {
    const p = e.closest('.in'); const st = p ? parseFloat(p.dataset.st) : 0.2;
    e.animate([{transform: 'scaleY(0)'}, {transform: 'scaleY(1)'}], {duration: 700, delay: (st + 0.1) * 1000, fill: 'both', easing: 'cubic-bezier(.2,.8,.2,1)'});
  });
  counters = [...document.querySelectorAll('#root .count')].map(e => {
    const p = e.closest('.in'); return {e, st: (p ? parseFloat(p.dataset.st) : 0.1) + 0.1};
  });
}
function fmt(v, dec) { if (dec < 0) return String(Math.round(v)); return v.toLocaleString('en-US', {minimumFractionDigits: dec, maximumFractionDigits: dec}); }
function frame(t, cap) {
  document.getAnimations().forEach(a => { a.currentTime = t * 1000; });
  counters.forEach(({e, st}) => {
    const to = parseFloat(e.dataset.to), fr = parseFloat(e.dataset.from), dec = parseInt(e.dataset.dec);
    let k = Math.min(1, Math.max(0, (t - st) / 1.0)); k = 1 - Math.pow(1 - k, 3);
    e.textContent = e.dataset.prefix + fmt(fr + (to - fr) * k, dec) + e.dataset.suffix;
  });
  document.getElementById('cap').innerHTML = cap;
}
</script></body></html>"""


def words_of(text):
    return text.split()


def cap_html(words):
    out = []
    for w in words:
        if w.startswith("*") or w.rstrip(".,!?:;").endswith("*"):
            out.append(f'<span class="h">{html.escape(w.replace("*", ""))}</span>')
        else:
            out.append(html.escape(w))
    return " ".join(out)


def voiced_span(a, sr):
    env = np.convolve(np.abs(a), np.ones(int(sr * 0.02)) / int(sr * 0.02), mode="same")
    idx = np.where(env > env.max() * 0.06)[0]
    return (idx[0] / sr, idx[-1] / sr) if len(idx) else (0, len(a) / sr)


def main(spec_path):
    spec_path = Path(spec_path).resolve()
    name = spec_path.parent.name
    s = importlib.util.spec_from_file_location("scenes", spec_path)
    mod = importlib.util.module_from_spec(s)
    s.loader.exec_module(mod)
    voice, speed = getattr(mod, "VOICE", "af_heart"), getattr(mod, "SPEED", 1.12)
    acc = getattr(mod, "ACCENT", "#ffc845")

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
            spoken = sc["text"].replace("*", "")
            a, sr = tts.create(spoken, voice=voice, speed=speed, lang=lang)
            a = np.concatenate([a, np.zeros(int(sr * PAUSE), np.float32)])
            audio.append(a)
            dur = len(a) / sr
            scenes.append({"start": round(t0, 3), "dur": round(dur, 3)})
            t0 += dur

            # субтитры: группы по WORDS слов, время — по длине слов внутри звучащего участка
            ws = words_of(sc["text"])
            groups = [ws[k:k + WORDS] for k in range(0, len(ws), WORDS)]
            v0, v1 = voiced_span(a, sr)
            lens = np.array([sum(len(w) + 1 for w in gr) for gr in groups], float)
            starts = v0 + np.concatenate([[0], np.cumsum(lens)[:-1]]) / lens.sum() * (v1 - v0)

            def cap_at(t):
                return int(max(0, np.searchsorted(starts, t, side="right") - 1))

            page.set_content(PAGE % dict(F, acc=acc, title=html.escape(sc.get("title", "")),
                                         sub=html.escape(sc.get("sub", "")).upper(), svg=sc["svg"]))
            page.evaluate("document.fonts.ready")
            page.evaluate(f"setup({INTRO})")
            anim_end = min(dur, INTRO + 1.4)       # пока идут анимации и счётчики
            shots = {}

            def shot(t, c, key=None):
                if key is not None and key in shots:
                    return shots[key]
                png = work / f"s{i:02}_{len(shots):03}.png"
                page.evaluate("([t, c]) => frame(t, c)", [t, cap_html(groups[c])])
                page.screenshot(path=str(png))
                shots[key if key is not None else ("t", round(t, 3))] = png
                return png

            t = 0.0
            while t < anim_end - 1e-6:
                frames.append((shot(t, cap_at(t)), 1 / FPS))
                t += 1 / FPS
            # дальше картинка стоит, меняются только субтитры
            bounds = sorted(set([t] + [b for b in starts if b > t] + [dur]))
            for b0, b1 in zip(bounds[:-1], bounds[1:]):
                if b1 - b0 > 1e-4:
                    frames.append((shot(99.0, cap_at(b0), key=("cap", cap_at(b0))), b1 - b0))
            print(f"сцена {i + 1}/{len(mod.SCENES)}: {dur:.1f} c, {len(shots)} кадров")

    (work / "scenes.json").write_text(json.dumps(scenes))
    lst = work / "frames.txt"
    lst.write_text("".join(f"file '{f}'\nduration {d:.4f}\n" for f, d in frames) + f"file '{frames[-1][0]}'\n")
    sf.write(work / "voice.wav", np.concatenate(audio), sr)
    out = ROOT / "output" / f"{name}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(work / "voice.wav"),
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "19", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", "-movflags", "+faststart", str(out)], check=True)
    print("Готово:", out)


if __name__ == "__main__":
    main(sys.argv[1])
