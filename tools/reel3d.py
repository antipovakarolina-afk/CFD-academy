"""3D-версия рисованного стиля: пастельный фон, объёмные «игрушечные» объекты (three.js),
надписи от руки и субтитры поверх. Объекты выпрыгивают, покачиваются и медленно вращаются.

Сценарий — scenes.py: SCENES = [dict(bg, text, objs=[O(...)...], labels=[L(...)...], bubble="текст"|None)].
Координаты как в 2D: поле 1000×1000 (x 0..1000, y 0..1000 — центральная часть кадра).

    python3 tools/reel3d.py reels/<папка>/scenes.py
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
FPS = 24
PAUSE = 0.3
WORDS = 5
PX = 304.0                       # пикселей на 1 единицу 3D-мира в плоскости z=0
KOKORO = ROOT / "assets/voices/kokoro"
FONT_HAND = base64.b64encode((ROOT / "assets/fonts/Caveat-Bold.woff2").read_bytes()).decode()
FONT_CAP = base64.b64encode((ROOT / "assets/fonts/PTSerif-Regular.woff2").read_bytes()).decode()
GOOGLE = ["#4285F4", "#EA4335", "#FBBC05", "#4285F4", "#34A853", "#EA4335"]


def world(bx, by):
    return (40 + bx - W / 2) / PX, (H / 2 - (480 + by)) / PX


def O(model, bx, by, s=1.0, args=(), r=(0, 0, 0), spin=1.0, z=0.0):
    x, y = world(bx, by)
    return dict(m=model, a=list(args), p=[x, y, z], s=s, r=list(r), spin=spin)


def L(text, bx, by, size=110, color="#111", rot=0, google=False):
    return dict(t=text, x=40 + bx, y=480 + by, size=size, color=color, rot=rot, google=google)


PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Hand;src:url(data:font/woff2;base64,%(hand)s)}
@font-face{font-family:Cap;src:url(data:font/woff2;base64,%(cap)s)}
html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:%(bg)s}
canvas{position:absolute;inset:0;width:1080px;height:1920px}
#cap{position:absolute;top:300px;left:90px;right:90px;text-align:center;font:44px/1.25 Cap,serif;color:%(capc)s}
.lab{position:absolute;font-family:Hand;font-weight:700;white-space:nowrap;transform-origin:center}
.bub{position:absolute;left:140px;top:690px;width:800px;height:220px;background:#fff;border:7px solid #111;border-radius:12px;
 display:flex;align-items:center;justify-content:center;font:700 80px Hand;color:#7b3fe4}
.bub:after{content:'';position:absolute;left:330px;bottom:-62px;border:30px solid transparent;border-top:34px solid #111}
</style></head><body><canvas id="c" width="1080" height="1920"></canvas><div id="cap"></div><div id="labs"></div></body></html>"""

JS = """
THREE.ColorManagement.legacyMode = false;
let R, S, C, objs = [], snows = [];
function easeBack(k) { const c = 1.7; k = Math.min(1, Math.max(0, k)); return 1 + (c + 1) * Math.pow(k - 1, 3) + c * Math.pow(k - 1, 2); }
function setup(def) {
  R = new THREE.WebGLRenderer({canvas: document.getElementById('c'), antialias: true, preserveDrawingBuffer: true});
  R.setPixelRatio(1); R.setSize(1080, 1920, false); R.shadowMap.enabled = true; R.shadowMap.type = THREE.PCFSoftShadowMap;
  R.outputEncoding = THREE.sRGBEncoding;
  S = new THREE.Scene(); S.background = new THREE.Color(def.bg);
  C = new THREE.PerspectiveCamera(32, 1080 / 1920, 0.1, 100); C.position.set(0, 0.5, 11); C.lookAt(0, 0, 0);
  S.add(new THREE.HemisphereLight(0xffffff, 0x9aa4c0, def.dark ? 0.7 : 1.0));
  const d = new THREE.DirectionalLight(0xffffff, def.dark ? 0.8 : 1.1); d.position.set(-2, 4, 10); d.castShadow = true;
  d.shadow.mapSize.set(1024, 1024); d.shadow.radius = 6; const sc = d.shadow.camera; sc.left = -5; sc.right = 5; sc.top = 6; sc.bottom = -6; sc.far = 30;
  S.add(d);
  const back = new THREE.Mesh(new THREE.PlaneGeometry(30, 30), new THREE.ShadowMaterial({opacity: def.dark ? 0.18 : 0.13}));
  back.position.z = -0.9; back.receiveShadow = true; S.add(back);
  const n = def.objs.length;
  def.objs.forEach((o, i) => {
    const g = Models[o.m](...o.a); g.position.set(...o.p); g.rotation.set(...o.r);
    const st = g.userData.noPop ? 0 : 0.15 + (n > 1 ? i / (n - 1) * 0.9 : 0);
    S.add(g); objs.push({g, o, st, i});
    g.traverse(m => { if (m.userData && m.userData.snow) snows.push({m, y0: m.position.y}); });
  });
  const labs = document.getElementById('labs');
  def.labels.forEach((l, i) => {
    const e = document.createElement('div'); e.className = 'lab';
    e.style.left = l.x + 'px'; e.style.top = l.y + 'px'; e.style.fontSize = l.size + 'px'; e.style.color = l.color;
    e.innerHTML = l.html; labs.appendChild(e);
    const base = `translate(-50%, -75%) rotate(${l.rot}deg)`;
    e.animate([{opacity: 0, transform: base + ' scale(.3)'}, {opacity: 1, transform: base + ' scale(1.12)', offset: .7}, {opacity: 1, transform: base + ' scale(1)'}],
      {duration: 450, delay: (0.35 + i * 0.25) * 1000, fill: 'both', easing: 'ease-out'});
  });
  if (def.bubble) { const b = document.createElement('div'); b.className = 'bub'; b.style.top = '290px'; b.textContent = def.bubble; labs.appendChild(b);
    b.animate([{opacity: 0, transform: 'scale(.6)'}, {opacity: 1, transform: 'scale(1)'}], {duration: 400, delay: 150, fill: 'both', easing: 'ease-out'}); }
}
function frame(t, cap) {
  objs.forEach(({g, o, st, i}) => {
    const k = easeBack((t - st) / 0.55);
    g.scale.setScalar(o.s * Math.max(k, 0.0001));
    g.rotation.y = o.r[1] + 0.28 * o.spin * Math.sin(t * 0.8 + i * 1.3);
    g.position.y = o.p[1] + 0.05 * Math.sin(t * 1.6 + i);
    g.traverse(m => { if (m.userData && m.userData.flame) { if (m.userData.sy === undefined) m.userData.sy = m.scale.y; m.scale.y = m.userData.sy * (1 + 0.12 * Math.sin(t * 17 + i * 3) + 0.06 * Math.sin(t * 31)); } });
  });
  snows.forEach(({m, y0}) => { let y = y0 - t * m.userData.snow; y = ((y + 2.5) % 5 + 5) % 5 - 2.5; m.position.y = y; });
  C.position.x = 0.12 * Math.sin(t * 0.35); C.lookAt(0, 0, 0);
  document.getAnimations().forEach(a => { a.currentTime = t * 1000; });
  document.getElementById('cap').innerHTML = cap;
  R.render(S, C);
}
"""


