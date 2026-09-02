# Выбленочный · clove hitch

**ID файла:** `s-14-clove-hitch` · соотношение 3:4

## Назначение

Быстро крепит конец к лееру, рейке или свае. На яхте им подвязывают
кранцы. Держит, пока тяга поперёк опоры; при тяге вдоль опоры ползёт,
поэтому под серьёзной нагрузкой дополняется полуштыком.

## Последовательность вязки

1. Ходовой конец обносится вокруг опоры — первый шлаг.
2. Ходовой конец ведётся дальше и **перекрещивает** наложенный шлаг.
3. Ходовой конец обносится вокруг опоры второй раз — второй шлаг.
4. Ходовой конец пропускается **под перекрещивающий шлаг**, то есть под
   собственную диагональ.

## Что должно читаться на рисунке

- **Одна верёвка**, а не два отдельных кольца: путь троса прослеживается
  от коренной части до ходового конца непрерывно.
- Два шлага вокруг опоры, между ними видна **диагональ**.
- Ходовой конец **прижат этой диагональю** и выходит из-под неё.
- Коренная часть и ходовой конец выходят с **противоположных** сторон
  узла.

## Критерий приёмки

Прослеживается непрерывный путь одной верёвки: коренная часть → шлаг →
диагональ → второй шлаг → под диагональ → ходовой конец. Если на рисунке
два независимых кольца и отдельно лежащая верёвка — узла нет.

## Типичная ошибка генератора

Рисуются два аккуратных кольца вокруг опоры и поверх них — не связанная
с ними диагональная верёвка. Выглядит опрятно, узлом не является.

## Композиция: начало и финал

Узел показывается **дважды, рядом**: слева — последний шаг вязки, когда
остаётся одно движение; справа — готовый затянутый узел.

Так сделаны образцы в `reference-samples/`. Пара «начало → финал» учит
вязать, а не просто показывает результат дважды: по левому кадру видно,
что делать, по правому — что должно получиться. Обе половины в одном
файле, одного масштаба, без разделительной линии.

**Критерий приёмки проверяется по правому кадру.** Левый проверяется
отдельно: это должен быть последний шаг перед готовым узлом, а не
произвольная стадия.

## Образец геометрии

`reference-samples/lj-02-clove-hitch.jpg` — выбленочный.
Сверять по нему **топологию**, а не стиль: образцы цветные и с фоном.

## Промпт

```
Two frames side by side, same scale, no divider: on the left the final step of tying, one move short of complete, with every crossing readable; on the right the finished knot pulled up tight as it looks in use.
A clove hitch tied around a vertical wooden rail, seen from the front. One
single continuous rope only. The rope makes a first turn around the rail, the
running part then crosses diagonally over that first turn, makes a second turn
around the rail, and the free end is tucked underneath its own diagonal
crossing and emerges from under it. Both turns lie flat and parallel around the
rail with the diagonal crossing clearly visible between them. The standing part
leaves the knot on one side, the free tail on the opposite side. Loosely
dressed so the rope path can be traced continuously from standing part to tail.
Standing part light grey, working end darker grey, round three-strand rope.
```
