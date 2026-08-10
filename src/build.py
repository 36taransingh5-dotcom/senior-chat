#!/usr/bin/env python3
"""Rebuild index.html from src/template.html + fonts/*.woff2.

Run from the repo root:
    python3 src/build.py
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

def b64(path):
    return base64.b64encode(path.read_bytes()).decode("ascii")

def main():
    template = (ROOT / "src" / "template.html").read_text()
    manrope = b64(ROOT / "fonts" / "Manrope-Variable.woff2")
    jbm = b64(ROOT / "fonts" / "JetBrainsMono-Regular.woff2")
    serif = b64(ROOT / "fonts" / "InstrumentSerif-Regular.woff2")
    serif_it = b64(ROOT / "fonts" / "InstrumentSerif-Italic.woff2")
    grotesk = b64(ROOT / "fonts" / "SpaceGrotesk-Variable.woff2")

    html = (
        template.replace("{{MANROPE}}", manrope)
        .replace("{{JBM}}", jbm)
        .replace("{{SERIF}}", serif)
        .replace("{{SERIF_IT}}", serif_it)
        .replace("{{GROTESK}}", grotesk)
    )
    out = ROOT / "index.html"
    out.write_text(html)
    print(f"wrote {out} ({len(html):,} bytes)")

if __name__ == "__main__":
    main()
