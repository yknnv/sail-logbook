#!/usr/bin/env python3
"""SAIL logbook — судовой журнал яхтсмена.
A5, перфорация под кольцевой переплёт, одна краска (чёрная).
Подписи полей дублируются на русском и английском."""

import os

from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
from reportlab.lib.colors import CMYKColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RLTTFont

from reference import build_reference

# ------------------------------------------------------------------ шрифты
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_D = os.path.join(_ROOT, "assets", "fonts") + os.sep
if not os.path.exists(_D + "Carlito-Regular.ttf"):
    _D = "/usr/share/fonts/truetype/crosextra/"     # запасной вариант: системный шрифт
pdfmetrics.registerFont(RLTTFont("Body", _D + "Carlito-Regular.ttf"))
pdfmetrics.registerFont(RLTTFont("BodyB", _D + "Carlito-Bold.ttf"))
pdfmetrics.registerFont(RLTTFont("Lbl", _D + "Carlito-Regular.ttf"))
pdfmetrics.registerFont(RLTTFont("LblB", _D + "Carlito-Bold.ttf"))
BODY, BOLD = "Body", "BodyB"        # проза
LBL, LBLB = "Lbl", "LblB"           # подписи полей и заголовки

# Carlito мельче DejaVu при том же кегле — компенсируем единым множителем.
# Он применяется и при отрисовке, и при замерах ширины, иначе подгонка
# подписей под колонку начнёт врать.
FONT_SCALE = 1.13


def scale_canvas(c):
    raw = c.stringWidth
    c.stringWidth = lambda s, f, sz, *a, **k: raw(s, f, sz * FONT_SCALE, *a, **k)
    return c

# ------------------------------------------------------------------ палитра
# весь набор в одной краске K — печать в одну краску, чёткий текст
INK    = CMYKColor(0, 0, 0, 1)
ACCENT = CMYKColor(0, 0, 0, 1)      # заголовки и линейки — чёрные
LABEL  = CMYKColor(0, 0, 0, 1)      # русская подпись — плотно чёрная
LABEL2 = CMYKColor(0, 0, 0, 0.55)   # английский дубль
RULE   = CMYKColor(0, 0, 0, 0.34)
GRID   = CMYKColor(0, 0, 0, 0.15)
FAINT  = CMYKColor(0, 0, 0, 0.07)
PUNCH  = CMYKColor(0, 0, 0, 0.22)



# ------------------------------------------------------------------ картинки
IMG_DIR = os.path.join(_ROOT, "assets", "images")


def img(c, name, x, y, w, h, align="c"):
    """Иллюстрация в бокс (x, y — левый верх, w×h). Пропорции сохраняются,
    картинка вписывается и центрируется. Возвращает израсходованную высоту."""
    path = os.path.join(IMG_DIR, name if name.endswith(".png") else name + ".png")
    if not os.path.exists(path):
        return 0.0
    ir = ImageReader(path)
    iw, ih = ir.getSize()
    k = min(w / iw, h / ih)
    dw, dh = iw * k, ih * k
    dx = x + (w - dw) / 2 if align == "c" else x
    c.drawImage(ir, dx, y - dh, dw, dh, mask="auto")
    return dh

# ------------------------------------------------------------------ геометрия
TRIM_W, TRIM_H = 148 * mm, 210 * mm

MT, MB = 10 * mm, 10 * mm
M_BIND = 23 * mm          # поле со стороны колец
M_OUT  = 10 * mm

HOLE_D = 6 * mm
HOLE_INSET = 11 * mm
HOLE_SPACING = 47 * mm
HOLE_MARKS = True

N_PASSAGES = 42
N_NOTES = 10

VERSION = "1.0"        # ставится в имя файла и в свойства PDF
AUTHOR = "Yury Kononov"
HOMEPAGE = "https://github.com/yknnv/sail-logbook"
KEEP_CREATED_WITH_AI = True   # строка на титуле; выключается без правки композиции


def hole_centers():
    n = 4
    span = HOLE_SPACING * (n - 1)
    top = TRIM_H / 2 + span / 2
    return [top - i * HOLE_SPACING for i in range(n)]


# ------------------------------------------------------------------ примитивы
def margins(page_no):
    if page_no % 2 == 1:
        return M_BIND, M_OUT
    return M_OUT, M_BIND


