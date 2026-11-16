"""Розпізнає мову у відео/аудіо і зберігає субтитри (.srt) у теку output/.

Використання:
    python tools/transcribe.py originals/video.mp4            # українська за замовчуванням
    python tools/transcribe.py originals/video.mp4 --model medium
"""
import argparse
from pathlib import Path

from faster_whisper import WhisperModel


def ts(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("file", help="відео або аудіо файл")
    p.add_argument("--lang", default="uk", help="мова (uk, en, ...)")
    p.add_argument("--model", default="small", help="tiny / base / small / medium / large-v3")
    args = p.parse_args()

    src = Path(args.file)
    out = Path(__file__).resolve().parent.parent / "output" / (src.stem + ".srt")
    out.parent.mkdir(exist_ok=True)

    print(f"Завантажую модель '{args.model}' (перший раз — кілька хвилин)...")
    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(src), language=args.lang, vad_filter=True)

    with out.open("w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, 1):
            f.write(f"{i}\n{ts(seg.start)} --> {ts(seg.end)}\n{seg.text.strip()}\n\n")
            print(f"[{ts(seg.start)}] {seg.text.strip()}")

    print(f"\nГотово! Субтитри: {out}")


if __name__ == "__main__":
    main()
