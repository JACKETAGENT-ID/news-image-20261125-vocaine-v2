#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261125 (vocaine v2).

Concept: world map + 5 region panels + 'By The Numbers' strip.
All 37 headlines were verified against news reported on Wednesday
25 November 2026 (see NOTES.md for a source per story).
Drawn from scratch with PIL only; no external assets.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

def bold(sz):
    return ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf"), sz)

def reg(sz):
    return ImageFont.truetype(os.path.join(FONT_DIR, "DejaVuSans.ttf"), sz)

# ---------------------------------------------------------------- stories
PANELS = [
    ("THE AMERICAS", "#8C2F39", [
        "US unveils new tariffs on 14 partners, rates of 20-40%",
        "Wall Street slides, then recovers: S&P -0.25%, Nasdaq -0.62%",
        "Trump: US war funding against Iran secured through January",
        "Nvidia falls 4% as AI sell-off deepens; Huang apologises",
        "CIA and ODNI hit by cyber breach of unclassified data",
        "US charges 800+ in global anti-scam crackdown, 400 cases",
        "Coast Guard recovers all six from Cessna crash off Mississippi",
        "First Thanksgiving Eve NFL game: Packers at Rams on Netflix",
    ]),
    ("EUROPE", "#1F4E79", [
        "Abu Dhabi Ukraine talks end with no deal, no concessions",
        "Zelensky rejects Lukashenko's offer of a Moscow escort",
        "EU to join next Ukraine peace talks, von der Leyen says",
        "Russia fires 160+ drones and missiles at Ukraine's energy grid",
        "BBC: leaked data puts Russian war dead at 490,334",
        "Champions League: PSG 2-2 Roma; Lille stun Bayern 2-1",
        "Liverpool cruise 3-0 at Brugge; Barca win 4-1 at Sabah",
        "France's 2027 hopefuls clash in three-hour TV debate",
    ]),
    ("MIDDLE EAST & AFRICA", "#8A6D00", [
        "Two oil tankers hit by mines in Strait of Hormuz, catch fire",
        "Iran claims it shot down two US drones over Hormuz",
        "Houthi strike hits Riyadh's tallest tower; 11 wounded",
        "Houthis attack Saudi Arabia's Ras Tanura oil refinery",
        "Israel kills Hamas security chief Abuelouf in Gaza strike",
        "Sudan: RSF drone strikes kill 19 civilians, wound 20",
        "Ten die in bus-truck crash in southern Egypt",
        "ECOWAS approves regional security force roadmap to 2027",
    ]),
    ("ASIA", "#2E6B34", [
        "Shenzhou-24 docks; Pakistan's first astronaut reaches orbit",
        "Huawei convicted in US trial over Iran business",
        "Bangladesh raises garment wage 36% to $139 after protests",
        "Taiwan comic fires back at China's anger over his jokes",
        "India thrash Japan 4-0 to sweep women's hockey group",
        "India, Malaysia armies drill hostage rescue in Harimau Shakti",
        "26 miners feared trapped in illegal gold mine in Indonesia",
        "Myanmar rebel with artificial leg vows to fight on",
    ]),
    ("OCEANIA & THE PACIFIC", "#0E6B6B", [
        "Solomon Islands and Australia sign treaty barring foreign military bases",
        "China swipes at Australia after Solomons ends security pact with Beijing",
        "Pope Leo XIV laments failure of COP31 climate talks",
        "Pacific nations despair as COP31 ends with no deal",
        "Australia's climate minister Bowen under fire over COP31 collapse",
    ]),
]

NUMBERS = [
    ("-0.25%", "S&P 500 close after a -3.2% morning plunge"),
    ("$57,209", "Bitcoin intraday low; recovered to ~$60,300"),
    ("$84.10", "WTI oil, up 2.5% on Hormuz fears"),
    ("490,334", "Russian soldiers dead since 2022: leaked data"),
    ("160+", "Russian drones & missiles fired overnight"),
    ("36%", "Bangladesh garment minimum-wage rise"),
]