def txt(c, x, y, s, font, size, color, space=0.0, align="l"):
    w = c.stringWidth(s, font, size) + space * len(s)
    if align == "c":
        x -= w / 2
    elif align == "r":
        x -= w
    t = c.beginText(x, y)
    t.setFont(font, size * FONT_SCALE)
    t.setCharSpace(space)
    t.setFillColor(color)
    t.textOut(s)
    c.drawText(t)
    return w


def caps(c, x, y, text, size=5.6, color=LABEL, space=0.7, font=LBLB):
    return txt(c, x, y, text.upper(), font, size, color, space)


def bilabel(c, x, y, ru, en, size=5.4, maxw=None):
    """Русская подпись жирным, английская — светлее.
    Если пара не влезает даже в минимальном кегле, английский дубль опускается."""
    ru, en = ru.upper(), en.upper()
    en_s = "/ " + en

    def pair_w(s):
        return (c.stringWidth(ru, LBLB, s) + 0.4 * len(ru) + 1.3 * mm
                + c.stringWidth(en_s, LBL, s * 0.83) + 0.3 * len(en_s))

    while size > 3.9 and maxw is not None and pair_w(size) > maxw:
        size -= 0.1

    if maxw is not None and pair_w(size) > maxw:
        s = size
        while s > 3.6 and c.stringWidth(ru, LBLB, s) + 0.4 * len(ru) > maxw:
            s -= 0.1
        txt(c, x, y, ru, LBLB, s, LABEL, 0.4)
        return

    w1 = txt(c, x, y, ru, LBLB, size, LABEL, 0.4)
    txt(c, x + w1 + 1.3 * mm, y, en_s, LBL, size * 0.83, LABEL2, 0.3)


def field(c, x, y, w, ru, en, h=9 * mm, size=5.4):
    bilabel(c, x, y + h - 3.7 * mm, ru, en, size, maxw=w)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.4)
    c.line(x, y, x + w, y)


def cols(x, w, n, gap=4 * mm):
    cw = (w - gap * (n - 1)) / n
    return [(x + i * (cw + gap), cw) for i in range(n)]


def checkrow(c, x, y, w, items, ncols=4, size=5.2):
    """Чекбоксы по фиксированной сетке колонок."""
    box = 2.6 * mm
    cw = w / ncols
    for i, (ru, en) in enumerate(items):
        cx = x + i * cw
        ru_u, en_u = ru.upper(), " / " + en.upper()
        s = size
        while s > 4.2:
            need = (box + 1.2 * mm
                    + c.stringWidth(ru_u, LBLB, s) + 0.2 * len(ru_u)
                    + c.stringWidth(en_u, LBL, s * 0.85) + 0.2 * len(en_u))
            if need <= cw - 2 * mm:
                break
            s -= 0.1
        c.setStrokeColor(RULE)
        c.setLineWidth(0.4)
        c.rect(cx, y, box, box, stroke=1, fill=0)
        tw = txt(c, cx + box + 1.2 * mm, y + 0.6 * mm, ru_u, LBLB, s, LABEL, 0.2)
        txt(c, cx + box + 1.2 * mm + tw, y + 0.6 * mm, en_u, LBL, s * 0.85, LABEL2, 0.2)


def block_head(c, x, y, w, ru, en):
    caps(c, x, y, ru, 5.8, ACCENT, 0.9)
    txt(c, x + w, y, en, LBL, 5.0, LABEL2, 0.6, "r")
    return 5.6 * mm


def punch(c, page_no):
    if not HOLE_MARKS:
        return
    cx = HOLE_INSET if page_no % 2 else TRIM_W - HOLE_INSET
    c.setStrokeColor(PUNCH)
    c.setLineWidth(0.3)
    for cy in hole_centers():
        c.setDash(0.8, 1.2)
        c.circle(cx, cy, HOLE_D / 2, stroke=1, fill=0)
        c.setDash()
        c.line(cx - 1.4 * mm, cy, cx + 1.4 * mm, cy)
        c.line(cx, cy - 1.4 * mm, cx, cy + 1.4 * mm)


def folio(c, page_no):
    """Номера страниц не печатаются: листы съёмные."""
    return


