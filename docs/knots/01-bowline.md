# Беседочный · bowline

**ID файла:** `s-10-bowline` · соотношение 3:4

## Назначение

Незатягивающаяся петля фиксированного размера. Держит под нагрузкой,
развязывается после неё. Основной узел на яхте.

## Последовательность вязки

1. На коренной части делается небольшая **колышка** — петля, в которой
   коренная часть проходит **под** собой.
2. Ходовой конец подаётся в колышку **снизу вверх**.
3. Ходовой конец обносится **вокруг коренной части** сзади — образуется
   «воротник».
4. Ходовой конец возвращается в колышку **сверху вниз**, рядом с той
   прядью, по которой вошёл.

Большая петля образуется между колышкой и воротником.

## Что должно читаться на рисунке

- **Ходовой конец выходит внутри большой петли**, а не снаружи.
- Воротник вокруг коренной части виден отдельной дугой.
- В колышке ходовой конец идёт двумя параллельными прядями — вошёл
  и вышел.
- Длина ходового конца — примерно четыре диаметра троса.

## Критерий приёмки

Ходовой конец **внутри** петли. Если он выходит наружу — нарисован
неправильный булинь: он развяжется под переменной нагрузкой.

## Типичная ошибка генератора

Рисуется просто петля с накинутым сверху витком, без воротника вокруг
коренной части. Проверять именно воротник: без него узла нет.

## Композиция: два состояния в одном кадре

Узел показывается **дважды, рядом**: слева — свободно уложенный, где виден
путь троса и каждое пересечение; справа — тот же узел затянутый, каким он
выглядит в работе.

Так сделаны образцы в `reference-samples/`, и это заметно полезнее одной
картинки: по левой половине узел вяжут, по правой узнают. Обе половины
в одном файле, одного масштаба, без разделительной линии.

## Образец геометрии

`reference-samples/lj-01-bowline.jpg` — беседочный.
Сверять по нему **топологию**, а не стиль: образцы цветные и с фоном.

## Промпт

```
Two views of the same knot side by side in one frame: on the left the knot loosely laid out so the path of the rope and every crossing is readable, on the right the same knot pulled up tight as it looks in use. Same scale, no divider.
A bowline knot tied in a single rope, loosely dressed so every crossing is
readable. A small fixed loop hangs open at the bottom of the frame. The
standing part runs up to the top of the frame. In the standing part there is a
small round bight; the working end comes up through that bight from below,
passes behind the standing part forming a visible collar around it, and comes
back down through the same bight, lying alongside the strand it entered by. The
free tail ends inside the large loop, about four rope diameters long. Standing
part in light grey, working end in darker grey. Round three-strand rope. Every
crossing unambiguous: the strand in front continuous, the strand behind
interrupted.
```