# Simplified continent outlines as (lon, lat) polygons.
CONTINENTS = [
    # North America
    [(-168, 66), (-150, 70), (-135, 69), (-125, 71), (-115, 68), (-105, 68),
     (-95, 69), (-85, 66), (-80, 73), (-70, 62), (-60, 55), (-55, 52),
     (-60, 47), (-65, 44), (-70, 42), (-75, 35), (-80, 32), (-81, 26),
     (-84, 30), (-90, 21), (-95, 16), (-100, 16), (-105, 20), (-110, 23),
     (-115, 29), (-120, 34), (-125, 40), (-125, 49), (-130, 54), (-140, 60),
     (-150, 59), (-158, 58), (-165, 60), (-168, 66)],
    # Greenland
    [(-58, 64), (-45, 60), (-40, 64), (-32, 68), (-25, 70), (-30, 74),
     (-45, 76), (-58, 74), (-58, 64)],
    # South America
    [(-80, 10), (-77, 5), (-75, 2), (-70, 8), (-62, 9), (-55, 6), (-50, 4),
     (-44, 0), (-38, -5), (-35, -8), (-38, -15), (-40, -21), (-46, -24),
     (-50, -28), (-55, -34), (-60, -38), (-65, -42), (-68, -48), (-70, -53),
     (-73, -50), (-73, -40), (-73, -30), (-72, -20), (-75, -15), (-78, -8),
     (-80, -2), (-80, 10)],
    # Europe
    [(-10, 36), (-9, 38), (-9, 43), (-2, 44), (-1, 46), (-4, 48), (-1, 50),
     (2, 51), (5, 53), (8, 55), (8, 58), (10, 59), (13, 56), (18, 56),
     (21, 55), (24, 58), (25, 60), (28, 62), (30, 64), (32, 70), (38, 68),
     (44, 68), (44, 64), (40, 60), (38, 56), (35, 54), (32, 51), (30, 48),
     (28, 45), (26, 44), (23, 40), (23, 37), (20, 39), (19, 42), (15, 44),
     (12, 44), (8, 44), (6, 43), (3, 42), (0, 39), (-2, 37), (-6, 36),
     (-9, 37), (-10, 36)],
    # Africa
    [(-17, 15), (-16, 20), (-15, 27), (-10, 31), (-6, 34), (-2, 35),
     (5, 37), (10, 37), (11, 34), (15, 32), (20, 32), (25, 32), (30, 31),
     (32, 31), (34, 28), (36, 24), (38, 20), (39, 15), (42, 12), (45, 11),
     (48, 11), (51, 12), (48, 6), (44, 2), (41, -2), (40, -7), (38, -12),
     (36, -18), (33, -22), (32, -26), (29, -30), (27, -33), (22, -35),
     (19, -34), (16, -30), (14, -24), (12, -18), (13, -12), (12, -8),
     (9, 4), (6, 4), (0, 6), (-5, 5), (-8, 5), (-12, 8), (-15, 11),
     (-17, 15)],
    # Asia
    [(28, 41), (32, 41), (36, 42), (40, 43), (44, 42), (48, 44), (50, 46),
     (55, 46), (58, 48), (62, 50), (66, 51), (70, 54), (74, 57), (78, 61),
     (80, 66), (84, 69), (88, 71), (92, 73), (96, 75), (100, 76), (104, 77),
     (108, 76), (112, 74), (116, 73), (120, 73), (124, 72), (128, 71),
     (132, 71), (136, 72), (140, 72), (144, 71), (148, 70), (152, 70),
     (156, 68), (160, 66), (164, 66), (168, 66), (172, 65), (176, 65),
     (178, 64), (173, 62), (170, 60), (166, 60), (162, 58), (158, 52),
     (156, 51), (152, 55), (150, 59), (146, 59), (142, 55), (141, 50),
     (140, 45), (138, 42), (135, 42), (132, 38), (130, 35), (127, 35),
     (126, 38), (124, 33), (122, 30), (121, 28), (119, 25), (116, 23),
     (113, 22), (110, 20), (108, 18), (106, 12), (105, 9), (103, 8),
     (101, 7), (100, 10), (98, 14), (97, 16), (95, 16), (93, 18), (92, 21),
     (90, 22), (88, 22), (86, 20), (84, 19), (81, 16), (80, 13), (78, 8),
     (76, 9), (75, 12), (73, 16), (72, 20), (70, 22), (68, 23), (66, 25),
     (64, 25), (62, 25), (60, 25), (58, 26), (56, 27), (54, 27), (52, 28),
     (50, 29), (48, 30), (46, 30), (44, 29), (42, 29), (40, 31), (38, 33),
     (36, 36), (33, 36), (30, 36), (28, 41)],
    # Australia
    [(113, -22), (114, -28), (114, -32), (115, -35), (118, -35), (121, -34),
     (124, -33), (127, -32), (130, -32), (132, -32), (134, -33), (136, -35),
     (138, -35), (140, -38), (143, -39), (146, -39), (149, -37), (150, -37),
     (152, -33), (153, -30), (153, -27), (151, -24), (150, -23), (148, -20),
     (146, -19), (144, -15), (142, -11), (141, -13), (139, -15), (137, -12),
     (136, -15), (135, -15), (133, -12), (131, -12), (130, -13), (128, -14),
     (126, -14), (124, -15), (122, -17), (120, -20), (117, -21), (115, -22),
     (113, -22)],
    # Japan
    [(130, 31), (131, 32), (132, 33), (134, 34), (136, 34), (138, 35),
     (139, 36), (140, 38), (141, 40), (141, 42), (143, 44), (142, 42),
     (141, 39), (140, 37), (138, 35), (136, 33), (134, 33), (132, 32),
     (130, 31)],
    # New Zealand
    [(167, -45), (168, -44), (170, -42), (172, -41), (174, -40), (176, -38),
     (178, -38), (176, -39), (174, -41), (172, -43), (170, -45), (168, -46),
     (167, -45)],
    # United Kingdom
    [(-5, 50), (-4, 51), (-3, 53), (-4, 55), (-5, 56), (-4, 58), (-2, 58),
     (-1, 57), (0, 55), (0, 53), (-1, 51), (-3, 50), (-5, 50)],
    # Indonesia (rough)
    [(95, 5), (98, 3), (101, 0), (104, -3), (106, -6), (110, -7), (113, -8),
     (116, -9), (119, -9), (120, -10), (119, -8), (116, -7), (112, -7),
     (108, -6), (105, -4), (102, 0), (98, 3), (95, 5)],
]