# ------------------------------------------------------------------ страницы
def cover(c):
    cx = TRIM_W / 2 + (M_BIND - M_OUT) / 2
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.8)
    c.rect(M_BIND - 5 * mm, 12 * mm,
           TRIM_W - M_BIND - M_OUT + 10 * mm, TRIM_H - 24 * mm, stroke=1, fill=0)

    # горизонт и волна
    img(c, "s-01-under-sail", cx - 40 * mm, 118 * mm, 80 * mm, 46 * mm)

    ty = TRIM_H - 66 * mm
    w1 = c.stringWidth("SAIL", LBLB, 30) + 3.0 * 4
    w2 = c.stringWidth("logbook", LBL, 30) + 1.2 * 7
    tx = cx - (w1 + 3.5 * mm + w2) / 2
    txt(c, tx, ty, "SAIL", LBLB, 30, ACCENT, 3.0)
    txt(c, tx + w1 + 3.5 * mm, ty, "logbook", LBL, 30, LABEL, 1.2)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.2)
    c.line(cx - 16 * mm, ty - 10 * mm, cx + 16 * mm, ty - 10 * mm)
    txt(c, cx, ty - 18 * mm, "ЛИЧНЫЙ ЖУРНАЛ ЯХТСМЕНА · PERSONAL SAILING LOGBOOK",
        LBL, 6.2, LABEL2, 1.2, "c")

    txt(c, cx, 24 * mm, "Author: Yury Kononov", LBL, 7.2, LABEL, 0.8, "c")
    txt(c, cx, 19.5 * mm, "ykononov.com", LBL, 6.6, LABEL2, 0.8, "c")
    if KEEP_CREATED_WITH_AI:
        txt(c, cx, 15 * mm, "Created with AI", LBL, 6.2, LABEL2, 0.8, "c")

    x = M_BIND
    w = TRIM_W - M_BIND - M_OUT
    field(c, x, 46 * mm, w, "владелец", "name")
    a, b = cols(x, w, 2)
    field(c, a[0], 32 * mm, a[1], "квалификация", "certificate")
    field(c, b[0], 32 * mm, b[1], "том №", "book no.")
    punch(c, 1)


def personal(c):
    ml, mr = margins(2)
    x, w = ml, TRIM_W - ml - mr
    y = TRIM_H - MT

    caps(c, x, y - 5 * mm, "данные яхтсмена", 8.4, ACCENT, 1.8)
    txt(c, x + w, y - 5 * mm, "SAILOR DETAILS", LBL, 6.4, LABEL2, 1.2, "r")
    y -= 9 * mm
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.8)
    c.line(x, y, x + w, y)
    y -= 11 * mm

    rows = [
        [("фамилия, имя", "full name", 1.0)],
        [("дата рождения", "date of birth", 0.5), ("группа крови", "blood type", 0.5)],
        [("город, страна", "city, country", 0.62), ("индекс", "postcode", 0.38)],
        [("телефон", "phone", 0.5), ("e-mail", "e-mail", 0.5)],
    ]
    for row in rows:
        cx, gap = x, 4 * mm
        avail = w - gap * (len(row) - 1)
        for ru, en, frac in row:
            cw = avail * frac
            field(c, cx, y, cw, ru, en, h=11 * mm)
            cx += cw + gap
        y -= 11 * mm

    def block(y, title, en, pairs):
        caps(c, x, y, title, 6.6, ACCENT, 1.3)
        txt(c, x + w, y, en, LBL, 5.8, LABEL2, 1.0, "r")
        y -= 14 * mm
        for l, r in pairs:
            a, b = cols(x, w, 2)
            field(c, a[0], y, a[1], l[0], l[1], h=11 * mm)
            field(c, b[0], y, b[1], r[0], r[1], h=11 * mm)
            y -= 11 * mm
        return y

    y -= 3 * mm
    y = block(y, "экстренный контакт", "EMERGENCY CONTACT",
              [(("кто", "name"), ("кем приходится", "relationship")),
               (("телефон", "phone"), ("e-mail", "e-mail"))])
    y -= 1 * mm
    y = block(y, "страховка", "INSURANCE",
              [(("компания", "provider"), ("номер полиса", "policy no.")),
               (("действует до", "valid until"), ("линия 24 ч", "24 h line"))])
    y -= 1 * mm
    caps(c, x, y, "медицина", 6.6, ACCENT, 1.3)
    txt(c, x + w, y, "MEDICAL", LBL, 5.8, LABEL2, 1.0, "r")
    y -= 14 * mm
    field(c, x, y, w, "ограничения, хронические состояния", "restrictions", h=11 * mm)
    y -= 11 * mm
    field(c, x, y, w, "аллергии, препараты", "allergies, medication", h=11 * mm)

    assert y >= MB, "стр. 2 переполнена: %.1f мм" % (y / mm)
    punch(c, 2)
    folio(c, 2)


