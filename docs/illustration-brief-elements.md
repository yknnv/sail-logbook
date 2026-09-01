# Задание на элементы схем

Не иллюстрации на страницу, а **детали конструктора**: отдельные лодки
и суда, из которых вёрстка сама собирает схемы. Углы, расстановку,
подписи и сетку рисует код — от вас нужны только сами объекты.

Отсюда главное требование, которого нет в обычных заданиях.

---

## 1. Каноническая ориентация — жёсткое требование

**Каждый элемент рисуется носом строго вверх, вид точно сверху,
без перспективы и без наклона.** Повороты делает вёрстка.

Если лодка приедет нарисованной «под углом», весь смысл пропадает:
код не сможет поставить её на 45° точно, потому что не знает, сколько
градусов уже заложено в картинку. Схема снова станет приблизительной —
ровно то, ради чего затевалась замена.

Проверка на приёмке простая: если провести вертикаль через кадр, она
должна пройти по диаметральной плоскости корпуса от носа к корме.

---

## 2. Стиль

Тот же, что у принятой серии `s-01` … `s-31`. Префикс к каждому промпту:

```
Editorial line illustration for a printed pocket field manual. Clean confident
ink linework, flat grey fills, minimal detail. Pure white background. Strictly
monochrome: black ink and neutral greys only, absolutely no colour of any kind.
No gradients, no photorealism, no 3D render, no dramatic shadows. Even flat
lighting. Absolutely no text, letters, numbers, labels, watermark or signature
anywhere in the image.
```

Дополнительно для элементов:

```
Single isolated object centred in the frame, nothing else in the picture. Plain
white background with no ground plane, no shadow, no horizon, no water texture,
no border. Flat orthographic top-down view, no perspective, no tilt.
```

---

## 3. Технические требования

- PNG, от **1200 px по длинной стороне**: на странице элемент занимает
  около 11 мм, но ставится под поворотом — запас на пересчёт нужен
- фон строго белый и сплошной, без подложки и виньетки
- объект не касается краёв кадра, поле вокруг 5–10 % ширины
- строго монохром, никакого текста
- **одинаковая толщина обводки во всех шести файлах** — см. раздел 6

Прозрачность делать не нужно: белый фон выбивается автоматически
командой `python3 tools/prepare_illustrations.py --elements`.

---

## 4. Список

Шесть элементов закрывают восемь схем в книге.

### e-boat-close-hauled · яхта, паруса втянуты — 2:3

```
Top-down orthographic view of a sailing yacht, bow pointing straight up. Hull
drawn as a clean symmetrical ink outline with a hint of deck detail: cockpit
opening near the stern, a slim cabin top forward of it. Mainsail and headsail
both hauled in tight, lying almost along the centreline of the hull, overlapping
the deck, filled flat light grey. Boom barely off centre.
```

Приёмка: паруса почти вдоль оси корпуса; корпус симметричен относительно
вертикали.

---

### e-boat-beam-reach · яхта, паруса приспущены — 2:3

```
Top-down orthographic view of a sailing yacht, bow pointing straight up.
Identical hull to the other yacht elements. Mainsail and headsail eased out to
the right side of the hull at roughly forty-five degrees from the centreline,
filled flat light grey, boom clearly swung out to starboard.
```

Приёмка: паруса вынесены на правый борт примерно на 45°; корпус тот же,
что у остальных элементов.

---

### e-boat-broad-reach · яхта, паруса отпущены — 2:3

```
Top-down orthographic view of a sailing yacht, bow pointing straight up.
Identical hull to the other yacht elements. Mainsail and headsail eased far out
to the right side, roughly seventy degrees from the centreline, well clear of
the deck, filled flat light grey.
```

Приёмка: паруса вынесены заметно дальше, чем на галфвинде, но ещё не
поперёк.

---

### e-boat-running · яхта, бабочка — 1:1

```
Top-down orthographic view of a sailing yacht, bow pointing straight up.
Identical hull to the other yacht elements. Mainsail swung fully out to the left
side and headsail fully out to the right side, both roughly square across the
hull, forming a symmetrical butterfly. Sails filled flat light grey.
```

Приёмка: паруса разведены на оба борта симметрично; композиция шире,
чем высокая.

---

### e-vessel-power · моторное судно — 2:3

```
Top-down orthographic view of a motor vessel, bow pointing straight up. Plain
pointed bow, straight parallel sides, flat transom stern. A simple wheelhouse
block set slightly forward of amidships. No masts, no sails, no rigging. Hull
outline in clean ink line with flat light grey fill.
```

Приёмка: силуэт однозначно моторный, не парусный; корма прямая.

---

### e-yacht-side · яхта сбоку — 16:9

```
Side elevation of a small cruising yacht seen from directly abeam, bow pointing
to the right, floating on an implied waterline with the keel visible below it.
Mast and boom drawn as thin lines, no sails set. Clean ink outline, flat light
grey hull fill, no perspective, no water, no background, no shadow.
```

Приёмка: строго боковой вид, нос вправо; киль читается.

Этот элемент — единственный не сверху. Он для схемы якорной стоянки,
где вид сбоку задан самой схемой.

---

## 5. Именование и сдача

Имя файла — ровно ID из задания, префикс `e-`. Архив
`elements/<ID>.png`. Не склеивать в общий лист: каждый элемент
отдельным файлом.

---

## 6. Главный риск партии

**Толщина обводки гуляет между отрисовками.** Каждый файл — отдельный
запуск генератора, и линия приходит то тоньше, то жирнее. На странице
эти лодки стоят рядом по кругу, и разнобой виден сразу — набор
перестаёт читаться как одна серия.

Поэтому: сгенерируйте по три-четыре кандидата на элемент, выложите их
рядом в одном масштабе и отберите **согласованный комплект**, а не
лучший файл по отдельности. Это единственное место, где партия
разваливается, и починить его после вставки в вёрстку нельзя.

Второе по частоте — разная ширина корпуса. Все четыре яхты должны быть
одним и тем же судном в разной обтяжке парусов, а не четырьмя разными
лодками.

---

## 7. Как элементы попадают в книгу

```bash
python3 tools/prepare_illustrations.py --elements elements/ mapping.txt
./build.sh
```

`--elements` обрезает поля и выбивает белый фон в прозрачность заливкой
от края кадра — белое внутри корпуса остаётся белым, и линия круга не
просвечивает сквозь палубу.

Дальше ничего делать не нужно: `fig_points_of_sail` уже ищет эти файлы
по именам. Пока их нет, схема рисуется вектором, как сейчас, — сборка
не ломается на полпути.

Проверить после вставки: `./build.sh`, затем глазами страницу «Курсы
относительно ветра». Смотреть на стык элемента с серым сектором —
если по контуру лодки видна белая кайма, порог выбивания фона нужно
поднять.
