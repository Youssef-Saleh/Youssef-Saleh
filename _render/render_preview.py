"""
render_preview.py — Render the GitHub profile README to a PNG so we can
verify it visually before pushing to GitHub.

Strategy:
- Parse the README's <svg> block(s) out and save them as standalone .svg files
  (PIL/Pillow can render those, since cairo/wand aren't installed)
- Render the SVG to PNG with cairosvg if present, else fall back to a custom
  inline SVG → PNG rasterizer that uses Pillow's basic primitives. Most of the
  hero SVG is rectangles, lines, text and gradients — all of which PIL handles.
- Stitch the SVG render + a rasterized Markdown preview into one tall PNG
  so we can see the profile top-to-bottom.
"""
import sys
import re
import base64
import io
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(r"C:\Users\Youssef\Youssef-Saleh")
PREVIEW_DIR = ROOT / "_preview"
PREVIEW_DIR.mkdir(exist_ok=True)
README = (ROOT / "README.md").read_text(encoding="utf-8")

# ---------- SVG extraction ----------
svg_re = re.compile(r"<svg[^>]*>.*?</svg>", re.DOTALL | re.IGNORECASE)
svgs = svg_re.findall(README)
print(f"Found {len(svgs)} SVG block(s)")

def save_svg(idx, svg_str):
    p = PREVIEW_DIR / f"hero_{idx}.svg"
    p.write_text(svg_str, encoding="utf-8")
    return p

# ---------- Simple SVG → PNG rasterizer (Cairo/Wand-free, PIL-only) ----------
# Handles the subset of SVG we'll actually use:
#   <svg viewBox=...> <defs> linearGradient </defs>
#   <rect x y width height fill=... rx=... ry=...>
#   <line x1 y1 x2 y2 stroke=... stroke-width=...>
#   <text x y font-size=... fill=... text-anchor=...>[content]</text>
#   <text>...<tspan x= y= ...>...</tspan></text>
#   <circle cx cy r=... fill=... stroke=...>
#   <path d=...M..L.. stroke=... fill=...>
# Anything else will be ignored (logged).
def parse_length(s, scale=1.0):
    s = s.strip()
    m = re.match(r"([\d.]+)(px|pt|em|%)?", s)
    if not m:
        return 0.0
    v = float(m.group(1))
    unit = m.group(2) or "px"
    if unit == "%":
        return v / 100.0  # caller will multiply by viewport
    return v * scale

def parse_color(c):
    if not c:
        return None
    c = c.strip()
    if c in ("none", "transparent"):
        return None
    # hex
    if c.startswith("#"):
        c = c[1:]
        if len(c) == 3:
            c = "".join(ch*2 for ch in c)
        if len(c) == 6:
            return tuple(int(c[i:i+2], 16) for i in (0, 2, 4)) + (255,)
        if len(c) == 8:
            return tuple(int(c[i:i+2], 16) for i in (0, 2, 4, 6))
    # rgb()
    m = re.match(r"rgba?\(([^)]+)\)", c)
    if m:
        parts = [p.strip() for p in m.group(1).split(",")]
        rgb = [int(parts[i]) for i in range(3)]
        a = int(float(parts[3]) * 255) if len(parts) > 3 else 255
        return tuple(rgb) + (a,)
    # named
    named = {
        "black": (0,0,0,255), "white": (255,255,255,255),
        "red": (255,0,0,255), "green": (0,255,0,255),
        "blue": (0,0,255,255), "yellow": (255,255,0,255),
        "cyan": (0,255,255,255), "magenta": (255,0,255,255),
        "gray": (128,128,128,255), "grey": (128,128,128,255),
        "orange": (255,165,0,255), "purple": (128,0,128,255),
        "lime": (0,255,0,255), "navy": (0,0,128,255),
        "teal": (0,128,128,255),
    }
    return named.get(c.lower())