def table_page(c, page_no, title, title_en, headers, widths, n_rows, row_h=9 * mm):
    ml, mr = margins(page_no)
    x, w = ml, TRIM_W - ml - mr
    y = TRIM_H - MT

    caps(c, x, y - 5 * mm, title, 8.4, ACCENT, 1.8)
    txt(c, x + w, y - 5 * mm, title_en, LBL, 6.4, LABEL2, 1.2, "r")
    y -= 9 * mm
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.8)
    c.line(x, y, x + w, y)
    y -= 6 * mm

    total = sum(widths)
    abs_w = [w * v / total for v in widths]

    cx = x
    for (ru, en), cw in zip(headers, abs_w):
        bilabel(c, cx + 1.5 * mm, y - 3.2 * mm, ru, en, 5.0, maxw=cw - 3 * mm)
        cx += cw
    y -= 5 * mm

    top = y
    for r in range(n_rows + 1):
        yy = top - r * row_h
        c.setStrokeColor(ACCENT if r == 0 else RULE)
        c.setLineWidth(0.6 if r == 0 else 0.4)
        c.line(x, yy, x + w, yy)
    bottom = top - n_rows * row_h

    cx = x
    c.setStrokeColor(GRID)
    c.setLineWidth(0.35)
    for cw in abs_w[:-1]:
        cx += cw
        c.line(cx, top, cx, bottom)

    punch(c, page_no)
    folio(c, page_no)


def passage_page_a(c, page_no):
    """Левая страница разворота: судно, маршрут, время, схема."""
    ml, mr = margins(page_no)
    x, w = ml, TRIM_W - ml - mr
    y = TRIM_H - MT
    cs = cols(x, w, 3, 4 * mm)

    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.0)
    c.line(x, y, x + w, y)
    y -= 9.5 * mm
    hw = 34 * mm
    bilabel(c, x, y + 5.9 * mm, "переход №", "passage no.", 5.6, maxw=hw)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.7)
    c.line(x, y, x + hw, y)
    field(c, x + hw + 4 * mm, y, w - hw - 4 * mm, "дата", "date", h=9.5 * mm)

    y -= 6 * mm
    y -= block_head(c, x, y, w, "судно и экипаж", "VESSEL & CREW")
    for row in [[("яхта", "vessel"), ("тип, вооружение", "type, rig"), ("длина, м", "loa")],
                [("шкипер", "skipper"), ("роль на борту", "capacity"), ("экипаж, чел", "crew")]]:
        y -= 9.5 * mm
        for (cx, cw), (ru, en) in zip(cs, row):
            field(c, cx, y, cw, ru, en, h=9.5 * mm, size=5.2)

    y -= 6 * mm
    y -= block_head(c, x, y, w, "маршрут", "ROUTE")
    a, b = cols(x, w, 2, 4 * mm)
    for l, r in [(("порт отхода", "from"), ("порт прихода", "to")),
                 (("расчётный отход", "etd"), ("фактический отход", "atd")),
                 (("расчётный приход", "eta"), ("фактический приход", "ata")),
                 (("пройдено по лагу, миль", "log"), ("пройдено по gps, миль", "over ground"))]:
        y -= 9.5 * mm
        field(c, a[0], y, a[1], l[0], l[1], h=9.5 * mm, size=5.2)
        field(c, b[0], y, b[1], r[0], r[1], h=9.5 * mm, size=5.2)

    y -= 6 * mm
    y -= block_head(c, x, y, w, "время", "TIME")
    for row in [[("всего, ч", "total"), ("дневных, ч", "day"), ("ночных, ч", "night")],
                [("под парусом, ч", "sailing"), ("под мотором, ч", "engine"), ("шкипером, ч", "as skipper")],
                [("на вахте, ч", "watchkeeping"), ("", ""), ("", "")]]:
        y -= 9.5 * mm
        for (cx, cw), (ru, en) in zip(cs, row):
            if ru:
                field(c, cx, y, cw, ru, en, h=9.5 * mm, size=5.2)

    assert y >= MB, "карточка A переполнена: %.1f мм" % (y / mm)
    punch(c, page_no)


