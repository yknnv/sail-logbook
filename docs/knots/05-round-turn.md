# Штык со шлагом · round turn and two half hitches

**ID файла:** `s-15-round-turn` · соотношение 1:1

## Назначение

Швартовка к рыму, кольцу или свае. Держит рывок и развязывается после
нагрузки. Полный оборот принимает на себя рывок, а полуштыки только
запирают узел.

## Терминология

Английское название полное — **round turn and two half hitches**.
Сокращать до «round turn» нельзя: round turn — это просто оборот,
не узел. В книге исправлено.

## Последовательность вязки

1. Ходовой конец обносится вокруг опоры **дважды** — полный оборот
   плюс ещё один шлаг. Это и есть «шлаг», который отличает узел
   от простого штыка.
2. Ходовым концом делается полуштык вокруг **коренной части**.
3. Делается второй полуштык вокруг коренной части — **в ту же сторону**,
   что и первый.

## Что должно читаться на рисунке

- Вокруг опоры **два витка**, а не один.
- Оба полуштыка — вокруг коренной части, **рядом друг с другом**.
- Полуштыки **однонаправленные**: они выглядят как два одинаковых витка,
  идущих в одну сторону.

## Критерий приёмки

Считаются витки на опоре: **два**. Полуштыки закручены **в одну сторону**.
Если в разные — получилась коровья затяжка, узел ползёт по коренной части.

## Типичная ошибка генератора

Рисуются два независимых узла в разных местах кольца, соединённые
верёвками разного цвета. Путь одной верёвки не прослеживается.

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

`reference-samples/lj-04-two-half-hitches.jpg` — штык со шлагом.
Сверять по нему **топологию**, а не стиль: образцы цветные и с фоном.

## Промпт

```
Two frames side by side, same scale, no divider: on the left the final step of tying, one move short of complete, with every crossing readable; on the right the finished knot pulled up tight as it looks in use.
A round turn and two half hitches tied to a heavy metal mooring ring. One
single continuous rope. The rope passes through the ring twice, making two
complete parallel turns around the metal, with both turns clearly visible and
separated. The working end then makes two half hitches around its own standing
part, one after the other, both wound in the same direction so they look like
two identical coils lying side by side. The standing part runs out of the frame
under tension. Loosely dressed so the rope path is traceable from the ring to
the free tail. Standing part light grey, working end darker grey, round
three-strand rope, plain metal ring.
```
