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

## Композиция: два состояния в одном кадре

Узел показывается **дважды, рядом**: слева — свободно уложенный, где виден
путь троса и каждое пересечение; справа — тот же узел затянутый, каким он
выглядит в работе.

Так сделаны образцы в `reference-samples/`, и это заметно полезнее одной
картинки: по левой половине узел вяжут, по правой узнают. Обе половины
в одном файле, одного масштаба, без разделительной линии.

## Образец геометрии

`reference-samples/lj-05-sheet-bend.jpg` — шкотовый.
Сверять по нему **топологию**, а не стиль: образцы цветные и с фоном.

## Промпт

```
Two views of the same knot side by side in one frame: on the left the knot loosely laid out so the path of the rope and every crossing is readable, on the right the same knot pulled up tight as it looks in use. Same scale, no divider.
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