def passage_page_b(c, page_no):
    """Правая страница разворота: погода, навигация, операции, стоянка."""
    ml, mr = margins(page_no)
    x, w = ml, TRIM_W - ml - mr
    y = TRIM_H - MT
    cs = cols(x, w, 3, 4 * mm)

    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.0)
    c.line(x, y, x + w, y)
    y -= 5.5 * mm

    y -= block_head(c, x, y, w, "погода", "WEATHER")
    for row in [[("направление ветра", "wind dir"), ("сила, баллы / узлы", "force"), ("порывы, узлы", "gust")],
                [("волнение", "sea state"), ("зыбь, м / с", "swell"), ("видимость", "visibility")]]:
        y -= 9.0 * mm
        for (cx, cw), (ru, en) in zip(cs, row):
            field(c, cx, y, cw, ru, en, h=9.0 * mm, size=5.2)
    y -= 9.0 * mm
    field(c, cs[0][0], y, cs[0][1], "давление, гПа", "pressure", h=9.0 * mm, size=5.2)
    caps(c, cs[1][0], y + 1.4 * mm, "тенденция", 5.0, LABEL, 0.5)
    checkrow(c, cs[1][0] + 20 * mm, y + 0.6 * mm, w - (cs[1][0] - x) - 20 * mm,
             [("растёт", "rising"), ("ровно", "steady"), ("падает", "falling")], ncols=3)

    y -= 6 * mm
    y -= block_head(c, x, y, w, "навигация", "NAVIGATION")
    for row in [[("курс", "course"), ("средняя, уз", "avg speed"), ("максимум, уз", "max speed")]]:
        y -= 9.0 * mm
        for (cx, cw), (ru, en) in zip(cs, row):
            field(c, cx, y, cw, ru, en, h=9.0 * mm, size=5.2)
    for group in [[("приливные воды", "tidal"), ("лоцманская", "pilotage"),
                   ("открытое море", "offshore"), ("ночь", "night")],
                  [("туман", "fog"), ("срд", "tss"), ("", ""), ("", "")]]:
        y -= 5.6 * mm
        checkrow(c, x, y, w, [g for g in group if g[0]])

    y -= 6 * mm
    y -= block_head(c, x, y, w, "операции", "OPERATIONS")
    for group in [[("швартовка", "mooring"), ("якорь", "anchoring"), ("бочка", "buoy"), ("шлюз", "lock")],
                  [("рифление", "reefing"), ("спинакер", "spinnaker"), ("лавировка", "beating"), ("фордевинд", "running")],
                  [("моб учебный", "mob drill"), ("укв", "vhf"), ("", ""), ("", "")]]:
        y -= 5.6 * mm
        checkrow(c, x, y, w, [g for g in group if g[0]])

    y -= 6 * mm
    y -= block_head(c, x, y, w, "двигатель и стоянка", "ENGINE & BERTH")
    for row in [[("моточасы, начало", "hours start"), ("моточасы, конец", "hours end"), ("топливо, л", "fuel used")],
                [("марина, стоянка", "berth"), ("место №", "berth no."), ("глубина, м", "depth")]]:
        y -= 9.0 * mm
        for (cx, cw), (ru, en) in zip(cs, row):
            field(c, cx, y, cw, ru, en, h=9.0 * mm, size=5.2)

    y -= 6 * mm
    y -= block_head(c, x, y, w, "заметки", "NOTES")
    c.setStrokeColor(RULE)
    c.setLineWidth(0.4)
    for _ in range(3):
        y -= 6.4 * mm
        c.line(x, y, x + w, y)

    y -= 4 * mm
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.7)
    c.line(x, y, x + w, y)
    stamp_w = 33 * mm
    left_w = w - stamp_w - 5 * mm
    a, b = cols(x, left_w, 2, 4 * mm)
    top = y
    y -= 9.4 * mm
    field(c, a[0], y, a[1], "шкипер", "skipper", h=9.4 * mm, size=5.2)
    field(c, b[0], y, b[1], "№ квалификации", "cert. no.", h=9.4 * mm, size=5.2)
    y -= 9.4 * mm
    field(c, a[0], y, a[1], "подпись", "signature", h=9.4 * mm, size=5.2)
    field(c, b[0], y, b[1], "всего миль", "total miles", h=9.4 * mm, size=5.2)
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.setDash(1.6, 1.6)
    c.rect(x + w - stamp_w, y, stamp_w, top - y - 2 * mm, stroke=1, fill=0)
    c.setDash()
    scy = y + (top - y - 2 * mm) / 2
    txt(c, x + w - stamp_w / 2, scy + 1.2 * mm, "ПЕЧАТЬ ШКОЛЫ", LBL, 5.0, LABEL, 0.5, "c")
    txt(c, x + w - stamp_w / 2, scy - 3 * mm, "ИЛИ МАРИНЫ", LBL, 5.0, LABEL, 0.5, "c")

    assert y >= MB, "карточка B переполнена: %.1f мм" % (y / mm)
    punch(c, page_no)


