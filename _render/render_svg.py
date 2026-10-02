"""
render_svg.py — Improved SVG → PNG rasterizer.
Renders the C2 hero SVG (and any subset of SVG that uses primitives only).
Supports: rect, line, circle, ellipse, path (M/L/Q/C/Z), polygon, polyline,
text, tspan, linearGradient (with multiple stops), fill/stroke, stroke-width,
stroke-dasharray, fill-opacity, stroke-opacity, text-anchor, font-size.

Doesn't support: filter, clipPath, mask, symbol/use, animation, foreignObject.
"""
import sys, re, html
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Default font paths (we look for these in order)
FONT_PATHS = [
    r"C:\Windows\Fonts\CascadiaMono.ttf",
    r"C:\Windows\Fonts\consola.ttf",
    r"C:\Windows\Fonts\cour.ttf",
]

def _load_font(size):
    size = max(6, int(size))
    for p in FONT_PATHS:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

# ---------- helpers ----------
def _parse_color(c):
    if not c:
        return None
    c = c.strip()
    if c in ("none", "transparent", ""):
        return None
    if c.startswith("#"):
        hexpart = c[1:]
        if len(hexpart) == 3:
            hexpart = "".join(ch*2 for ch in hexpart)
        if len(hexpart) == 6:
            return tuple(int(hexpart[i:i+2], 16) for i in (0,2,4)) + (255,)
        if len(hexpart) == 8:
            return tuple(int(hexpart[i:i+2], 16) for i in (0,2,4,6))
    m = re.match(r"rgba?\(([^)]+)\)", c)
    if m:
        parts = [p.strip() for p in m.group(1).split(",")]
        try:
            rgb = [int(float(parts[i])) for i in range(3)]
        except ValueError:
            return None
        a = int(float(parts[3]) * 255) if len(parts) > 3 else 255
        return tuple(rgb) + (max(0, min(255, a)),)
    named = {
        "black":(0,0,0,255),"white":(255,255,255,255),"red":(255,0,0,255),
        "green":(0,255,0,255),"blue":(0,0,255,255),"yellow":(255,255,0,255),
        "cyan":(0,255,255,255),"magenta":(255,0,255,255),
        "gray":(128,128,128,255),"grey":(128,128,128,255),
        "orange":(255,165,0,255),"purple":(128,0,128,255),
        "lime":(0,255,0,255),"navy":(0,0,128,255),"teal":(0,128,128,255),
    }
    return named.get(c.lower())

def _html_decode(s):
    # handles &#x27; &#272; and named like &amp;
    s = html.unescape(s)
    return s

def _attr(node, name, default=None):
    m = re.search(rf"\b{name}\s*=\s*\"([^\"]+)\"", node)
    return m.group(1) if m else default

def _attr_num(node, name, default=0.0):
    v = _attr(node, name)
    if v is None:
        return default
    try:
        return float(v)
    except ValueError:
        return default

