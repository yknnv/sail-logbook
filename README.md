# SAIL logbook — журнал яхтсмена A5 для печати

[![build](https://github.com/yknnv/sail-logbook/actions/workflows/build.yml/badge.svg)](https://github.com/yknnv/sail-logbook/actions/workflows/build.yml)
[![release](https://img.shields.io/github/v/release/yknnv/sail-logbook?label=релиз)](https://github.com/yknnv/sail-logbook/releases/latest)
[![код: MIT](https://img.shields.io/badge/код-MIT-black)](LICENSE)
[![содержимое: CC BY-NC-SA 4.0](https://img.shields.io/badge/содержимое-CC%20BY--NC--SA%204.0-black)](LICENSE-CONTENT)

**[Скачать готовый PDF](https://github.com/yknnv/sail-logbook/releases/latest)** ·
**[Витрина проекта](https://yknnv.github.io/sail-logbook/)** ·
[English](#english)

Личный журнал яхтсмена формата A5 — печатный журнал, справочник и памятка в одном.
Вёрстка описана кодом, а не лежит в бинарном макете: книга собирается
одной командой и правится текстом.

- **144 страниц**, из них 42 разворота под записи
- A5 148 × 210 мм, перфорация под кольцевой переплёт
- печать в одну краску, чёрным
- подписи полей на русском и английском
- справочный раздел: безопасность на борту, брифинг, курсы относительно ветра, человек за бортом, радиосвязь и MAYDAY, экстренные контакты, снаряжение безопасности, леер и страховка, узлы, скорость и расстояние, МППСС, огни и знаки, звуковые сигналы, дневные знаки, стоянка и швартовка, кранцы, приёмка чартера, чек-листы, план перехода, план захода, двигатель, погода, Бофорт, навигация и приливы, буи IALA

Парный проект для другой дисциплины — `dive-logbook`.

---

## Скачать

Готовые PDF лежат в [релизах](https://github.com/yknnv/sail-logbook/releases/latest) —
собирать ничего не нужно. В репозиторий они не коммитятся: каждая пересборка
добавляла бы к истории 32 МБ.

## Собрать самому

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
./build.sh
```

Результат в `dist/` (папка в `.gitignore`):

| файл | зачем |
|---|---|
| `sail-logbook-A5-final.pdf` | основной, лист ровно 148 × 210 мм |
| `sail-logbook-A5-final-bleed3mm-cropmarks.pdf` | 154 × 216 мм с припуском 3 мм и метками реза, если типография режет пачкой |
| `punch-template-A5.pdf` | один лист 1:1 для проверки перфорации |

**Начните с шаблона перфорации.** Распечатайте его в масштабе 100 %,
без «вписать в страницу», и приложите к своей обложке: расположение
колец различается. Параметры правятся в начале `src/logbook.py`.

---

## Структура

```
src/logbook.py        геометрия, примитивы, обложка, карточки записей, сборка
src/reference.py      справочный раздел, одна функция на страницу
src/figures.py        векторные схемы
src/check_margins.py  проверка полей и наложений
assets/fonts/         Carlito, SIL OFL 1.1
assets/images/        иллюстрации, монохромные PNG
dist/                 результат сборки, не коммитится
site/                 витрина для GitHub Pages
CLAUDE.md             инструкции для ИИ-агента при доработке
CONTRIBUTING.md       правила правок и чек-лист перед pull request
docs/                 шаблон задания на иллюстрации
tools/                подготовка новых иллюстраций
```

---

## Настройки без правки вёрстки

В начале `src/logbook.py`:

```python
VERSION = "1.0"               # попадает в имя файла и свойства PDF
N_PASSAGES = 42                # число разворотов под записи
N_NOTES = 10                  # страниц заметок в конце
KEEP_CREATED_WITH_AI = True   # строка на титуле
HOLE_D = 6 * mm               # диаметр отверстия
HOLE_INSET = 11 * mm          # от края листа до центра отверстия
HOLE_SPACING = 47 * mm        # между центрами соседних отверстий
HOLE_MARKS = True             # печатать метки под пробойник
M_BIND = 23 * mm              # поле со стороны колец
```

---

## Доработка через ИИ

В корне лежит `CLAUDE.md` — инструкции для агента: инварианты вёрстки,
карта файлов, шаблоны добавления страниц и схем, формат постановки
правки и список типовых граблей. Claude Code читает его автоматически
при открытии проекта; другим инструментам его можно просто передать
в контекст.

## Правила вёрстки

Их стоит держать при любой доработке.

**Отступы задаются константами.** В `src/reference.py` объявлены
`GAP_TEXT`, `GAP_LIST`, `GAP_TABLE`, `GAP_FIG`, `GAP_NOTE`. Один тип
элемента — один отступ. Не помещается — режется содержимое, а не
интервал: именно подгонка интервалов под конкретную страницу и разводит
книгу вразнос.

**Переполнение ловит сборка.** Каждая страница заканчивается
`assert y >= MB`. Если не влезло, сборка падает и называет страницу и
недостающие миллиметры. Правильная реакция: сократить текст, уменьшить
картинку или разделить страницу надвое.

**Подписи двуязычные.** `field(c, x, y, w, "русский", "english")` рисует
русское название плотно чёрным, английское светлее и мельче, с
автоподбором кегля под ширину колонки.

**Монохром.** Вся палитра — оттенки чёрного.

**Номеров страниц нет** намеренно: листы съёмные, порядок задаёт владелец.

---

## Проверка перед печатью

```bash
python3 src/check_margins.py dist/sail-logbook-A5-final.pdf
```

Три проверки: выход за границы набора с допуском 0,15 мм, горизонтальные
наложения символов, вертикальные наложения слов. Метки перфорации в поле
переплёта учитываются отдельно и нарушением не считаются.

---

## Печать

- бумага 100–120 г/м², офсет
- поле со стороны колец 23 мм, внешнее 10 мм, чередуются по чётности
- печать двусторонняя, число страниц чётное
- карточка записи занимает разворот и всегда начинается с чётной страницы

---

## Как помочь

Нашли ошибку в фактах или съехавшую вёрстку — заведите issue: для того
и другого есть шаблон. Правила правок, инварианты вёрстки и чек-лист
перед pull request — в [CONTRIBUTING.md](CONTRIBUTING.md).

Историю выпусков ведёт [CHANGELOG.md](CHANGELOG.md).

---

## Лицензии и оговорки

| что | лицензия |
|---|---|
| код: `src/`, `tools/`, `build.sh` | [MIT](LICENSE) |
| содержимое: тексты, иллюстрации, вёрстка, собранные PDF | [CC BY-NC-SA 4.0](LICENSE-CONTENT) |
| шрифт Carlito | [SIL OFL 1.1](assets/fonts/Carlito-COPYRIGHT.txt) |

Печатайте для себя, экипажа или школы; печать на продажу условиями
CC BY-NC-SA не разрешена. Carlito метрически совместим с Calibri,
кириллица полная.

Иллюстрации сгенерированы ИИ и обработаны вручную. Схемы в `figures.py`
нарисованы кодом.

**Справочный раздел не заменяет обучение.** Числовые ориентиры зависят
от подготовки, снаряжения, местных правил и плана; там, где это
существенно, в тексте есть оговорка.

---

## English

**SAIL logbook** is a printable A5 sailing logbook: 42 passage spreads plus
a reference section, generated from Python source rather than kept in a
binary layout file.

- 144 pages, 148 × 210 mm, punched for a ring binder
- single-ink (black) printing, monochrome throughout
- every field label is doubled in English
- reference: safety on board, crew briefing, points of sail, man overboard,
  VHF and MAYDAY, safety gear, jackstay and tether, knots, COLREGS, lights
  and shapes, sound signals, mooring, charter handover, passage plan, engine,
  weather and Beaufort, navigation, tides, IALA buoyage

Headings and reference prose are in Russian; field labels are bilingual.

**[Download the PDF](https://github.com/yknnv/sail-logbook/releases/latest)** —
three files per release: the trimmed A5 sheet, a version with 3 mm bleed and
crop marks, and a 1:1 punch template. Print the punch template first at 100 %
scale and hold it against your binder — ring spacing varies.

To build it yourself: `pip install -r requirements.txt && ./build.sh`. The
build renders the PDFs and runs layout checks; an overfull page fails the
build and names the page and the missing millimetres.

Code is MIT, content is CC BY-NC-SA 4.0. The reference section does not
replace training. More at **[yknnv.github.io/sail-logbook](https://yknnv.github.io/sail-logbook/en/)**.