def summary_page(c, page_no):
    ml, mr = margins(page_no)
    x, w = ml, TRIM_W - ml - mr
    y = TRIM_H - MT

    caps(c, x, y - 5 * mm, "итоги", 8.4, ACCENT, 1.8)
    txt(c, x + w, y - 5 * mm, "LOGBOOK SUMMARY", LBL, 6.4, LABEL2, 1.2, "r")
    y -= 9 * mm
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.8)
    c.line(x, y, x + w, y)
    y -= 14 * mm

    pairs = [
        (("всего миль", "total miles"), ("из них ночных", "night miles")),
        (("часов под парусом", "sailing hours"), ("часов под мотором", "engine hours")),
        (("переходов", "passages"), ("суток в море", "days at sea")),
        (("самый длинный переход", "longest"), ("максимальный ветер", "max wind")),
        (("миль шкипером", "as skipper"), ("портов и стран", "ports")),
    ]
    for l, r in pairs:
        a, b = cols(x, w, 2)
        field(c, a[0], y, a[1], l[0], l[1], h=14 * mm)
        field(c, b[0], y, b[1], r[0], r[1], h=14 * mm)
        y -= 14 * mm

    y -= 4 * mm
    caps(c, x, y, "заметки", 6.6, ACCENT, 1.3)
    txt(c, x + w, y, "NOTES", LBL, 5.8, LABEL2, 1.0, "r")
    y -= 8 * mm
    c.setStrokeColor(RULE)
    c.setLineWidth(0.4)
    while y > MB + 4 * mm:
        c.line(x, y, x + w, y)
        y -= 8 * mm

    punch(c, page_no)
    folio(c, page_no)



def summary_page2(c, page_no):
    """Вторая страница итогов: опыт и сводка по годам."""
    ml, mr = margins(page_no)
    x, w = ml, TRIM_W - ml - mr
    y = TRIM_H - MT
    caps(c, x, y - 5 * mm, "опыт", 8.4, ACCENT, 1.8)
    txt(c, x + w, y - 5 * mm, "EXPERIENCE TOTALS", LBL, 6.4, LABEL2, 1.2, "r")
    y -= 9 * mm
    c.setStrokeColor(ACCENT); c.setLineWidth(0.8)
    c.line(x, y, x + w, y)
    y -= 12 * mm
    pairs = [(("миль шкипером", "skipper miles"), ("приливных миль", "tidal miles")),
             (("миль в открытом море", "offshore miles"), ("ночных миль", "night miles")),
             (("часов на вахте", "watchkeeping"), ("часов шкипером", "as skipper")),
             (("суток в море", "days at sea"), ("переходов", "passages")),
             (("портов", "ports"), ("шлюзов", "locks")),
             (("учений моб", "mob drills"), ("стран", "countries"))]
    for l, r in pairs:
        a, b = cols(x, w, 2)
        field(c, a[0], y, a[1], l[0], l[1], h=12 * mm)
        field(c, b[0], y, b[1], r[0], r[1], h=12 * mm)
        y -= 12 * mm

    y -= 6 * mm
    caps(c, x, y, "по годам", 6.6, ACCENT, 1.3)
    txt(c, x + w, y, "BY YEAR", LBL, 5.8, LABEL2, 1.0, "r")
    y -= 8 * mm
    heads = [("год", "year"), ("миль", "miles"), ("шкипером", "skipper"),
             ("ночных", "night"), ("суток", "days"), ("переходов", "passages")]
    widths = [0.7, 0.8, 0.9, 0.8, 0.7, 0.9]
    total = sum(widths)
    cw = [w * v / total for v in widths]
    cx = x
    for (ru, en), ww in zip(heads, cw):
        bilabel(c, cx + 1.5 * mm, y - 3.2 * mm, ru, en, 5.0, maxw=ww - 3 * mm)
        cx += ww
    top = y - 5 * mm
    c.setStrokeColor(ACCENT); c.setLineWidth(0.6)
    c.line(x, top, x + w, top)
    rows = int((top - MB - 2 * mm) / (9 * mm))
    for r in range(rows):
        c.setStrokeColor(RULE); c.setLineWidth(0.35)
        c.line(x, top - (r + 1) * 9 * mm, x + w, top - (r + 1) * 9 * mm)
    cx = x
    c.setStrokeColor(GRID); c.setLineWidth(0.3)
    for ww in cw[:-1]:
        cx += ww
        c.line(cx, top, cx, top - rows * 9 * mm)
    punch(c, page_no)