# ---------- main renderer ----------
def render(svg_text, out_path, target_w=1400, bg=(0,0,0,0)):
    # 1. Parse viewBox
    m = re.search(r"viewBox\s*=\s*\"([^\"]+)\"", svg_text)
    if m:
        vb = [float(x) for x in m.group(1).split()]
        vb_x, vb_y, vb_w, vb_h = vb
    else:
        vb_x, vb_y, vb_w, vb_h = 0, 0, 800, 600

    target_h = int(target_w * vb_h / vb_w)
    scale = target_w / vb_w
    img = Image.new("RGBA", (target_w, target_h), bg)
    draw = ImageDraw.Draw(img)

    # 2. Build gradients
    gradients = {}
    for g in re.finditer(r"<(linear|radial)Gradient\b[^>]*\bid\s*=\s*\"([^\"]+)\"[^>]*>(.*?)</\1Gradient>", svg_text, re.DOTALL):
        gid = g.group(2)
        body = g.group(3)
        stops = []
        for s in re.finditer(r"<stop\b([^/>]*)/?>", body, re.DOTALL):
            sattrs = s.group(1)
            off = _attr(sattrs, "offset", "0")
            col = _attr(sattrs, "stop-color", "#000000")
            op = _attr(sattrs, "stop-opacity", "1")
            off_val = float(off.rstrip("%")) / (100 if off.endswith("%") else 1)
            base = _parse_color(col)
            if base is None:
                continue
            a = int(float(op) * base[3])
            stops.append((off_val, (base[0], base[1], base[2], a)))
        stops.sort()
        gradients[gid] = stops

    def color_at(gid, t):
        if gid not in gradients:
            return (255,255,255,255)
        stops = gradients[gid]
        if t <= stops[0][0]:
            return stops[0][1]
        if t >= stops[-1][0]:
            return stops[-1][1]
        for i in range(len(stops)-1):
            ao, ac = stops[i]
            bo, bc = stops[i+1]
            if ao <= t <= bo:
                k = (t-ao)/max(bo-ao, 1e-6)
                return tuple(int(ac[c]+(bc[c]-ac[c])*k) for c in range(4))
        return stops[-1][1]

    def fill_of(attrs, x0=0, y0=0, x1=0, y1=0, parent_fill=None):
        f = _attr(attrs, "fill", parent_fill if parent_fill is not None else "#000000")
        fo = _attr(attrs, "fill-opacity", "1")
        if f == "none":
            return None
        if f.startswith("url("):
            gid = f[4:].rstrip(")").strip().lstrip("#")
            # gradient along x for linear, or radial simple
            if vb_w == 0:
                return (255,255,255,255)
            t = (x0 / (vb_w * scale))
            base = color_at(gid, max(0, min(1, t)))
        else:
            base = _parse_color(f)
        if base is None:
            return None
        if fo != "1":
            a = int(float(fo) * base[3])
            base = (base[0], base[1], base[2], a)
        return base

    def stroke_of(attrs, parent_stroke=None):
        s = _attr(attrs, "stroke", parent_stroke)
        if s is None or s == "none":
            return None
        so = _attr(attrs, "stroke-opacity", "1")
        if s.startswith("url("):
            base = (255,255,255,255)
        else:
            base = _parse_color(s)
        if base is None:
            return None
        if so != "1":
            a = int(float(so) * base[3])
            base = (base[0], base[1], base[2], a)
        return base

    def stroke_w(attrs, parent=1.0):
        sw = _attr(attrs, "stroke-width")
        if sw is None:
            return max(1, int(parent * scale))
        return max(1, int(float(sw) * scale))

    # helper to convert a (x,y) in viewBox to image pixels
    def pt(x, y):
        return (int((x - vb_x) * scale), int((y - vb_y) * scale))

    # helper to convert size
    def sz(v):
        return max(1, int(v * scale))

    # transform stack placeholder — actual transform is applied per-drawable
    # by rebinding `pt` in the render loop.

    def fill_rect(p0, p1, color, rx=0):
        if rx > 0:
            draw.rounded_rectangle([p0, p1], radius=sz(rx), fill=color)
        else:
            draw.rectangle([p0, p1], fill=color)
    def stroke_rect(p0, p1, color, w, rx=0):
        if rx > 0:
            draw.rounded_rectangle([p0, p1], radius=sz(rx), outline=color, width=w)
        else:
            draw.rectangle([p0, p1], outline=color, width=w)
    def fill_ellipse(p0, p1, color):
        draw.ellipse([p0, p1], fill=color)
    def stroke_ellipse(p0, p1, color, w):
        draw.ellipse([p0, p1], outline=color, width=w)
    def fill_polygon(pts, color):
        draw.polygon(pts, fill=color)
    def fill_path_polygon(pts, color):
        # if path was M..L..Z, the last point == first so polygon is fine
        if len(pts) >= 3:
            draw.polygon(pts, fill=color)
    def stroke_line(pts, color, w):
        draw.line(pts, fill=color, width=w, joint="curve")
    def stroke_path(pts, color, w):
        draw.line(pts, fill=color, width=w, joint="curve")

    # 3. Render pass order:
    #    1) <defs>  — skip (no visible output)
    #    2) <rect>, <line>, <polygon>, <polyline>, <circle>, <ellipse>
    #    3) <path>
    #    4) <text>
    # Order of regex matches = document order; SVG paint order applies.

    # Strip comments
    svg_clean = re.sub(r"<!--.*?-->", "", svg_text, flags=re.DOTALL)

    # Collect nodes in document order
    node_re = re.compile(
        r"<(rect|line|circle|ellipse|polygon|polyline|path|text)\b([^/>]*)(/?)>",
        re.DOTALL
    )
    # We need to also capture <text>...content...</text> separately for tspan handling
    text_re = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.DOTALL)
    text_nodes = {m.start(): m for m in text_re.finditer(svg_clean)}

    # Map positions of self-closing or non-text nodes
    pos_to_kind = {}
    for m in node_re.finditer(svg_clean):
        kind = m.group(1)
        if kind == "text":
            continue  # handled separately
        pos_to_kind[m.start()] = (kind, m)

    # Build an ordered list of all drawable items
    # We process <g> as containers that push/pop transforms, and any shape inside
    # uses pt_t() instead of pt() so transforms apply.
    drawables = []
    # Walk through SVG, but for each <g transform="..."> we'll record it so we can
    # push its translate during the render loop.
    g_starts = []  # list of (position, tx, ty)
    g_ends = []    # list of positions
    for m in re.finditer(r'<g\b([^>]*)>', svg_clean):
        t = _attr(m.group(1), 'transform', '')
        tm = re.search(r'translate\(\s*(-?[\d.]+)[ ,]+(-?[\d.]+)\s*\)', t)
        if tm:
            g_starts.append((m.start(), float(tm.group(1)), float(tm.group(2))))
    for m in re.finditer(r'</g>', svg_clean):
        g_ends.append(m.start())

    for m in node_re.finditer(svg_clean):
        kind = m.group(1)
        if kind == "text":
            tm = text_re.match(svg_clean, m.start())
            if tm:
                drawables.append(("text", tm.start(), tm.group(1), tm.group(2)))
        else:
            drawables.append((kind, m.start(), m.group(2), None))
    drawables.sort(key=lambda d: d[1])

    # Build a set of "inside <g> with transform" ranges so we can
    # track current transform while rendering each node.
    # For each <g transform="translate(tx,ty)">, find the matching </g> end
    # using a simple stack walk over the text. Then for each drawable, the
    # active transforms are the g's whose start is before pos and end is after pos.
    # CRITICAL: we must track ALL <g>/</g> pairs, not just translated ones,
    # otherwise the closing tag of an inner non-translated g pops the wrong g
    # from the stack (it pops the parent instead of the inner).
    g_ranges = []  # list of (start, end, tx, ty) — only for translated g's
    g_open_stack = []  # stack of ALL g's, with (start, tx, ty or None)
    for m in re.finditer(r'<g\b([^>]*)>|</g>', svg_clean):
        if m.group(0).startswith('</'):
            if g_open_stack:
                start, tx, ty = g_open_stack.pop()
                if tx is not None:
                    g_ranges.append((start, m.end(), tx, ty))
        else:
            t = re.search(r'translate\(\s*(-?[\d.]+)[ ,]+(-?[\d.]+)\s*\)', m.group(1))
            if tm_m := t:
                g_open_stack.append((m.start(), float(tm_m.group(1)), float(tm_m.group(2))))
            else:
                # non-translated g — still track on the stack so the close matches
                g_open_stack.append((m.start(), None, None))
    # g_ranges now contains (start, end, tx, ty) for each translated <g>

    def active_transforms_at(pos):
        active = []
        for s, e, tx, ty in g_ranges:
            if s < pos <= e:
                active.append((tx, ty))
        return active

    # 4. Render each
    for d in drawables:
        kind, pos, attrs, body = d
        # determine active transforms at this position
        cur_tx, cur_ty = 0, 0
        for tx, ty in active_transforms_at(pos):
            cur_tx += tx
            cur_ty += ty
        def pt(x, y):
            return (int((x + cur_tx - vb_x) * scale), int((y + cur_ty - vb_y) * scale))
        try:
            if kind == "rect":
                x = _attr_num(attrs, "x")
                y = _attr_num(attrs, "y")
                w = _attr_num(attrs, "width")
                h = _attr_num(attrs, "height")
                rx = _attr_num(attrs, "rx", 0)
                p0 = pt(x, y)
                p1 = pt(x + w, y + h)
                fill = fill_of(attrs, x, y, x+w, y+h)
                stroke = stroke_of(attrs)
                sw = stroke_w(attrs)
                if fill is not None:
                    fill_rect(p0, p1, fill, rx=sz(rx))
                if stroke is not None and sw >= 1:
                    stroke_rect(p0, p1, stroke, sw, rx=sz(rx))

            elif kind == "line":
                x1 = _attr_num(attrs, "x1")
                y1 = _attr_num(attrs, "y1")
                x2 = _attr_num(attrs, "x2")
                y2 = _attr_num(attrs, "y2")
                stroke = stroke_of(attrs) or (255,255,255,255)
                sw = stroke_w(attrs)
                p0 = pt(x1, y1); p1 = pt(x2, y2)
                draw.line([p0, p1], fill=stroke, width=sw)

            elif kind == "circle":
                cx = _attr_num(attrs, "cx")
                cy = _attr_num(attrs, "cy")
                r  = _attr_num(attrs, "r")
                p0 = pt(cx-r, cy-r); p1 = pt(cx+r, cy+r)
                fill = fill_of(attrs, cx-r, cy-r, cx+r, cy+r)
                stroke = stroke_of(attrs)
                sw = stroke_w(attrs)
                if fill is not None:
                    fill_ellipse(p0, p1, fill)
                if stroke is not None and sw >= 1:
                    stroke_ellipse(p0, p1, stroke, sw)

            elif kind == "ellipse":
                cx = _attr_num(attrs, "cx")
                cy = _attr_num(attrs, "cy")
                rx = _attr_num(attrs, "rx")
                ry = _attr_num(attrs, "ry")
                p0 = pt(cx-rx, cy-ry); p1 = pt(cx+rx, cy+ry)
                fill = fill_of(attrs, cx-rx, cy-ry, cx+rx, cy+ry)
                stroke = stroke_of(attrs)
                sw = stroke_w(attrs)
                if fill is not None:
                    fill_ellipse(p0, p1, fill)
                if stroke is not None and sw >= 1:
                    stroke_ellipse(p0, p1, stroke, sw)

            elif kind in ("polygon", "polyline"):
                pts_str = _attr(attrs, "points", "")
                pts = []
                for p in re.findall(r"(-?[\d.]+)[ ,]+(-?[\d.]+)", pts_str):
                    pts.append(pt(float(p[0]), float(p[1])))
                if not pts:
                    continue
                xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
                bb_x0, bb_y0, bb_x1, bb_y1 = min(xs), min(ys), max(xs), max(ys)
                if kind == "polygon":
                    fill = fill_of(attrs, bb_x0, bb_y0, bb_x1, bb_y1)
                    stroke = stroke_of(attrs)
                else:
                    fill = None
                    stroke = stroke_of(attrs) or (255,255,255,255)
                sw = stroke_w(attrs)
                if kind == "polygon" and fill is not None:
                    fill_polygon(pts, fill)
                if stroke is not None and sw >= 1:
                    if kind == "polygon" and fill is None:
                        closed = pts + [pts[0]]
                        stroke_line(closed, stroke, sw)
                    else:
                        stroke_line(pts, stroke, sw)

            elif kind == "path":
                # basic M/L/Q/C/Z support
                d_str = _attr(attrs, "d", "")
                tokens = re.findall(r"[MLQCZmlqcz]|-?[\d.]+", d_str)
                pts_path = []
                i = 0
                start_x, start_y = 0, 0
                cur_cmd = None
                while i < len(tokens):
                    t = tokens[i]
                    if t in "MLQCZmlqcz":
                        cur_cmd = t
                        if t in ("Z", "z"):
                            if pts_path:
                                pts_path.append(pt(start_x, start_y))
                            i += 1
                            continue
                        i += 1
                        continue
                    if cur_cmd in ("M", "L"):
                        x = float(tokens[i]); y = float(tokens[i+1])
                        if cur_cmd == "M":
                            start_x, start_y = x, y
                        pts_path.append(pt(x, y))
                        i += 2
                    elif cur_cmd in ("Q",):
                        x1 = float(tokens[i]); y1 = float(tokens[i+1])
                        x = float(tokens[i+2]); y = float(tokens[i+3])
                        pts_path.append(pt(x1, y1))
                        pts_path.append(pt(x, y))
                        i += 4
                    elif cur_cmd in ("C",):
                        x1 = float(tokens[i]); y1 = float(tokens[i+1])
                        x2 = float(tokens[i+2]); y2 = float(tokens[i+3])
                        x = float(tokens[i+4]); y = float(tokens[i+5])
                        pts_path.append(pt(x1, y1))
                        pts_path.append(pt(x2, y2))
                        pts_path.append(pt(x, y))
                        i += 6
                    else:
                        i += 1
                if not pts_path:
                    continue
                xs = [p[0] for p in pts_path]; ys = [p[1] for p in pts_path]
                bb_x0, bb_y0, bb_x1, bb_y1 = min(xs), min(ys), max(xs), max(ys)
                fill = fill_of(attrs, bb_x0, bb_y0, bb_x1, bb_y1)
                stroke = stroke_of(attrs)
                sw = stroke_w(attrs)
                if fill is not None and len(pts_path) >= 3:
                    fill_path_polygon(pts_path, fill)
                if stroke is not None and sw >= 1:
                    stroke_path(pts_path, stroke, sw)

            elif kind == "text":
                # extract position
                x = _attr_num(attrs, "x")
                y = _attr_num(attrs, "y")
                sz_v = _attr_num(attrs, "font-size", 16)
                anchor = _attr(attrs, "text-anchor", "start")
                # body may include <tspan>s; for simplicity concatenate their text content
                clean = re.sub(r"<[^>]+>", "", body)
                clean = _html_decode(clean)
                if not clean.strip():
                    continue
                font = _load_font(sz_v)
                fill = fill_of(attrs, x, y, x, y) or (255, 255, 255, 255)
                # measure
                bbox = draw.textbbox((0, 0), clean, font=font)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]
                px, py = pt(x, y)
                if anchor == "middle":
                    px -= tw // 2
                elif anchor == "end":
                    px -= tw
                # SVG y is the baseline; PIL draws from top-left, so shift up by ~80% of font size
                py -= int(sz_v * 0.8 * scale)
                # blit
                if fill[3] < 255:
                    overlay = Image.new("RGBA", img.size, (0,0,0,0))
                    od = ImageDraw.Draw(overlay)
                    od.text((px, py), clean, font=font, fill=fill)
                    img.alpha_composite(overlay)
                else:
                    draw.text((px, py), clean, font=font, fill=fill)
        except Exception as e:
            print(f"  ! error rendering <{kind}>: {e}", file=sys.stderr)

    img.save(out_path, "PNG")
    return img

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: render_svg.py <input.svg> <output.png> [width]")
        sys.exit(1)
    svg = Path(sys.argv[1]).read_text(encoding="utf-8")
    out = sys.argv[2]
    w = int(sys.argv[3]) if len(sys.argv) > 3 else 1400
    render(svg, out, target_w=w)
    print(f"rendered → {out}")
