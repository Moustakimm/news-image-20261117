#!/usr/bin/env python3
"""Renders entry.png (1024x1024) for the news-image-20261117 bounty.

A newspaper front page summing up Tuesday 17 November 2026 in five stories:
the Strait of Hormuz tanker attack and US-Iran strikes, Ukraine's drone
barrage on the Crimea bridge, Wall Street's fourth straight down day, the
COP31 draft deal, and the Western call to open Gaza crossings.

Run:  python3 render.py        (writes ./entry.png beside this file)
Requires Pillow and the DejaVu fonts (standard on this machine).
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 229)
INK = (25, 23, 19)
BODY = (43, 40, 34)
RED = (138, 47, 36)
NAVY = (29, 58, 95)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def wrap(draw, text, f, max_w):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if text_w(draw, trial, f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, lines, f, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=f, fill=fill)
        y += leading
    return y


def centered(draw, cx, y, s, f, fill, tracking=0):
    """Draw text centred on cx, with optional extra tracking between chars."""
    if tracking:
        w = sum(draw.textlength(ch, font=f) + tracking for ch in s) - tracking
        x = cx - w / 2
        for ch in s:
            draw.text((x, y), ch, font=f, fill=fill)
            x += draw.textlength(ch, font=f) + tracking
    else:
        w = draw.textlength(s, font=f)
        draw.text((cx - w / 2, y), s, font=f, fill=fill)


def fit_font(draw, s, path, start, max_w):
    """Largest size <= start whose text fits max_w."""
    size = start
    while size > 10 and draw.textlength(s, font=font(path, size)) > max_w:
        size -= 1
    return font(path, size)


# ---------------------------------------------------------------- lead art
def lead_art():
    im = Image.new("RGB", (470, 300), (29, 58, 95))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 470, 122], fill=(232, 163, 76))          # dusk sky
    d.ellipse([393, 26, 457, 90], fill=(244, 213, 141))          # sun
    d.rectangle([0, 118, 470, 130], fill=(201, 123, 45))         # horizon
    # sea with wave bands
    for y0, col in ((130, (39, 75, 115)), (205, (29, 58, 95)), (238, (22, 50, 79))):
        pts = [(0, y0 + 14)]
        for x in range(0, 471, 20):
            pts.append((x, y0 + 14 + 8 * math.sin(x / 55.0)))
        pts += [(470, 300), (0, 300)]
        d.polygon(pts, fill=col)
    # tanker
    d.rectangle([70, 196, 400, 230], fill=(43, 33, 24))          # hull
    d.rectangle([70, 230, 400, 242], fill=RED)                   # waterline
    d.rectangle([96, 168, 142, 196], fill=(61, 47, 34))
    d.rectangle([150, 172, 206, 196], fill=(74, 58, 40))
    d.rectangle([214, 170, 270, 196], fill=(61, 47, 34))
    d.rectangle([330, 150, 364, 196], fill=(36, 26, 18))         # funnel block
    d.rectangle([338, 138, 356, 152], fill=(36, 26, 18))
    # fire + smoke
    d.polygon([(346, 152), (354, 128), (362, 148), (370, 124),
               (378, 150), (386, 130), (392, 152)], fill=(232, 106, 44))
    for (cx, cy, r, col) in ((340, 118, 14, (92, 85, 72)),
                             (355, 98, 18, (110, 103, 90)),
                             (370, 80, 20, (138, 130, 114))):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    f_lab = font(SANS_B, 21)
    d.text((18, 30), "STRAIT OF HORMUZ", font=f_lab, fill=(122, 31, 22))
    f_sub = font(SANS, 17)
    d.text((18, 268), "IRAN  ————  GULF  ————  OMAN", font=f_sub, fill=(207, 224, 238))
    return im


# ---------------------------------------------------------------- icons
def icon_bridge():
    im = Image.new("RGB", (96, 96), (223, 232, 239))
    d = ImageDraw.Draw(im)
    d.line([(8, 78), (8, 58)], fill=INK, width=5)
    d.line([(88, 78), (88, 58)], fill=INK, width=5)
    d.line([(8, 58), (88, 58)], fill=INK, width=3)
    d.arc([8, 30, 88, 126], start=180, end=360, fill=RED, width=7)
    d.line([(10, 88), (86, 88)], fill=NAVY, width=6)
    for (cx, cy) in ((30, 26), (48, 16), (66, 26)):
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=INK)
    return im


def icon_chart():
    im = Image.new("RGB", (96, 96), (243, 227, 222))
    d = ImageDraw.Draw(im)
    d.line([(10, 26), (32, 40), (52, 34), (74, 62), (88, 70)],
           fill=RED, width=6, joint="curve")
    d.line([(74, 62), (88, 70)], fill=RED, width=5)
    d.line([(88, 56), (88, 70), (74, 70)], fill=RED, width=5)
    d.line([(10, 82), (88, 82)], fill=INK, width=3)
    d.text((12, 4), "-1.6%", font=font(SANS_B, 15), fill=RED)
    return im


def icon_globe():
    im = Image.new("RGB", (96, 96), (226, 236, 221))
    d = ImageDraw.Draw(im)
    d.ellipse([18, 18, 78, 78], fill=NAVY)
    d.pieslice([18, 18, 78, 78], start=180, end=360, fill=(63, 125, 78))
    d.pieslice([18, 18, 78, 78], start=0, end=90, fill=(106, 168, 79))
    d.ellipse([52, 46, 76, 68], fill=(143, 206, 110))
    d.line([(48, 62), (42, 54)], fill=(143, 206, 110), width=3)
    return im


def icon_truck():
    im = Image.new("RGB", (96, 96), (243, 234, 214))
    d = ImageDraw.Draw(im)
    d.line([(14, 30), (82, 30)], fill=INK, width=4)
    d.line([(14, 30), (24, 44)], fill=INK, width=4)
    d.line([(82, 30), (72, 44)], fill=INK, width=4)
    d.rectangle([14, 44, 66, 70], fill=(201, 123, 45))
    d.rectangle([66, 50, 82, 70], fill=RED)
    d.rectangle([20, 50, 60, 64], fill=PAPER)
    d.line([(40, 52), (40, 62)], fill=RED, width=3)
    d.line([(35, 57), (45, 57)], fill=RED, width=3)
    for cx in (28, 58):
        d.ellipse([cx - 8, 66, cx + 8, 82], fill=INK)
    return im


# ---------------------------------------------------------------- page
def main():
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    x0, x1 = 40, 984

    # masthead
    centered(d, W // 2, 34, "THE WORLD IN ONE IMAGE", font(SANS_B, 17), RED, tracking=6)
    title_f = fit_font(d, "TUESDAY 17 NOVEMBER 2026", SERIF, 62, x1 - x0)
    centered(d, W // 2, 62, "TUESDAY 17 NOVEMBER 2026", title_f, INK)
    centered(d, W // 2, 140, "FIVE STORIES  ·  ONE DAY  ·  AROUND THE GLOBE",
             font(SANS, 21), BODY, tracking=2)
    d.line([(x0, 176), (x1, 176)], fill=INK, width=4)
    d.line([(x0, 182), (x1, 182)], fill=INK, width=2)

    # lead story
    ly = 202
    im.paste(lead_art(), (x0, ly))
    tx = 536
    tag = "GULF ON EDGE"
    tf = font(SANS_B, 15)
    tw = d.textlength(tag, font=tf) + 20
    d.rectangle([tx, ly, tx + tw, ly + 28], fill=RED)
    d.text((tx + 10, ly + 5), tag, font=tf, fill=(255, 255, 255))
    y = ly + 40
    y = draw_wrapped(d, tx, y,
                     wrap(d, "Tanker hit in the Strait of Hormuz", font(SERIF, 44), x1 - tx),
                     font(SERIF, 44), INK, 48)
    body = ("A tanker is struck and set ablaze in the world's busiest oil "
            "chokepoint; its crew is evacuated. Iran drones hit a US radar "
            "site in Bahrain, and US jets strike Iranian missile sites on "
            "Qeshm Island.")
    y = draw_wrapped(d, tx, y + 10,
                     wrap(d, body, font(SANS, 21), x1 - tx),
                     font(SANS, 21), BODY, 29)

    # four stories, 2 x 2
    stories = [
        (icon_bridge(),
         "Ukraine's 1,300-drone barrage hits Crimea bridge",
         "Hundreds of drones fired overnight hit the bridge to Crimea. "
         "Russia answers with strikes on two Kyiv bridges, cutting water and power."),
        (icon_chart(),
         "Wall Street falls for a fourth straight day",
         "The Dow drops 1.6% and the S&P 500 slips below its 200-day line "
         "as AI-chip worries deepen ahead of Nvidia's results."),
        (icon_globe(),
         "COP31 draft urges a faster exit from fossil fuels",
         "In Antalya, the first draft deal calls for accelerated action to "
         "phase out fossil fuels — stronger words than the world agreed in 2023."),
        (icon_truck(),
         "West urges Israel to open Gaza crossings",
         "The UK, Australia, Canada and Italy call for rapid humanitarian "
         "access, describing conditions in Gaza as catastrophic."),
    ]
    gy = 560
    col_w = (x1 - x0 - 30) // 2
    for i, (icon, head, body) in enumerate(stories):
        cx = x0 + (i % 2) * (col_w + 30)
        cy = gy + (i // 2) * 200
        d.line([(cx, cy), (cx + col_w, cy)], fill=INK, width=2)
        im.paste(icon, (cx, cy + 14))
        hx = cx + 112
        hw = col_w - 112
        y = draw_wrapped(d, hx, cy + 12,
                         wrap(d, head, font(SERIF, 26), hw),
                         font(SERIF, 26), INK, 29)
        draw_wrapped(d, hx, y + 6,
                     wrap(d, body, font(SANS, 17), hw),
                     font(SANS, 17), BODY, 22)

    # footer
    fy = 972
    d.line([(x0, fy), (x1, fy)], fill=INK, width=4)
    centered(d, W // 2, fy + 12, "TUESDAY 17 NOVEMBER 2026  ·  THE DAY, IN ONE IMAGE",
             font(SANS, 17), BODY, tracking=2)

    im.save("entry.png", format="PNG", optimize=True)
    import os
    size = os.path.getsize("entry.png")
    print(f"wrote entry.png: {size} bytes (limit 1048576), {im.size}")
    assert size <= 1048576, "image exceeds the 1 MiB gate"


if __name__ == "__main__":
    main()