def notes_page(c, page_no):
    ml, mr = margins(page_no)
    x, w = ml, TRIM_W - ml - mr
    caps(c, x, TRIM_H - MT - 5 * mm, "заметки", 8.4, ACCENT, 1.8)
    txt(c, x + w, TRIM_H - MT - 5 * mm, "NOTES", LBL, 6.4, LABEL2, 1.2, "r")
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.8)
    c.line(x, TRIM_H - MT - 9 * mm, x + w, TRIM_H - MT - 9 * mm)
    y = TRIM_H - MT - 21 * mm
    c.setStrokeColor(RULE)
    c.setLineWidth(0.4)
    while y > MB + 4 * mm:
        c.line(x, y, x + w, y)
        y -= 8 * mm
    punch(c, page_no)
    folio(c, page_no)


def crop_marks(c, bleed):
    L, off = 4 * mm, 1.5 * mm
    c.setStrokeColor(INK)
    c.setLineWidth(0.25)
    for cx, cy, sx, sy in [(bleed, bleed, -1, -1),
                           (bleed + TRIM_W, bleed, 1, -1),
                           (bleed, bleed + TRIM_H, -1, 1),
                           (bleed + TRIM_W, bleed + TRIM_H, 1, 1)]:
        c.line(cx + sx * off, cy, cx + sx * (off + L), cy)
        c.line(cx, cy + sy * off, cx, cy + sy * (off + L))


# ------------------------------------------------------------------ сборка
def build(path, bleed=0.0, marks=False):
    pw, ph = TRIM_W + 2 * bleed, TRIM_H + 2 * bleed
    c = scale_canvas(canvas.Canvas(path, pagesize=(pw, ph)))
    c.setTitle("SAIL logbook — личный журнал яхтсмена · Personal Sailing Logbook")
    c.setAuthor(AUTHOR)
    c.setSubject("Журнал яхтсмена A5 для печати: записи о переходах и справочник. "
                 "Версия %s · %s" % (VERSION, HOMEPAGE))
    # свойства PDF индексируются поисковиками — перечисляем то, по чему журнал ищут
    c.setKeywords("журнал яхтсмена, судовой журнал, яхтенный логбук, sailing logbook, "
                  "yacht logbook, printable logbook A5, парусный спорт, МППСС, COLREGS, "
                  "MAYDAY, узлы, приливы, версия %s" % VERSION)
    c.setCreator("sail-logbook %s · %s" % (VERSION, HOMEPAGE))

    def start():
        c.saveState()
        c.translate(bleed, bleed)

    def end():
        c.restoreState()
        if marks:
            crop_marks(c, bleed)
        c.showPage()

    ctx = dict(c=c, TRIM_W=TRIM_W, TRIM_H=TRIM_H, MT=MT, MB=MB,
               INK=INK, ACCENT=ACCENT, LABEL=LABEL, LABEL2=LABEL2,
               RULE=RULE, GRID=GRID, FAINT=FAINT,
               BODY=BODY, BOLD=BOLD, LBL=LBL, LBLB=LBLB,
               margins=margins, caps=caps, txt=txt, field=field, img=img,
               bilabel=bilabel, cols=cols, folio=folio, punch=punch,
               checkrow=checkrow)
    ref_pages = build_reference(ctx)

    start(); cover(c);    end()
    start(); personal(c); end()

    for i, draw in enumerate(ref_pages):
        start(); draw(3 + i); end()

    p = 3 + len(ref_pages)
    start()
    table_page(c, p, "квалификации", "CERTIFICATES",
               [("школа, агентство", "school"), ("квалификация", "level"),
                ("№", "cert. no."), ("дата", "date"), ("инструктор", "instructor")],
               [1.3, 1.25, 1.0, 0.8, 1.25], 18)
    end()

    p += 1
    start()
    table_page(c, p, "яхты", "VESSELS",
               [("название", "name"), ("тип, длина", "type, loa"),
                ("порт приписки", "home port"), ("период", "period")],
               [1.15, 1.4, 1.2, 0.95], 18)
    end()

    if (p + 1) % 2:
        p += 1
        start(); notes_page(c, p); end()
    for i in range(N_PASSAGES):
        start(); passage_page_a(c, p + 1 + 2 * i); end()
        start(); passage_page_b(c, p + 2 + 2 * i); end()

    p = p + 2 * N_PASSAGES + 1
    start(); summary_page(c, p); end()
    p += 1
    start(); summary_page2(c, p); end()
    for _ in range(N_NOTES):
        p += 1
        start(); notes_page(c, p); end()
    if p % 2:                      # добор до чётного: печать двусторонняя
        p += 1
        start(); notes_page(c, p); end()

    c.save()
    return p