# Red dots: (lon, lat) of flashpoints.
DOTS = [(57, 26), (47, 25), (34, 31), (30, 50), (30, 46), (-77, 39),
        (160, -9), (100, 14)]

MAP_LABELS = [
    ("NORTH AMERICA", -105, 58), ("SOUTH AMERICA", -62, -18),
    ("EUROPE", 8, 60), ("AFRICA", 18, 8), ("ASIA", 88, 58),
    ("OCEANIA", 138, -32),
]

NAVY = "#0B2545"
PAPER = "#F6F1E6"
GOLD = "#E8B84B"


def project(lon, lat, x0, y0, w, h):
    x = x0 + (lon + 170.0) / 360.0 * w
    y = y0 + (75.0 - lat) / 130.0 * h
    return (x, y)


def wrap(draw, text, font, max_w):
    words = text.split(" ")
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_panel(draw, x, y, w, h, title, color, stories, body_font, head_font,
               line_h=17):
    draw.rectangle([x, y, x + w - 1, y + h - 1], fill="white",
                   outline="#CFC7B4", width=1)
    draw.rectangle([x, y, x + w - 1, y + 31], fill=color)
    draw.text((x + 12, y + 7), title, font=head_font, fill="white")
    n = str(len(stories))
    tw = draw.textlength(n + " STORIES", font=reg(11))
    draw.text((x + w - 12 - tw, y + 10), n + " STORIES", font=reg(11),
              fill="#F2E6C8")
    ty = y + 31 + 7
    for story in stories:
        lines = wrap(draw, story, body_font, w - 34)
        for i, ln in enumerate(lines):
            if i == 0:
                draw.ellipse([x + 12, ty + 5, x + 17, ty + 10], fill=color)
            draw.text((x + 22, ty), ln, font=body_font, fill="#1F1F1F")
            ty += line_h
        ty += 1
    return ty


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- header ----
    d.rectangle([0, 0, W - 1, 99], fill=NAVY)
    d.rectangle([0, 99, W - 1, 101], fill=GOLD)
    title = "WEDNESDAY, 25 NOVEMBER 2026"
    tf = bold(40)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 12), title, font=tf, fill="white")
    sub = "THE WORLD IN ONE DAY  ·  37 STORIES FROM EVERY CONTINENT"
    sf = bold(16)
    sw = d.textlength(sub, font=sf)
    d.text(((W - sw) / 2, 62), sub, font=sf, fill=GOLD)

    # ---- world map band ----
    mx0, my0, mw, mh = 16, 106, 992, 150
    d.rectangle([mx0 - 4, my0 - 4, mx0 + mw + 4, my0 + mh + 4],
                fill="#A9C6D8", outline="#8FA9BC", width=1)
    for poly in CONTINENTS:
        pts = [project(lon, lat, mx0, my0, mw, mh) for lon, lat in poly]
        d.polygon(pts, fill="#3E7C59", outline="#2C5A40")
    for lon, lat in DOTS:
        px, py = project(lon, lat, mx0, my0, mw, mh)
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill="#C0392B",
                  outline="white", width=1)
    for label, lon, lat in MAP_LABELS:
        px, py = project(lon, lat, mx0, my0, mw, mh)
        f = bold(11)
        lw = d.textlength(label, font=f)
        d.text((px - lw / 2, py - 6), label, font=f, fill="#123A24")
    cap = "War in the Gulf  ·  Markets in turmoil  ·  History in orbit"
    cf = reg(12)
    cw = d.textlength(cap, font=cf)
    d.text(((W - cw) / 2, my0 + mh + 8), cap, font=cf, fill="#4A4438")

    # ---- region panels ----
    body_font = reg(13)
    head_font = bold(17)
    gap = 8
    col_w = (W - 24 - gap) // 2
    x0, x1 = 12, 12 + col_w + gap
    y_top = 284
    row_h = 196
    draw_panel(d, x0, y_top, col_w, row_h, PANELS[0][0], PANELS[0][1],
               PANELS[0][2], body_font, head_font)
    draw_panel(d, x1, y_top, col_w, row_h, PANELS[1][0], PANELS[1][1],
               PANELS[1][2], body_font, head_font)
    y2 = y_top + row_h + gap
    draw_panel(d, x0, y2, col_w, row_h, PANELS[2][0], PANELS[2][1],
               PANELS[2][2], body_font, head_font)
    draw_panel(d, x1, y2, col_w, row_h, PANELS[3][0], PANELS[3][1],
               PANELS[3][2], body_font, head_font)
    y3 = y2 + row_h + gap
    draw_panel(d, x0, y3, W - 24, 158, PANELS[4][0], PANELS[4][1],
               PANELS[4][2], body_font, head_font, line_h=22)

    # ---- By The Numbers strip ----
    ny0, ny1 = 850, 952
    d.rectangle([12, ny0, W - 13, ny1], fill=NAVY)
    d.text((24, ny0 + 8), "BY THE NUMBERS", font=bold(13), fill=GOLD)
    cell_w = (W - 24) // 6
    big_f, lab_f = bold(23), reg(11)
    for i, (num, label) in enumerate(NUMBERS):
        cx = 12 + i * cell_w
        if i:
            d.line([cx, ny0 + 30, cx, ny1 - 8], fill="#2A4A6B", width=1)
        nw = d.textlength(num, font=big_f)
        d.text((cx + (cell_w - nw) / 2, ny0 + 32), num, font=big_f,
               fill="white")
        lines = wrap(d, label, lab_f, cell_w - 16)
        ly = ny0 + 62
        for ln in lines:
            lw = d.textlength(ln, font=lab_f)
            d.text((cx + (cell_w - lw) / 2, ly), ln, font=lab_f,
                   fill="#C9D6E4")
            ly += 13

    # ---- footer ----
    f1 = ("All stories first reported Wednesday 25 November 2026  ·  "
          "Sources: Reuters · AP · BBC · UEFA · Investopedia · Nature")
    f1f = reg(12)
    fw = d.textlength(f1, font=f1f)
    d.text(((W - fw) / 2, 962), f1, font=f1f, fill="#5A5346")
    f2 = "ONE DAY  ·  ONE IMAGE  ·  THE WORLD"
    f2f = bold(12)
    fw2 = d.textlength(f2, font=f2f)
    d.text(((W - fw2) / 2, 984), f2, font=f2f, fill="#8C2F39")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
