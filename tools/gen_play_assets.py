#!/usr/bin/env python3
"""Genera los HTML fuente de los recursos de Google Play (página de desarrollador
e iconos de las apps). Después, captura cada uno con un Chromium headless
(ver tools/render_play_assets.sh)."""

import pathlib
import random

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "play-assets" / "_src"
SRC.mkdir(parents=True, exist_ok=True)

random.seed(7)

PAGE = """<!doctype html>
<html><head><meta charset="utf-8">
<style>html,body{margin:0;padding:0;overflow:hidden}svg{display:block}</style>
</head><body>@SVG@</body></html>
"""

SKY_DEFS = """<defs>
<radialGradient id="sky" cx="50%" cy="62%" r="85%">
<stop offset="0%" stop-color="#0f2740"/>
<stop offset="55%" stop-color="#0a1a2d"/>
<stop offset="100%" stop-color="#07101d"/>
</radialGradient>
</defs>"""

BRAND_GLYPH = """<path d="M362 150 A150 150 0 1 0 362 362" fill="none" stroke="#3fd0e0" stroke-width="64" stroke-linecap="round"/>
<circle cx="406" cy="256" r="28" fill="#eaf6f8"/>"""

SAT = '<circle cx="398" cy="120" r="22" fill="#eaf6f8"/>'

GLYPHS = {
    "developer-icon": BRAND_GLYPH,
    "app-oremus": (
        '<path d="M256 118 C322 196 344 250 344 306 A88 88 0 0 1 168 306 '
        'C168 250 190 196 256 118 Z" fill="#3fd0e0"/>'
        '<path d="M256 252 C284 286 294 308 294 330 A38 38 0 0 1 218 330 '
        'C218 308 228 286 256 252 Z" fill="#0a1a2d"/>' + SAT
    ),
    "app-constitucion": (
        '<path d="M248 198 C206 174 148 168 112 176 L112 332 C148 324 206 330 248 354 Z" '
        'fill="#3fd0e0" stroke="#3fd0e0" stroke-width="16" stroke-linejoin="round"/>'
        '<path d="M264 198 C306 174 364 168 400 176 L400 332 C364 324 306 330 264 354 Z" '
        'fill="#3fd0e0" stroke="#3fd0e0" stroke-width="16" stroke-linejoin="round"/>' + SAT
    ),
    "app-auxiliar-administrativo": (
        '<path d="M185 140 H281 L349 208 V350 Q349 372 327 372 H185 Q163 372 163 350 '
        'V162 Q163 140 185 140 Z" fill="#3fd0e0"/>'
        '<path d="M281 140 L349 208 H281 Z" fill="#9fe6ef"/>'
        '<path d="M209 268 L243 302 L307 230" stroke="#0a1a2d" stroke-width="26" '
        'fill="none" stroke-linecap="round" stroke-linejoin="round"/>' + SAT
    ),
}

for name, glyph in GLYPHS.items():
    svg = (
        '<svg width="512" height="512" viewBox="0 0 512 512" '
        'xmlns="http://www.w3.org/2000/svg">'
        + SKY_DEFS
        + '<rect width="512" height="512" fill="url(#sky)"/>'
        + glyph
        + "</svg>"
    )
    (SRC / f"{name}.html").write_text(PAGE.replace("@SVG@", svg), encoding="utf-8")

W, H = 4096, 2304
stars = "".join(
    f'<circle cx="{random.uniform(0, W):.0f}" cy="{random.uniform(0, H * 0.92):.0f}" '
    f'r="{random.uniform(2, 6.5):.1f}" fill="#cfeef3" '
    f'opacity="{random.uniform(0.25, 0.85):.2f}"/>'
    for _ in range(150)
)

header_svg = f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
<defs>
<radialGradient id="sky" cx="50%" cy="58%" r="80%">
<stop offset="0%" stop-color="#0f2740"/>
<stop offset="55%" stop-color="#0a1a2d"/>
<stop offset="100%" stop-color="#07101d"/>
</radialGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%">
<stop offset="0%" stop-color="#3fd0e0" stop-opacity="0.16"/>
<stop offset="100%" stop-color="#3fd0e0" stop-opacity="0"/>
</radialGradient>
<linearGradient id="title" x1="0" y1="0" x2="0" y2="1">
<stop offset="0.2" stop-color="#ffffff"/>
<stop offset="1" stop-color="#9fd9e3"/>
</linearGradient>
<linearGradient id="streak" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#cfeef3" stop-opacity="0"/>
<stop offset="1" stop-color="#cfeef3" stop-opacity="0.8"/>
</linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
{stars}
<line x1="420" y1="330" x2="860" y2="430" stroke="url(#streak)" stroke-width="6" stroke-linecap="round"/>
<ellipse cx="2048" cy="2540" rx="2750" ry="980" fill="url(#glow)"/>
<g transform="translate(575.6,537.6) scale(2.4)">{BRAND_GLYPH}</g>
<text x="1750" y="1210" font-family="-apple-system,'SF Pro Display','Helvetica Neue',Arial,sans-serif" font-size="330" font-weight="500" letter-spacing="66" fill="url(#title)">CAELYN</text>
<text x="1760" y="1390" font-family="-apple-system,'SF Pro Display','Helvetica Neue',Arial,sans-serif" font-size="96" font-weight="500" letter-spacing="58" fill="#3fd0e0">TECH</text>
<text x="1760" y="1565" font-family="-apple-system,'SF Pro Display','Helvetica Neue',Arial,sans-serif" font-size="96" fill="#8aa0ad">Tecnología y desarrollo de aplicaciones</text>
</svg>"""

(SRC / "header.html").write_text(PAGE.replace("@SVG@", header_svg), encoding="utf-8")

print("HTML generados en", SRC)
