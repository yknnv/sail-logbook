# Шкотовый · sheet bend

**ID файла:** `s-12-sheet-bend` · соотношение 16:9

## Назначение

Соединяет два конца **разной толщины** — там, где прямой узел ползёт.
Держит под натяжением; на ослабленном тросе может распуститься.

## Состояние

Иллюстрации для этого узла в книге нет: прежняя оказалась негодной, и
страница сейчас объясняет узел словами. Это первый кандидат на замену.

## Последовательность вязки

1. **Толстый** трос складывается петлёй — открытым концом от себя.
2. **Тонкий** трос заводится в петлю **снизу вверх**.
3. Тонкий обносит **обе пряди петли сзади** — сначала одну, потом другую.
4. Тонкий подворачивается **под собственную коренную часть**, ту, что
   вышла из петли.

## Что должно читаться на рисунке

- Толстый трос образует петлю, тонкий её обвивает — толщины **разные
  и заметно**.
- **Ходовые концы обоих тросов выходят с одной стороны узла.**
- Тонкий конец прижат собственной коренной частью.

## Критерий приёмки

Ходовые концы толстого и тонкого — **с одной стороны**. Если с разных,
нарисован левый шкотовый: он развязывается под нагрузкой. Это
единственное отличие, и оно решающее.

## Типичная ошибка генератора

Тросы рисуются одинаковой толщины — тогда узел теряет смысл, ради
которого существует. Разница диаметров должна быть примерно вдвое.

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

`reference-samples/lj-05-sheet-bend.jpg` — шкотовый.
Сверять по нему **топологию**, а не стиль: образцы цветные и с фоном.

## Промпт

```
Two frames side by side, same scale, no divider: on the left the final step of tying, one move short of complete, with every crossing readable; on the right the finished knot pulled up tight as it looks in use.
A sheet bend joining two ropes of clearly different thickness, loosely dressed
and lying flat, seen from directly above. The thick rope is bent back on itself
to form an open bight. The thin rope comes up through that bight from below,
passes behind both legs of the bight, and is then tucked under its own standing
part where it emerged from the bight. Critically: the free tail of the thick
rope and the free tail of the thin rope both emerge on the same side of the
knot. The thick rope is about twice the diameter of the thin one. Thick rope in
light grey, thin rope in darker grey, round three-strand rope, every crossing
clearly readable.
```
