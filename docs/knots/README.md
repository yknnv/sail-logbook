# Узлы: задание на перерисовку

Шесть узлов со страницы «Узлы». Нынешние иллюстрации к печати не годятся:
проверка показала, что часть из них изображает не тот узел, а часть —
вообще не связный трос.

## Что здесь

| файл | узел |
|---|---|
| `01-bowline.md` | беседочный · bowline |
| `02-figure-eight.md` | восьмёрка · figure-eight stopper |
| `03-square-knot.md` | прямой · reef knot |
| `04-clove-hitch.md` | выбленочный · clove hitch |
| `05-round-turn.md` | штык со шлагом · round turn and two half hitches |
| `06-sheet-bend.md` | шкотовый · sheet bend |

В каждом файле: назначение, **точная последовательность вязки с указанием,
какая прядь идёт поверх какой**, промпт на английском, критерий приёмки
и типичная ошибка, по которой неверный узел узнаётся с одного взгляда.

## Чего здесь намеренно нет

**Готовых схем-картинок.** У узла всё содержание в том, какая прядь
проходит поверх какой. Схема, нарисованная приблизительно, выглядит
уверенно и врёт — а в печатном справочнике это хуже отсутствующей
картинки. Поэтому здесь текстовая спецификация, по которой рисунок можно
проверить однозначно, и ссылки на источники, где геометрию можно сверить
глазами.

## Как проверять присланное

Не «похоже на узел», а по критерию приёмки из файла. Каждый критерий
сформулирован так, чтобы неверный вариант отсекался за секунды: считается
число пересечений, проверяется сторона выхода ходового конца, взаимное
положение шлагов.

**Самая надёжная проверка — завязать по картинке.** Если по рисунку узел
не вяжется или получается другой, рисунок не годится, как бы хорошо он
ни выглядел.

## Общий стиль

Тот же, что у принятой серии `s-01` … `s-31`. Префикс к каждому промпту:

```
Editorial line illustration for a printed pocket field manual. Clean confident
ink linework, flat grey fills, minimal detail. Pure white background. Strictly
monochrome: black ink and neutral greys only, absolutely no colour of any kind.
No gradients, no photorealism, no 3D render, no dramatic shadows. Even flat
lighting. Absolutely no text, letters, numbers, labels, watermark or signature
anywhere in the image.
```

Дополнительно для узлов:

```
Loosely dressed knot, not pulled tight: every strand and every crossing clearly
separated and readable. Round rope with visible three-strand lay. Two tones:
the standing part in light grey, the working end in darker grey, so the path of
the rope can be followed. Every crossing unambiguous — the strand passing over
is drawn continuous, the strand passing under is interrupted by it. Single knot
centred in the frame, plain white background, no hands, no background objects.
```

Требования к файлу: PNG, от 2048 px по длинной стороне, монохром, белый
фон, без текста в кадре.

## Источники для сверки

- Л. Н. Скрягин, «Морские узлы» — справочник, по которому выверена
  русская терминология
- Морской справочник, раздел «Морские узлы»:
  https://flot.com/publications/books/shelf/maritimehandbook/26.htm
- Словарь морских узлов:
  https://dic.academic.ru/dic.nsf/sea_knots/
- Ru-Sailing, «Морские узлы»:
  https://ru-sailing.ru/poleznaya-informaciya/morskie-uzly/