def render_svg_to_pil(svg_text, target_w=1200, target_h=None, scale=None):
    """Render a simple SVG to a PIL image. Returns Image."""
    # viewBox
    m = re.search(r"viewBox\s*=\s*\"([^\"]+)\"", svg_text)
    if m:
        vb = [float(x) for x in m.group(1).split()]
        vb_w, vb_h = vb[2], vb[3]
    else:
        # fall back to width/height attrs
        w_m = re.search(r"<svg[^>]*\bwidth\s*=\s*\"([^\"]+)\"", svg_text)
        h_m = re.search(r"<svg[^>]*\bheight\s*=\s*\"([^\"]+)\"", svg_text)
        vb_w = float(re.match(r"([\d.]+)", w_m.group(1)).group(1)) if w_m else 800
        vb_h = float(re.match(r"([\d.]+)", h_m.group(1)).group(1)) if h_m else 400

    if target_h is None:
        # aspect ratio
        target_h = int(target_w * vb_h / vb_w)
    if scale is None:
        scale = target_w / vb_w

    img = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Build gradient palette
    gradients = {}
    for g in re.finditer(r"<linearGradient[^>]*\bid\s*=\s*\"([^\"]+)\"[^>]*>(.*?)</linearGradient>", svg_text, re.DOTALL):
        gid = g.group(1)
        body = g.group(2)
        stops = re.findall(r"<stop[^>]*\boffset\s*=\s*\"([\d.%]+)\"[^>]*\bstop-color\s*=\s*\"([^\"]+)\"", body)
        # also accept stop-color via style attr
        stops2 = re.findall(r"<stop[^>]*\bstop-color\s*=\s*\"([^\"]+)\"[^>]*\boffset\s*=\s*\"([\d.%]+)\"", body)
        if not stops and stops2:
            stops = [(o, c) for c, o in stops2]
        parsed = []
        for off_str, col in stops:
            off = float(off_str.rstrip("%")) / (100 if off_str.endswith("%") else 1)
            parsed.append((off, parse_color(col)))
        parsed.sort()
        gradients[gid] = parsed

    def color_at(grad_id, t):
        if grad_id not in gradients:
            return (255, 255, 255, 255)
        stops = gradients[grad_id]
        if t <= stops[0][0]: return stops[0][1]
        if t >= stops[-1][0]: return stops[-1][1]
        for i in range(len(stops) - 1):
            a_off, a_col = stops[i]
            b_off, b_col = stops[i+1]
            if a_off <= t <= b_off:
                k = (t - a_off) / max(b_off - a_off, 1e-6)
                return tuple(int(a_col[c] + (b_col[c] - a_col[c]) * k) for c in range(4))
        return stops[-1][1]

    def resolve_fill(node_str, x0, y0, x1, y1):
        f = re.search(r"\bfill\s*=\s*\"([^\"]+)\"", node_str)
        if not f:
            return (0, 0, 0, 0)  # default fill black
        v = f.group(1).strip()
        if v == "none":
            return None
        if v.startswith("url("):
            gid = v[4:-1].strip()
            # gradient along x for simplicity
            t = ((x0 + x1) / 2 - 0) / max(vb_w, 1)
            return color_at(gid, max(0, min(1, t)))
        c = parse_color(v)
        return c

    def resolve_stroke(node_str):
        s = re.search(r"\bstroke\s*=\s*\"([^\"]+)\"", node_str)
        if not s or s.group(1).strip() == "none":
            return None
        v = s.group(1).strip()
        if v.startswith("url("):
            return (255, 255, 255, 255)
        return parse_color(v)

    # ----- <rect> -----
    for r in re.finditer(r"<rect\b([^/>]*)/?>", svg_text, re.DOTALL):
        attrs = r.group(1)
        x = float(re.search(r"\bx\s*=\s*\"([^\"]+)\"", attrs).group(1)) if re.search(r"\bx\s*=", attrs) else 0
        y = float(re.search(r"\by\s*=\s*\"([^\"]+)\"", attrs).group(1)) if re.search(r"\by\s*=", attrs) else 0
        w = float(re.search(r"\bwidth\s*=\s*\"([^\"]+)\"", attrs).group(1))
        h = float(re.search(r"\bheight\s*=\s*\"([^\"]+)\"", attrs).group(1))
        rx = float(re.search(r"\brx\s*=\s*\"([^\"]+)\"", attrs).group(1)) if re.search(r"\brx\s*=", attrs) else 0
        # scale
        X, Y, W, H = x*scale, y*scale, w*scale, h*scale
        fill = resolve_fill(attrs, X, Y, X+W, Y+H)
        stroke = resolve_stroke(attrs)
        sw = float(re.search(r"\bstroke-width\s*=\s*\"([^\"]+)\"", attrs).group(1)) if re.search(r"\bstroke-width\s*=", attrs) else 1
        if fill is not None:
            if rx > 0:
                draw.rounded_rectangle([X, Y, X+W, Y+H], radius=rx*scale, fill=fill)
            else:
                draw.rectangle([X, Y, X+W, Y+H], fill=fill)
        if stroke is not None and sw > 0:
            if rx > 0:
                draw.rounded_rectangle([X, Y, X+W, Y+H], radius=rx*scale, outline=stroke, width=max(1, int(sw*scale)))
            else:
                draw.rectangle([X, Y, X+W, Y+H], outline=stroke, width=max(1, int(sw*scale)))

    # ----- <line> -----
    for ln in re.finditer(r"<line\b([^/>]*)/?>", svg_text, re.DOTALL):
        attrs = ln.group(1)
        x1 = float(re.search(r"\bx1\s*=\s*\"([^\"]+)\"", attrs).group(1))
        y1 = float(re.search(r"\by1\s*=\s*\"([^\"]+)\"", attrs).group(1))
        x2 = float(re.search(r"\bx2\s*=\s*\"([^\"]+)\"", attrs).group(1))
        y2 = float(re.search(r"\by2\s*=\s*\"([^\"]+)\"", attrs).group(1))
        stroke = resolve_stroke(attrs) or (255, 255, 255, 255)
        sw = float(re.search(r"\bstroke-width\s*=\s*\"([^\"]+)\"", attrs).group(1)) if re.search(r"\bstroke-width\s*=", attrs) else 1
        # dashed?
        dash = re.search(r"\bstroke-dasharray\s*=\s*\"([^\"]+)\"", attrs)
        dash_tuple = None
        if dash:
            dash_tuple = tuple(float(d) for d in dash.group(1).split(","))
        draw.line([x1*scale, y1*scale, x2*scale, y2*scale], fill=stroke, width=max(1, int(sw*scale)))

    # ----- <circle> -----
    for c in re.finditer(r"<circle\b([^/>]*)/?>", svg_text, re.DOTALL):
        attrs = c.group(1)
        cx = float(re.search(r"\bcx\s*=\s*\"([^\"]+)\"", attrs).group(1))
        cy = float(re.search(r"\bcy\s*=\s*\"([^\"]+)\"", attrs).group(1))
        rr = float(re.search(r"\br\s*=\s*\"([^\"]+)\"", attrs).group(1))
        fill = resolve_fill(attrs, cx-rr, cy-rr, cx+rr, cy+rr)
        stroke = resolve_stroke(attrs)
        sw = float(re.search(r"\bstroke-width\s*=\s*\"([^\"]+)\"", attrs).group(1)) if re.search(r"\bstroke-width\s*=", attrs) else 1
        if fill is not None:
            draw.ellipse([(cx-rr)*scale, (cy-rr)*scale, (cx+rr)*scale, (cy+rr)*scale], fill=fill)
        if stroke is not None and sw > 0:
            draw.ellipse([(cx-rr)*scale, (cy-rr)*scale, (cx+rr)*scale, (cy+rr)*scale], outline=stroke, width=max(1, int(sw*scale)))

    # ----- <text> -----
    def get_font(size, family=None, weight=None):
        size = int(size * scale)
        # try Cascadia Mono first
        candidates = [
            r"C:\Windows\Fonts\CascadiaMono.ttf",
            r"C:\Windows\Fonts\consola.ttf",
            r"C:\Windows\Fonts\cour.ttf",
        ]
        for path in candidates:
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
        return ImageFont.load_default()

    for t in re.finditer(r"<text\b([^>]*)>(.*?)</text>", svg_text, re.DOTALL):
        attrs = t.group(1)
        body = t.group(2)
        x = float(re.search(r"\bx\s*=\s*\"([^\"]+)\"", attrs).group(1)) if re.search(r"\bx\s*=", attrs) else 0
        y = float(re.search(r"\by\s*=\s*\"([^\"]+)\"", attrs).group(1)) if re.search(r"\by\s*=", attrs) else 0
        sz = float(re.search(r"\bfont-size\s*=\s*\"([^\"]+)\"", attrs).group(1)) if re.search(r"\bfont-size\s*=", attrs) else 16
        fill = resolve_fill(attrs, x, y, x, y) or (255, 255, 255, 255)
        # text-anchor
        anchor = re.search(r"\btext-anchor\s*=\s*\"([^\"]+)\"", attrs)
        anchor = anchor.group(1) if anchor else "start"
        font = get_font(sz)
        # extract plain text (strip tspan tags but keep content)
        clean = re.sub(r"<[^>]+>", "", body)
        # decode HTML entities (very small set)
        clean = clean.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#x27;", "'")
        if anchor == "middle":
            bbox = draw.textbbox((0, 0), clean, font=font)
            tw = bbox[2] - bbox[0]
            draw.text((x*scale - tw/2, y*scale), clean, font=font, fill=fill)
        elif anchor == "end":
            bbox = draw.textbbox((0, 0), clean, font=font)
            tw = bbox[2] - bbox[0]
            draw.text((x*scale - tw, y*scale), clean, font=font, fill=fill)
        else:
            draw.text((x*scale, y*scale), clean, font=font, fill=fill)

    return img

