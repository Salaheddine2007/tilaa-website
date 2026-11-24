"""Open Graph cards (1200x630) per page: night background, the HD bug, the page title.
build(out_dir, [(name, title), ...]) writes only missing <name>.png and returns how many it made.
Without Pillow (e.g. a bare cloud runner) missing cards become copies of home.png, so pages never
point at a 404 image.
"""
import os, shutil

NIGHT, SIGNAL, WHITE, MIST = (5, 14, 36), (200, 16, 46), (255, 255, 255), (147, 166, 204)
FONTS_BOLD = ["C:/Windows/Fonts/arialbd.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"]

def _font(size):
    from PIL import ImageFont
    for p in FONTS_BOLD:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def _wrap(draw, text, font, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + [cur]

def card(path, title):
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (1200, 630), NIGHT)
    # soft crimson glow top-right, like the site hero
    glow = Image.new("RGB", (1200, 630), NIGHT)
    gd = ImageDraw.Draw(glow)
    for r, a in ((520, 18), (400, 30), (280, 46)):
        col = tuple(int(NIGHT[i] + (SIGNAL[i] - NIGHT[i]) * a / 100) for i in range(3))
        gd.ellipse([1200 - r, -r, 1200 + r, r], fill=col)
    from PIL import ImageFilter
    img = glow.filter(ImageFilter.GaussianBlur(90))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 618, 1200, 630], fill=SIGNAL)
    brand = _font(44)
    d.text((80, 70), "iptv norway", font=brand, fill=WHITE)
    x = 80 + d.textlength("iptv norway ", font=brand)
    d.rounded_rectangle([x, 66, x + 118, 122], radius=10, fill=SIGNAL)
    d.text((x + 8, 70), "One", font=brand, fill=WHITE)
    size = 76
    while True:
        f = _font(size)
        lines = _wrap(d, title, f, 1040)
        if len(lines) <= 4 or size <= 44:
            break
        size -= 6
    y = 600 - 70 - len(lines) * int(size * 1.15)
    for line in lines:
        d.text((80, y), line, font=f, fill=WHITE)
        y += int(size * 1.15)
    d.text((80, 548), "iptvnorwayone.com", font=_font(26), fill=MIST)
    img.save(path, optimize=True)
    img.save(path[:-4] + ".webp", "WEBP", quality=82, method=6)  # in-content featured image

def build(out_dir, items):
    os.makedirs(out_dir, exist_ok=True)
    made = 0
    try:
        from PIL import Image, ImageDraw  # noqa: F401
        have_pil = True
    except (ImportError, Exception):
        have_pil = False
    for name, title in items:
        path = os.path.join(out_dir, name + ".png")
        if os.path.exists(path) and os.path.exists(path[:-4] + ".webp"):
            continue
        if have_pil:
            card(path, title)
        else:
            # no Pillow (bare runner): reuse an existing card so the page never points at a missing image
            fb = next((n for n in ("no-home", "en-home", "home") if os.path.exists(os.path.join(out_dir, n + ".png"))), None)
            if fb:
                shutil.copy(os.path.join(out_dir, fb + ".png"), path)
                shutil.copy(os.path.join(out_dir, fb + ".webp"), path[:-4] + ".webp")
        made += 1
    return made
