#!/usr/bin/env python3
"""Draw the front page for Friday 20 November 2026 world news.

A one-page newspaper, "THE WORLD", drawn from scratch with Pillow:
masthead, a Shenzhen-summit lead illustration, the peace-declaration
lead story, three columns (Kyiv, Anthropic, UK drones) and an
"Also on 20 Nov" strip. Every word is drawn from the strings below,
so no text can garble. Output: entry.png, 1024x1024, under 1 MiB.

Usage: python3 render_frontpage.py [out.png]
"""
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (18, 18, 18)
RED = (172, 32, 32)
NAVY = (38, 74, 96)
GOLD = (214, 164, 60)
DUSK = (233, 196, 150)
DUSK2 = (214, 158, 110)
GREY = (90, 90, 90)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(draw, text, font, width):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, font, width, leading, fill=INK):
    lines = wrap_text(draw, text, font, width)
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def hline(draw, y, x0=36, x1=988, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def vline(draw, x, y0, y1, width=1, fill=INK):
    draw.line([(x, y0), (x, y1)], fill=fill, width=width)


def centered(draw, y, text, font, fill=INK):
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2, y), text, font=font, fill=fill)
    return y + font.size + 4


def draw_summit_art(draw, x0, y0, x1, y1):
    """Shenzhen at dusk: sky, sun, skyline, three flags, dove."""
    draw.rectangle([x0, y0, x1, y1], fill=DUSK)
    draw.rectangle([x0, y0 + 118, x1, y1], fill=DUSK2)
    # sun
    cx, cy, r = x0 + 130, y0 + 58, 40
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD)
    # skyline silhouettes
    base = y1
    towers = [(0, 150, 70), (90, 190, 46), (170, 120, 90), (290, 175, 54),
              (370, 135, 84), (480, 185, 48), (560, 125, 96), (690, 170, 60),
              (780, 140, 78), (880, 180, 52)]
    for tx, th, tw in towers:
        draw.rectangle([x0 + tx, base - th, x0 + tx + tw, base],
                       fill=(64, 52, 48))
    # three flag poles
    pole_x = [x0 + 250, x0 + 490, x0 + 730]
    for px in pole_x:
        draw.line([(px, y0 + 22), (px, y0 + 118)], fill=INK, width=4)
    # US flag: stripes + blue canton
    fx, fy = pole_x[0] + 4, y0 + 24
    for i in range(7):
        draw.rectangle([fx, fy + i * 6, fx + 74, fy + i * 6 + 6],
                       fill=RED if i % 2 == 0 else (240, 240, 240))
    draw.rectangle([fx, fy, fx + 32, fy + 24], fill=NAVY)
    # China flag: red with five small stars
    fx = pole_x[1] + 4
    draw.rectangle([fx, fy, fx + 74, fy + 42], fill=RED)
    for sx, sy in [(8, 6), (22, 4), (28, 12), (22, 20), (10, 18)]:
        draw.ellipse([fx + sx, fy + sy, fx + sx + 6, fy + sy + 6],
                     fill=GOLD)
    # Russia flag: white, blue, red bands
    fx = pole_x[2] + 4
    for i, col in enumerate([(240, 240, 240), (28, 68, 142), RED]):
        draw.rectangle([fx, fy + i * 14, fx + 74, fy + i * 14 + 14], fill=col)


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    y = 26
    y = centered(d, y, "THE WORLD", load(SERIF_B, 96))
    hline(d, y + 2, width=3)
    y += 12
    dateline = "FRIDAY, 20 NOVEMBER 2026  ·  ONE DAY'S WORLD NEWS IN ONE PAGE"
    y = centered(d, y, dateline, load(SANS_B, 21))
    hline(d, y + 4, width=1)

    # ---- lead illustration ----
    art_y0 = y + 14
    art_y1 = art_y0 + 180
    draw_summit_art(d, 36, art_y0, 988, art_y1)

    # ---- lead story ----
    y = art_y1 + 14
    y = centered(d, y, "PEACE, ON PAPER", load(SERIF_B, 62), fill=RED)
    deck = ("Trump, Putin and Xi sign a four-point declaration after their "
            "historic Shenzhen summit. Zelensky: no deal without Kyiv.")
    y = draw_wrapped(d, 90, y + 2, deck, load(SERIF_I, 25), 844, 32)
    hline(d, y + 8, width=2)

    # ---- three columns ----
    col_y = y + 20
    col_w = 296
    cols_x = [36, 364, 692]
    columns = [
        ("KYIV UNDER FIRE",
         "Bridges hit as Russia rains missiles on Kyiv",
         "Three bridges struck in an overnight missile and drone attack; "
         "three killed, nine hurt, power cut. A hospital in Kharkiv was "
         "hit too. Europe readies talks — Kyiv sets the terms."),
        ("THE $81BN DEBUT",
         "Anthropic ends day one up 17%",
         "The Claude maker raised $81.3 billion, the largest listing ever, "
         "opening at $111.50 and closing at $97.17. Wider markets slid; "
         "the Dow dipped below 50,000."),
        ("DRONES FOR KYIV",
         "Britain pledges 1,000 drones",
         "London's £260m pledge joins air-defence, energy and financial "
         "aid from nearly 40 partners. Germany, France and Britain say "
         "Europe will join any new talks."),
    ]
    for (x, (kicker, head, body)) in zip(cols_x, columns):
        cy = col_y
        d.text((x, cy), kicker, font=load(SANS_B, 19), fill=RED)
        cy += 26
        cy = draw_wrapped(d, x, cy, head, load(SERIF_B, 28), col_w, 32)
        cy += 4
        draw_wrapped(d, x, cy, body, load(SERIF, 19), col_w, 24)
        if x != cols_x[-1]:
            vline(d, x + col_w + 16, col_y, col_y + 196)
    hline(d, col_y + 210, width=2)

    # ---- also strip ----
    y = col_y + 224
    d.text((36, y), "ALSO ON 20 NOVEMBER", font=load(SANS_B, 20), fill=RED)
    y += 30
    items = [
        "Poland lifts its air-threat warning; unknown objects near the "
        "Ukraine border are being investigated.",
        "The EU will summon Russia's envoy over damage to its Kyiv "
        "embassy in the 19 November strikes.",
        "Trump posthumously pardons baseball legend Pete Rose.",
        "Israel's one-day operation in central Gaza draws a Hamas "
        "ceasefire-violation charge.",
        "Saudi defences down two Houthi drones; a tanker burns after "
        "hitting a mine east of Hormuz.",
        "COP31 draft drops the call to phase out fossil fuels.",
    ]
    half = len(items) // 2
    left, right = items[:half], items[half:]
    for x, group in [(36, left), (512, right)]:
        iy = y
        for it in group:
            iy = draw_wrapped(d, x + 16, iy, "•  " + it,
                              load(SANS, 18), 440, 23)
            iy += 8
    y += 4 * 31 + 4 * 8 + 8

    # ---- footer ----
    hline(d, H - 44, width=1)
    centered(d, H - 36,
             "THE WORLD · Friday 20 November 2026 · Every story as reported on 20 November 2026",
             load(SANS, 15), fill=GREY)

    img.save(out_path, "PNG")
    print(f"wrote {out_path} {img.size}")


if __name__ == "__main__":
    main()