def chunks(text):
    w = text.split()
    return [" ".join(w[i:i + WORDS]) for i in range(0, len(w), WORDS)]


def lab_html(l):
    if l.get("google"):
        return "".join(f'<span style="color:{GOOGLE[i % 6]}">{c}</span>' for i, c in enumerate(l["t"]))
    return html.escape(l["t"])


def main(spec_path):
    spec_path = Path(spec_path).resolve()
    name = spec_path.parent.name
    s = importlib.util.spec_from_file_location("scenes", spec_path)
    mod = importlib.util.module_from_spec(s)
    s.loader.exec_module(mod)
    voice, speed = getattr(mod, "VOICE", "af_heart"), getattr(mod, "SPEED", 1.08)
    work = ROOT / "output" / f".work-{name}"
    work.mkdir(parents=True, exist_ok=True)
    for old in work.glob("f*.jpg"):
        old.unlink()

    from kokoro_onnx import Kokoro
    from playwright.sync_api import sync_playwright
    tts = Kokoro(str(KOKORO / "kokoro-v1.0.onnx"), str(KOKORO / "voices-v1.0.bin"))
    three = (ROOT / "assets/js/three.min.js").read_text()
    models = (ROOT / "tools/scene3d.js").read_text()

    audio, scenes, t0, nframe = [], [], 0.0, 0
    lst = []
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path="/opt/pw-browsers/chromium",
                               args=["--no-sandbox", "--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
        page = None
        for i, sc in enumerate(mod.SCENES):
            if page:
                page.close()
            page = br.new_page(viewport={"width": W, "height": H})   # новая вкладка — чистая сцена
            a, sr = tts.create(sc["text"], voice=voice, speed=speed, lang="en-us")
            a = np.concatenate([a, np.zeros(int(sr * PAUSE), np.float32)])
            audio.append(a)
            dur = len(a) / sr
            scenes.append({"start": round(t0, 3), "dur": round(dur, 3)})
            t0 += dur
            parts = chunks(sc["text"])
            tot = sum(len(c) for c in parts)
            bounds = np.cumsum([dur * len(c) / tot for c in parts])
            bg = sc.get("bg", "#fff")
            h = bg.lstrip("#")
            dark = 0.299 * int(h[0:2], 16) + 0.587 * int(h[2:4], 16) + 0.114 * int(h[4:6], 16) < 110
            labels = [dict(l, html=lab_html(l), color=("#f4f4f4" if dark and l["color"] == "#111" else l["color"])) for l in sc.get("labels", [])]
            page.set_content(PAGE % dict(hand=FONT_HAND, cap=FONT_CAP, bg=bg, capc="#f4f4f4" if dark else "#111"))
            page.add_script_tag(content=three)
            page.add_script_tag(content=models)
            page.add_script_tag(content=JS)
            page.evaluate("Promise.all([document.fonts.load('bold 100px Hand'), document.fonts.load('44px Cap')])")
            page.evaluate("def => setup(def)", dict(bg=bg, dark=dark, objs=sc["objs"], labels=labels, bubble=sc.get("bubble")))
            nf = int(round(dur * FPS))
            for k in range(nf):
                t = k / FPS
                c = int(min(np.searchsorted(bounds, t, side="right"), len(parts) - 1))
                page.evaluate("([t, c]) => frame(t, c)", [t, html.escape(parts[c])])
                f = work / f"f{nframe:05}.jpg"
                page.screenshot(path=str(f), type="jpeg", quality=92)
                lst.append(f)
                nframe += 1
            print(f"сцена {i + 1}/{len(mod.SCENES)}: {dur:.1f} c, {nf} кадров", flush=True)
        br.close()

    (work / "scenes.json").write_text(json.dumps(scenes))
    sf.write(work / "voice.wav", np.concatenate(audio), sr)
    out = ROOT / "output" / f"{name}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", str(work / "f%05d.jpg"), "-i", str(work / "voice.wav"),
                    "-vf", "format=yuv420p", "-c:v", "libx264", "-crf", "19", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", "-movflags", "+faststart", str(out)], check=True)
    print("Готово:", out)


if __name__ == "__main__":
    main(sys.argv[1])