# ---------- Render each SVG found ----------
for i, svg in enumerate(svgs):
    p = save_svg(i, svg)
    img = render_svg_to_pil(svg, target_w=1400)
    out = PREVIEW_DIR / f"hero_{i}.png"
    img.save(out)
    print(f"  hero_{i}.svg → {out.name}  ({img.size[0]}x{img.size[1]})")

# ---------- Render a Markdown preview (simple typeset) ----------
def render_markdown_preview(md_text, width=1400, bg=(10, 14, 26, 255)):
    """Render the markdown body (no SVGs) as a typographic preview."""
    img = Image.new("RGBA", (width, 8000), bg)
    draw = ImageDraw.Draw(img)
    # load fonts
    def f(size, bold=False, mono=False):
        if mono:
            return ImageFont.truetype(r"C:\Windows\Fonts\CascadiaMono.ttf", size)
        if bold:
            return ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", size)
        return ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", size)
    body_font = f(18)
    h1_font = f(34, bold=True)
    h2_font = f(26, bold=True)
    h3_font = f(22, bold=True)
    code_font = f(16, mono=True)
    link_color = (26, 199, 217, 255)  # teal
    text_color = (201, 209, 217, 255)  # light gray
    muted = (140, 150, 165, 255)
    accent = (242, 158, 46, 255)  # amber
    x_margin = 80
    y = 60
    line_h = 28
    max_w = width - 2 * x_margin

    def wrap(text, font, max_width):
        words = text.split()
        lines, cur = [], ""
        for w in words:
            test = (cur + " " + w).strip()
            bb = draw.textbbox((0, 0), test, font=font)
            if bb[2] - bb[0] <= max_width:
                cur = test
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    # strip svg blocks from the markdown so we don't double-render them
    md = svg_re.sub("", md_text)
    # strip the badges/img lines that pull from the network — they would just be blank space
    md = re.sub(r"^\s*<img[^>]*/>\s*$", "", md, flags=re.MULTILINE)
    md = re.sub(r"^\s*<picture>.*?</picture>\s*$", "", md, flags=re.MULTILINE | re.DOTALL)
    md = re.sub(r"^\s*<a[^>]*>.*?</a>\s*$", "", md, flags=re.MULTILINE | re.DOTALL)
    # strip html div wrappers
    md = re.sub(r"</?div[^>]*>", "", md)
    # strip badges-only lines (whole line is just <img> or shield)
    md = re.sub(r"<img[^>]*shields\.io[^>]*>", "", md)
    md = re.sub(r"<img[^>]*skillicons[^>]*>", "", md)

    in_code = False
    code_buf = []
    for line in md.splitlines():
        if line.strip().startswith("```"):
            if in_code:
                # flush code block
                for cl in code_buf:
                    draw.text((x_margin + 20, y), cl, font=code_font, fill=(26, 199, 217, 255))
                    y += 22
                y += 12
                code_buf = []
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_buf.append(line)
            continue
        if not line.strip():
            y += 12
            continue
        if line.startswith("# "):
            text = line[2:]
            draw.text((x_margin, y), text, font=h1_font, fill=accent)
            y += 48
            # underline
            draw.line([(x_margin, y - 8), (x_margin + 400, y - 8)], fill=accent, width=2)
        elif line.startswith("## "):
            text = line[3:]
            draw.text((x_margin, y), text, font=h2_font, fill=(26, 199, 217, 255))
            y += 40
        elif line.startswith("### "):
            text = line[4:]
            draw.text((x_margin, y), text, font=h3_font, fill=text_color)
            y += 34
        elif line.lstrip().startswith(("- ", "* ", "+ ")):
            text = "▸ " + line.lstrip()[2:]
            for ln in wrap(text, body_font, max_w - 40):
                draw.text((x_margin + 20, y), ln, font=body_font, fill=text_color)
                y += line_h
        elif re.match(r"^\d+\.\s", line.lstrip()):
            text = line.lstrip()
            for ln in wrap(text, body_font, max_w - 40):
                draw.text((x_margin + 20, y), ln, font=body_font, fill=text_color)
                y += line_h
        elif line.startswith(">"):
            text = line.lstrip(">").strip()
            for ln in wrap(text, body_font, max_w - 40):
                draw.text((x_margin + 12, y), "│ " + ln, font=body_font, fill=accent)
                y += line_h
        elif line.startswith("|") and "|" in line[1:]:
            # table — render simply
            text = line.strip().strip("|")
            cells = [c.strip() for c in text.split("|")]
            # skip separator rows
            if all(re.match(r"^[-:\s]+$", c) for c in cells):
                y += 4
                continue
            x = x_margin
            col_w = max_w // max(len(cells), 1)
            for c in cells:
                # simple truncation
                txt = c[:30] + ("…" if len(c) > 30 else "")
                # bold first cell if it looks like an emoji/icon header
                font = body_font
                draw.text((x, y), txt, font=font, fill=text_color)
                x += col_w
            y += line_h
        else:
            for ln in wrap(line, body_font, max_w):
                draw.text((x_margin, y), ln, font=body_font, fill=text_color)
                y += line_h
        y += 8
        if y > 7800:
            break

    # crop to actual height
    return img.crop((0, 0, width, min(y + 60, 8000)))

md_img = render_markdown_preview(README)
md_img.save(PREVIEW_DIR / "markdown_body.png")
print(f"markdown body: {md_img.size}")

# ---------- Stitch everything into one tall preview ----------
hero_imgs = [Image.open(PREVIEW_DIR / f"hero_{i}.png") for i in range(len(svgs))]
W = 1400
sections = hero_imgs + [md_img]
total_h = sum(s.size[1] for s in sections) + (len(sections) - 1) * 20
preview = Image.new("RGBA", (W, total_h), (10, 14, 26, 255))
y = 0
for s in sections:
    preview.paste(s, (0, y), s if s.mode == "RGBA" else None)
    y += s.size[1] + 20

# crop bottom whitespace
preview = preview.crop((0, 0, W, min(total_h, 6000)))
preview.save(PREVIEW_DIR / "profile_full.png")
print(f"full preview: {preview.size}, saved to {PREVIEW_DIR / 'profile_full.png'}")