def punch_template(path):
    c = canvas.Canvas(path, pagesize=(TRIM_W, TRIM_H))
    c.setTitle("Шаблон перфорации A5 — SAIL logbook")
    c.setAuthor(AUTHOR)
    c.setSubject("Печатать в масштабе 100 %, без «вписать в страницу» · " + HOMEPAGE)
    c.setCreator("sail-logbook %s · %s" % (VERSION, HOMEPAGE))
    x, w = M_BIND, TRIM_W - M_BIND - M_OUT

    caps(c, x, TRIM_H - MT - 5 * mm, "шаблон перфорации", 8.4, ACCENT, 1.8)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.8)
    c.line(x, TRIM_H - MT - 9 * mm, x + w, TRIM_H - MT - 9 * mm)

    lines = [
        "Распечатайте этот лист в масштабе 100 % (без «вписать",
        "в страницу») и приложите к обложке. Центры отверстий",
        "должны совпасть с кольцами.",
        "",
        "Числа у отверстий — расстояние от нижнего края листа",
        "до центра отверстия.",
        "",
        "Текущие параметры:",
        "     лист  148 × 210 мм (A5)",
        "     отверстий  4,  диаметр %.0f мм" % (HOLE_D / mm),
        "     шаг между центрами  %.0f мм" % (HOLE_SPACING / mm),
        "     от края до центра  %.0f мм" % (HOLE_INSET / mm),
        "     поле под кольца  %.0f мм" % (M_BIND / mm),
        "",
        "Не совпало — измерьте обложку и поправьте HOLE_SPACING,",
        "HOLE_INSET и M_BIND в начале saillog.py, затем",
        "пересоберите файл.",
    ]
    y = TRIM_H - MT - 22 * mm
    for ln in lines:
        txt(c, x, y, ln, BODY, 8, INK)
        y -= 4.7 * mm

    c.setStrokeColor(ACCENT)
    c.setLineWidth(0.6)
    for cy in hole_centers():
        c.circle(HOLE_INSET, cy, HOLE_D / 2, stroke=1, fill=0)
        c.line(HOLE_INSET - 4 * mm, cy, HOLE_INSET + 4 * mm, cy)
        c.line(HOLE_INSET, cy - 4 * mm, HOLE_INSET, cy + 4 * mm)
        txt(c, HOLE_INSET, cy - HOLE_D / 2 - 3.4 * mm,
            "%.0f мм" % (cy / mm), BODY, 5.6, LABEL2, 0, "c")

    c.setStrokeColor(RULE)
    c.setLineWidth(0.4)
    c.setDash(2, 2)
    c.line(M_BIND, MB, M_BIND, TRIM_H - MT)
    c.setDash()
    txt(c, M_BIND + 1.5 * mm, MB + 2 * mm, "граница набора", BODY, 5.6, LABEL2)
    c.save()


if __name__ == "__main__":
    n = build(os.path.join(_ROOT, "dist", "sail-logbook-A5-final.pdf"))
    build(os.path.join(_ROOT, "dist", "sail-logbook-A5-final-bleed3mm-cropmarks.pdf"), bleed=3 * mm, marks=True)
    punch_template(os.path.join(_ROOT, "dist", "punch-template-A5.pdf"))
    print("страниц:", n, "| переходов:", N_PASSAGES)
