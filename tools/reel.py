"""Собирает рисованный рилс 9:16 из сценария.

Сценарий — Python-файл со списком SCENES: [{"text": "фраза для голоса", "svg": "<рисунок>"}].
Каждая сцена: голос (Piper) + картинка (SVG) + субтитры сверху.

    python3 tools/reel.py reels/2026-11-16-advent-nuts/scenes.py
Результат: output/<имя папки>.mp4
"""
import base64
import html
import importlib.util
import subprocess
import sys
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1920
VOICE = ROOT / "assets/voices/en_US-amy-medium.onnx"
PAUSE = 0.35  # пауза после каждой фразы, сек
WORDS_PER_CAPTION = 5
FONTS = [base64.b64encode((ROOT / "assets/fonts" / f).read_bytes()).decode()
         for f in ("Caveat-Bold.woff2", "PTSerif-Regular.woff2")]

PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Hand;src:url(data:font/woff2;base64,%(hand)s)}
@font-face{font-family:Cap;src:url(data:font/woff2;base64,%(cap_font)s)}
html,body{margin:0;width:%(w)dpx;height:%(h)dpx;background:#fff;overflow:hidden}
.cap{position:absolute;top:300px;left:90px;right:90px;text-align:center;font:44px/1.25 Cap,serif;color:#111}
svg{position:absolute;left:40px;top:480px;width:1000px;height:1000px}
.hand{font-family:Hand,cursive;fill:#111}
.red{fill:#b3122e}
.ln{fill:none;stroke:#111;stroke-width:7;stroke-linecap:round;stroke-linejoin:round}
</style></head><body><div class="cap">%(cap)s</div>
<svg viewBox="0 0 1000 1000"><defs><filter id="wob"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="%(seed)d"/>
<feDisplacementMap in="SourceGraphic" scale="9"/></filter></defs><g filter="url(#wob)">%(svg)s</g></svg></body></html>"""


def tts(text: str, out: Path) -> float:
    subprocess.run([sys.executable, "-m", "piper", "-m", str(VOICE), "-f", str(out),
                    "--sentence-silence", "0.2"], input=text.encode(), check=True,
                   capture_output=True)
    with wave.open(str(out)) as w:
        return w.getnframes() / w.getframerate()


def chunks(text: str):
    words = text.split()
    return [" ".join(words[i:i + WORDS_PER_CAPTION]) for i in range(0, len(words), WORDS_PER_CAPTION)]


def main(spec_path: str) -> None:
    spec_path = Path(spec_path).resolve()
    name = spec_path.parent.name
    s = importlib.util.spec_from_file_location("scenes", spec_path)
    mod = importlib.util.module_from_spec(s)
    s.loader.exec_module(mod)

    work = ROOT / "output" / f".work-{name}"
    work.mkdir(parents=True, exist_ok=True)

    from playwright.sync_api import sync_playwright

    frames, audio = [], []
    with sync_playwright() as p:
        page = p.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"]).new_page(viewport={"width": W, "height": H})
        for i, sc in enumerate(mod.SCENES):
            wav = work / f"s{i:02}.wav"
            dur = tts(sc["text"], wav) + PAUSE
            audio.append(wav)
            parts = chunks(sc["text"])
            total = sum(len(c) for c in parts)
            for j, cap in enumerate(parts):
                png = work / f"s{i:02}_{j:02}.png"
                page.set_content(PAGE % dict(hand=FONTS[0], cap_font=FONTS[1], w=W, h=H, seed=i,
                                             cap=html.escape(cap), svg=sc["svg"]))
                page.evaluate("document.fonts.ready")
                page.wait_for_timeout(100)
                page.screenshot(path=str(png))
                frames.append((png, dur * len(cap) / total))
            print(f"сцена {i + 1}/{len(mod.SCENES)}: {dur:.1f} c")

    # видео-ряд
    lst = work / "frames.txt"
    lst.write_text("".join(f"file '{f}'\nduration {d:.3f}\n" for f, d in frames) + f"file '{frames[-1][0]}'\n")
    # аудио: каждая фраза + пауза
    alst = work / "audio.txt"
    alst.write_text("".join(f"file '{a}'\n" for a in audio))
    flt = ";".join(f"[{k}]apad=pad_dur={PAUSE}[a{k}]" for k in range(len(audio)))
    flt += ";" + "".join(f"[a{k}]" for k in range(len(audio))) + f"concat=n={len(audio)}:v=0:a=1[aout]"
    voice = work / "voice.m4a"
    subprocess.run(["ffmpeg", "-y", "-v", "error", *sum([["-i", str(a)] for a in audio], []),
                    "-filter_complex", flt, "-map", "[aout]", "-c:a", "aac", "-b:a", "160k", str(voice)], check=True)

    out = ROOT / "output" / f"{name}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(voice),
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "20", "-c:a", "copy",
                    "-shortest", "-movflags", "+faststart", str(out)], check=True)
    print("Готово:", out)


if __name__ == "__main__":
    main(sys.argv[1])
