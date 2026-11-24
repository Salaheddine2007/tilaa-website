"""Render the brand mark (assets/icons/mark.svg) to favicon/app icons.
Needs Playwright + Pillow locally; run by hand after changing the mark."""
import io, re
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "assets" / "icons"
svg = (ICONS / "mark.svg").read_text(encoding="utf-8")
# tiny sizes: drop the star, it turns into noise below 24px
small = svg
# apple-touch: full-bleed square, iOS rounds the corners itself
square = svg.replace('rx="16"', 'rx="0"')

def render(src, size):
    html = f"<body style='margin:0'><div style='width:{size}px;height:{size}px'>{src}</div></body>"
    pg.set_viewport_size({"width": size, "height": size})
    pg.set_content(html)
    return Image.open(io.BytesIO(pg.screenshot(omit_background=True))).convert("RGBA")

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    render(small, 32).save(ICONS / "favicon-32.png")
    render(square, 180).save(ICONS / "apple-touch-icon.png")
    render(svg, 192).save(ICONS / "icon-192.png")
    render(svg, 512).save(ICONS / "icon-512.png")
    ico = [render(small, s) for s in (16, 32)] + [render(svg, 48)]
    b.close()
ico[2].save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=ico[:2])
print("icons written")
