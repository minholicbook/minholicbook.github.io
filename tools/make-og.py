# -*- coding: utf-8 -*-
"""og.png(소셜 공유 미리보기)와 파비콘·앱 아이콘을 생성한다.

사이트 자체는 빌드 과정이 없다. 이 스크립트는 페이지를 만드는 도구가 아니라
**PNG 이미지만 굽는 도구**다. index.html 은 이 스크립트와 무관하게 그대로 동작한다.

    python tools/make-og.py            # og.png + 아이콘 4개 전부
    python tools/make-og.py . og       # og.png 만
    python tools/make-og.py . icons    # 아이콘만

왜 필요한가 — 인라인 SVG 는 CSS 토큰을 상속하지만 PNG 는 굽힌 이미지라
`:root` 색을 바꿔도 따라오지 않는다. 팔레트나 히어로 문구를 고치면
여기 상수도 같이 고치고 다시 실행해야 사이트와 공유 미리보기가 어긋나지 않는다.

윈도우 전용 — `C:/Windows/Fonts` 의 맑은 고딕·Consolas 를 쓴다.
다른 OS 에서는 FONT_DIR 과 아래 폰트 파일명을 바꿔야 한다.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

# 저장소 루트 = 이 파일(<루트>/tools/make-og.py)의 두 단계 위.
# 절대 경로를 하드코딩하면 다른 사람이 클론했을 때 바로 깨진다.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else ROOT
ONLY = sys.argv[2] if len(sys.argv) > 2 else "all"

SS = 2  # 슈퍼샘플링 배율. 2배로 그린 뒤 LANCZOS 로 줄여야 얇은 선이 깨지지 않는다.

# index.html :root 과 같은 값을 쓴다. 한쪽만 바꾸면 사이트와 공유 이미지가 어긋난다.
ARTBOARD = "#FFFFFF"
WASH = "#F3F8F1"
INK = "#17181C"
BODY = "#3E453F"
MUTED = "#697169"
RULE = "#E3E9E0"
RED = "#CE2E22"
GREEN = "#35803E"

FONT_DIR = "C:/Windows/Fonts/"
KR_B, KR_L = "malgunbd.ttf", "malgunsl.ttf"   # 한글 — 웹폰트(IBM Plex Sans KR) 대체
MONO = "consola.ttf"                          # 모노 — 웹폰트(IBM Plex Mono) 대체
# Consolas 에는 한글 글리프가 없다. 모노로 그리는 텍스트에 한글을 넣으면 안 된다.

W, H = 1200, 630

IMAGES = os.path.join(ROOT, "images")
LOGO_MARK = os.path.join(IMAGES, "logo-mark.png")        # 원피스 마크 선 그림 (투명 PNG)
LOGO_SIL = os.path.join(IMAGES, "logo-silhouette.png")   # 외곽을 채운 실루엣. 16px 에서만 쓴다
COVER = os.path.join(IMAGES, "cover-digital-fashion-design.jpg")


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, int(size * SS))


def make_canvas(w, h, bg):
    img = Image.new("RGB", (int(w * SS), int(h * SS)), bg)
    return img, ImageDraw.Draw(img)


def line(d, x1, y1, x2, y2, fill, width=1):
    d.line([(x1 * SS, y1 * SS), (x2 * SS, y2 * SS)], fill=fill, width=max(1, int(round(width * SS))))


def rect(d, x, y, w, h, outline=None, fill=None, width=1):
    d.rectangle([(x * SS, y * SS), ((x + w) * SS, (y + h) * SS)],
                outline=outline, fill=fill, width=max(1, int(round(width * SS))))


def text(d, x, y, s, fnt, fill, ls=0, anchor="la"):
    """letter-spacing 을 지원하는 텍스트. ls 는 SS 적용 전 px.

    Pillow 에 자간 옵션이 없어서 글자를 하나씩 찍는다.
    사이트가 영문 대문자에 자간을 넉넉히 주므로(§3-3) 여기서도 필요하다.
    """
    if ls == 0:
        d.text((x * SS, y * SS), s, font=fnt, fill=fill, anchor=anchor)
        return
    widths = [fnt.getlength(ch) + ls * SS for ch in s]
    total = sum(widths) - ls * SS
    cx = x * SS
    if anchor[0] == "m":
        cx -= total / 2
    elif anchor[0] == "r":
        cx -= total
    va = anchor[1]
    for ch, wch in zip(s, widths):
        d.text((cx, y * SS), ch, font=fnt, fill=fill, anchor="l" + va)
        cx += wch


# ---------------------------------------------------------------- OG 이미지
def build_og():
    """왼쪽에 로고·제목·ISBN, 오른쪽에 대표 도서 표지.

    바탕을 WASH(옅은 초록)로 두는 이유 — 순백 카드는 소셜 피드에서 빈 이미지처럼 보인다.
    """
    img, d = make_canvas(W, H, WASH)

    AX, AY, AW, AH = 76, 66, 1048, 498
    rect(d, AX, AY, AW, AH, outline=RULE, fill=ARTBOARD, width=1)

    # 오른쪽 : 대표 도서 표지. 사이트 히어로도 표지 사진이므로 인상을 맞춘다.
    cover = Image.open(COVER).convert("RGB")
    cs = int(400 * SS)
    cover = cover.resize((cs, cs), Image.LANCZOS)
    img.paste(cover, (int(698 * SS), int(115 * SS)))

    # 왼쪽 : 로고 마크 + 타이포. 마크가 곧 브랜드이므로 모노 라벨 대신 마크를 놓는다.
    x = 136
    mark = Image.open(LOGO_MARK)
    mh = int(56 * SS)
    mark = mark.resize((max(1, round(mark.width * mh / mark.height)), mh), Image.LANCZOS)
    img.paste(mark, (int(x * SS), int(104 * SS)), mark)
    line(d, x, 182, x + 96, 182, RULE, 1)

    # 사이트 h1 과 같은 문구를 쓴다. h1 을 고치면 여기도 고쳐야 한다.
    text(d, x, 202, "패션전공자를 위한", font(KR_B, 47), INK)
    text(d, x, 262, "디지털 패션 디자인", font(KR_B, 47), INK)
    # 라틴은 흘림체를 쓰지 않는다. 고딕 대문자 + 자간 (사이트 .latin 과 같은 처리)
    # 2026-07-28 : 사이트에서 .latin 을 초록→빨강으로 바꿨으므로 여기도 RED 로 맞춘다.
    # 안 맞추면 사이트는 빨강인데 카카오톡 공유 미리보기만 초록으로 남는다.
    text(d, x, 344, "DIGITAL FASHION DESIGN", font(KR_B, 16), RED, ls=3.4)

    line(d, x, 398, x + 420, 398, RULE, 1)
    text(d, x, 418, "일러스트레이터와 포토샵을 활용한", font(KR_L, 19), BODY)
    text(d, x, 448, "디지털 패션 디자인 — 도서출판 민홀릭", font(KR_L, 19), BODY)

    text(d, x, 498, "SINCE 2017", font(MONO, 12), MUTED, ls=1.8)
    text(d, x + 132, 498, "ISBN 979-11-962091-1-7", font(MONO, 12), MUTED, ls=1.8)

    img = img.resize((W, H), Image.LANCZOS)
    img.save(os.path.join(OUT, "og.png"), optimize=True)
    print("og.png", img.size)


# ---------------------------------------------------------------- 아이콘
def build_icon(size, filename, pad_ratio=0.06, art=None):
    """로고 원피스 마크를 옅은 초록 바탕에 앉힌다.

    배경을 흰색이 아니라 WASH 로 두는 이유는 흰 탭 배경에서 경계가 사라지지 않게 하려는 것.
    """
    px = size * SS
    img = Image.new("RGB", (px, px), WASH)
    mark = Image.open(art or LOGO_MARK)
    box = px - 2 * round(px * pad_ratio)
    sc = min(box / mark.width, box / mark.height)
    m = mark.resize((max(1, round(mark.width * sc)), max(1, round(mark.height * sc))), Image.LANCZOS)
    img.paste(m, ((px - m.width) // 2, (px - m.height) // 2), m)
    img = img.resize((size, size), Image.LANCZOS)
    path = os.path.join(OUT, filename)
    img.save(path, optimize=True)
    print(filename, img.size)


if ONLY in ("all", "og"):
    build_og()
if ONLY in ("all", "icons"):
    build_icon(180, "apple-touch-icon.png")
    build_icon(48, "favicon-48.png")
    build_icon(32, "favicon-32.png")
    # 16px 은 마크 안쪽 글자가 뭉개져 회색 덩어리가 된다. 실루엣만 형태가 남는다.
    build_icon(16, "favicon-16.png", pad_ratio=0.0, art=LOGO_SIL)
