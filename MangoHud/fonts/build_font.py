"""Gera a fonte do MangoHud com logos de marca em codepoints Latin-1
(o MangoHud só carrega o range Latin por padrão, então ícones no PUA não aparecem).

  U+00A4 (¤) -> logo AMD      U+00A5 (¥) -> logo NVIDIA
  U+00A6 (¦) -> logo Intel    U+00A7 (§) -> logo CachyOS

Uso (na pasta deste script):
  uv run --with fonttools python build_font.py \
      /usr/share/fonts/TTF/JetBrainsMonoNerdFont-Bold.ttf MangoHUD-Brand-Bold.ttf
Requer a JetBrains Mono Nerd Font (pacote ttf-jetbrains-mono-nerd).
"""
import os, re, sys
from fontTools.ttLib import TTFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.svgLib.path import parse_path

here = os.path.dirname(os.path.abspath(__file__))
src, dst = sys.argv[1], sys.argv[2]
font = TTFont(src)
upm = font["head"].unitsPerEm
cap = font["OS/2"].sCapHeight or int(upm * 0.73)
glyf, hmtx = font["glyf"], font["hmtx"]
order = font.getGlyphOrder()
gset = font.getGlyphSet()


def split_contours(rec):
    contours, cur = [], []
    for op, args in rec.value:
        cur.append((op, args))
        if op in ("closePath", "endPath"):
            contours.append(cur); cur = []
    return contours


def bounds(ops):
    r = RecordingPen(); r.value = ops
    b = BoundsPen(None); r.replay(b)
    return b.bounds


def from_svg(name):
    d = re.search(r'<path d="([^"]+)"', open(os.path.join(here, name)).read()).group(1)
    rec = RecordingPen(); parse_path(d, rec)
    contours = split_contours(rec)
    if name == "amd.svg":  # só a seta, sem o texto "AMD"
        contours = [c for c in contours if bounds(c)[0] > 17]
    rec.value = [x for c in contours for x in c]
    return rec, True          # True = eixo y para baixo (SVG)


def from_glyph(gname):
    rec = RecordingPen(); gset[gname].draw(rec)
    return rec, False


LOGOS = {
    0x00A4: ("amd", lambda: from_svg("amd.svg"), 1.08),
    0x00A5: ("nvidia", lambda: from_svg("nvidia.svg"), 1.08),
    0x00A6: ("intel", lambda: from_svg("intel.svg"), 1.08),
    0x00A7: ("cachyos", lambda: from_glyph(font.getBestCmap()[0xF385]), 1.30),
}

for cp, (label, load, scale) in LOGOS.items():
    rec, y_down = load()
    x0, y0, x1, y1 = bounds(rec.value)
    h = cap * scale
    s = h / max(y1 - y0, x1 - x0)
    w = (x1 - x0) * s
    hh = (y1 - y0) * s
    pad = upm * 0.06
    base = -(hh - cap) / 2       # centraliza verticalmente em relação às maiúsculas
    if y_down:
        m = (s, 0, 0, -s, pad - x0 * s, y1 * s + base)
    else:
        m = (s, 0, 0, s, pad - x0 * s, -y0 * s + base)
    pen = TTGlyphPen(None)
    rec.replay(TransformPen(pen, m))
    name = f"brand_{label}"
    glyf[name] = pen.glyph()
    if name not in order:
        order.append(name)
    hmtx[name] = (int(w + 2 * pad), int(pad))
    for table in font["cmap"].tables:
        if table.isUnicode():
            table.cmap[cp] = name

font.setGlyphOrder(order)
font["maxp"].numGlyphs = len(order)
for rec in font["name"].names:
    if rec.nameID in (1, 4, 16):
        rec.string = "MangoHUD Brand Mono"
font.save(dst)
print("ok", dst)
