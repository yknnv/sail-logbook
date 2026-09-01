# Задание на иллюстрации: замена векторных схем

Задание на перерисовку схем из `src/figures.py` растровыми иллюстрациями.
Самодостаточно: внешних файлов открывать не нужно. Приложите к заданию
два-три принятых PNG из `assets/images` как визуальный референс.

**Прочтите раздел «Что стоит и чего не стоит заменять» до того, как
запускать генерацию.** Часть схем несёт измеримую геометрию, и картинка
вместо них ухудшит справочник, а не улучшит.

---

## 1. Стиль

Редакционная штриховая иллюстрация, как в полевом руководстве. Уверенная
чёрная линия, плоские серые заливки, минимум деталей. Не фотореализм,
не 3D-рендер, без градиентов и драматических теней.

Префикс подставляется к каждому промпту ниже:

```
Editorial line illustration for a printed pocket field manual. Clean confident
ink linework, flat grey fills, minimal detail. Pure white background. Strictly
monochrome: black ink and neutral greys only, absolutely no colour of any kind.
No gradients, no photorealism, no 3D render, no dramatic shadows. Even flat
lighting. Centred composition with generous white margin. Absolutely no text,
letters, numbers, labels, watermark or signature anywhere in the image.
```

## 2. Технические требования

- PNG, sRGB, от 2048 px по длинной стороне
- фон строго белый, не серая плашка
- никакого текста в кадре: подписи наносятся в вёрстке
- строго монохром: книга печатается одной краской
- соотношение сторон ровно указанное
- без логотипов брендов и узнаваемых реальных людей

## 3. Именование и сдача

Имя файла — ровно ID из задания. Архив со структурой
`illustrations/<ID>.png`. ID начинаются с `s-f`, чтобы не пересекаться
с уже принятой серией `s-01` … `s-31`.

---

## 4. Что стоит и чего не стоит заменять

Схемы делятся на три группы. Группа указана у каждой позиции.

**«Можно»** — сюжет и пропорции не несут измеримой информации. Картинка
заменяет схему целиком.

**«Фон»** — картинка даёт обстановку и читаемость, но числа, оси, углы
и подписи остаются вектором поверх неё. Порядок: `img()` рисует фон,
следом функция `fig_*` дорисовывает измеримый слой.

**«Не рекомендую»** — вся информация схемы и есть геометрия. Генератор
ошибётся в углах и пропорциях убедительно и незаметно: картинка будет
выглядеть аккуратной и врать. Промпт написан, решение за вами.

---

## 5. Список

### s-f01 · Курсы относительно ветра — 1:1 — фон

```
Top-down bird's eye nautical diagram. A single sailing yacht silhouette drawn
seven times, evenly spaced around the rim of a large circle, every bow pointing
outward from the centre. Sails are trimmed differently at each position: pulled
in tight along the centreline at the two upper positions, progressively eased at
the side positions, boom swung fully out across the beam at the bottom position.
A wedge sector at the top of the circle, about ninety degrees wide in total,
filled with flat light grey to mark the no-go zone. One straight arrow above the
circle points straight down into that sector. Thin circle outline, hulls in clean
ink line with light grey sail fills. Flat plan view, no perspective.
```

Приёмка: семь силуэтов по кругу, носами наружу; у нижнего гик поперёк
корпуса, у верхних паруса вдоль оси; серый сектор строго сверху.

Остаётся вектором: раскрытие мёртвого угла, окружность, все подписи.

---

### s-f02 · Человек за бортом: манёвр — 16:9 — можно

```
Top-down bird's eye nautical manoeuvre diagram. A sailing yacht silhouette
appears three times along a single continuous track. First at the upper left,
sailing away. Then bearing away into a wide rounded loop that swings below and
to the right. Finally approaching from below, bow pointing up towards a small
solid dot that marks a person in the water, a thin ring drawn around the dot.
The track is a dashed curved line connecting the three positions. Two short
straight arrows at the top left edge indicate wind blowing downward across the
scene. Flat plan view, clean ink linework, light grey hull fills, no perspective.
```

Приёмка: петля широкая и замкнутая; финальный подход снизу вверх,
носом навстречу стрелкам ветра; человек — точка с кольцом, не фигура.

---

### s-f03 · Расхождение под парусом: разные галсы — 4:3 — можно

```
Top-down bird's eye diagram of two sailing yachts approaching each other. Both
seen from directly above, hulls in clean ink outline with light grey sails. The
left yacht has its boom and sails out to the left side, the right yacht has them
out to the right side, so the two are mirror images. Two short straight arrows
above the pair point downward to indicate wind direction. Flat plan view,
generous white space, no perspective, no horizon.
```

Приёмка: паруса разведены в разные стороны — это и есть разные галсы;
обе лодки в одном масштабе.

---

### s-f04 · Расхождение под парусом: один галс — 4:3 — можно

```
Top-down bird's eye diagram of two sailing yachts on the same course, one placed
higher and to the left, the other lower and to the right. Both have booms and
sails out to the same side, so the two shapes are parallel rather than mirrored.
The upper yacht is drawn slightly larger and closer to the wind arrows. Two short
straight arrows above the pair point downward. Flat plan view, clean ink linework,
light grey sail fills, no perspective.
```

Приёмка: паруса на одной стороне у обеих лодок; наветренная выше по кадру.

---

### s-f05 · Под мотором: курс на курс — 4:3 — можно

```
Top-down bird's eye diagram of two motor vessels meeting bow to bow. Both hulls
drawn from directly above as clean pointed outlines, one in the lower left
pointing up and slightly right, the other in the upper right pointing down and
slightly left. A short straight arrow beside each hull shows it altering course
to its own starboard side, so the two tracks diverge. Flat plan view, light grey
hull fills, no perspective, no wake, no water texture.
```

Приёмка: оба корпуса отворачивают вправо; стрелки расходятся, не сходятся.

---

### s-f06 · Под мотором: пересечение — 4:3 — можно

```
Top-down bird's eye diagram of two motor vessels on crossing courses. One hull in
the lower left points up and to the right, with a straight arrow ahead of it
showing its track. A second hull enters horizontally from the right side, pointing
left, crossing ahead of the first. The two tracks meet at a right angle. Flat plan
view from directly above, clean ink outlines, light grey fills, no perspective.
```

Приёмка: пути пересекаются под прямым углом; судно справа проходит
впереди.

---

### s-f07 · Под мотором: обгон — 4:3 — можно

```
Top-down bird's eye diagram of one motor vessel overtaking another. Two hulls
seen from directly above, both pointing up the frame, one directly behind the
other. The rear hull has a long straight arrow ahead of it angling out to the
left, passing clear of the leading hull. Flat plan view, clean ink outlines,
light grey fills, no perspective, no wake.
```

Приёмка: обгоняющий сзади, его стрелка уходит в сторону от обгоняемого.

---

### s-f08 · Секторы огней — 1:1 — не рекомендую

```
Top-down bird's eye diagram of a vessel hull seen from directly above, centred
inside a large thin circle. The circle rim is drawn as three separate arcs
separated by small gaps: a wide arc covering the forward and side portion drawn
as a solid heavy line on the right side of the hull, the matching arc on the left
side drawn as a dashed heavy line, and the remaining arc behind the stern drawn
as a solid heavy line. Two faint straight lines run from the hull outward to the
points where the side arcs end behind the beam. Flat plan view, clean ink linework,
no perspective.
```

Приёмка: три дуги без нахлёста, вместе замыкающие круг; границы бортовых
дуг позади траверза, не на нём.

Остаётся вектором: 112,5° на борт, 135° за корму, 225° топовый. **Это те
самые углы, которые генератор поставит на глаз.** Если картинка не сходится
с числами, схему на странице читают неверно, а выглядит она уверенно.
Настоятельно советую оставить вектор.

---

### s-f09 · Комбинации круговых огней — 16:9 — не рекомендую

```
Six identical thin vertical masts standing in a row on a common baseline, evenly
spaced. Each mast carries small empty circles threaded on it like beads: the
first mast two circles, the second three, the third two, the fourth two, the
fifth two, the sixth one. Circles are drawn as thin outlines with a very light
grey fill, spaced evenly down the upper part of each mast. Flat elevation view,
clean ink linework, no perspective, no vessel, no background.
```

Приёмка: пустые кружки одинакового диаметра, ровно по вертикали.

Остаётся вектором: буквы К, Б, З внутри кружков. Промпт запрещает текст
в кадре, значит содержательный слой схемы всё равно рисуется кодом —
картинка даст только палки с кружками. Замена почти ничего не экономит.

---

### s-f10 · Знаки IALA: как выглядят — 16:9 — не рекомендую

```
Six navigation buoys standing in a row on a common waterline, seen in flat
elevation from the side, evenly spaced, all the same height. First: a plain
cylinder, flat topped. Second: a plain cone, pointed at the top. Third: a slim
pillar carrying two solid black triangles stacked one above the other, both
pointing up. Fourth: an identical pillar carrying two solid black triangles
base to base, the lower one pointing up and the upper one pointing down. Fifth:
an identical pillar carrying two solid black triangles both pointing down.
Sixth: an identical pillar carrying two solid black triangles apex to apex, the
lower pointing down and the upper pointing up. Clean ink outlines, light grey
buoy bodies, solid black topmarks, no perspective, no sea texture.
```

Приёмка: топовые знаки строго по описанию — вверх, основаниями, вниз,
вершинами. Любая перестановка меняет смысл знака на противоположный.

Остаётся вектором: **проверьте каждый топовый знак по отдельности.**
Генератор путает пары треугольников постоянно, а на воде эта ошибка
означает обход буя не с той стороны.

---

### s-f11 · Правило двенадцатых — 16:9 — не рекомендую

```
A simple bar chart of six vertical bars standing on a common baseline, evenly
spaced with narrow gaps. Heights follow the pattern low, medium, tall, tall,
medium, low: the third and fourth bars are the tallest and equal, the second and
fifth are noticeably shorter and equal, the first and sixth are the shortest and
equal. Bars have thin ink outlines and flat light grey fill. Nothing else in the
frame. Flat front view, no perspective, no axis lines, no ticks.
```

Приёмка: высоты относятся ровно как 1 : 2 : 3 : 3 : 2 : 1.

Остаётся вектором: **само это отношение и есть содержание схемы.**
Столбики «на глаз» превращают правило двенадцатых в декорацию. Вектор
здесь стоит трёх строк кода и не врёт.

---

### s-f12 · Якорная стоянка: длина цепи — 16:9 — можно

```
Side elevation cross-section of an anchored yacht. A horizontal line near the
top of the frame is the water surface; a second horizontal line near the bottom
is the seabed. A yacht hull sits on the surface line at the right, seen from the
side. From its bow an anchor chain runs down and away to the left, sagging into
a shallow catenary curve, flattening out and lying horizontally along the seabed
for the last part of its length, ending at a small anchor lying flat on the
bottom. The horizontal run is roughly four times the vertical depth, so the
composition is wide and shallow. Clean ink linework, flat grey water band, no
perspective, no fish, no vegetation.
```

Приёмка: последний участок цепи лежит на грунте горизонтально; общая
длина заметно больше глубины, не вдвое.

---

### s-f13 · Дневные знаки — 16:9 — не рекомендую

```
Seven identical thin vertical masts standing in a row on a common baseline,
evenly spaced. Each carries solid black geometric shapes threaded on it: the
first a single ball. The second three balls stacked vertically. The third a
single cone with its apex pointing down. The fourth two balls stacked. The fifth
a ball, a diamond and a ball stacked from top to bottom. The sixth two cones
touching apex to apex, the upper pointing up and the lower pointing down. The
seventh a single diamond. All shapes solid black, same visual weight, evenly
spaced down the upper part of each mast. Flat elevation view, clean ink linework,
no perspective, no vessel, no background.
```

Приёмка: каждая комбинация ровно по описанию, порядок фигур сверху вниз
соблюдён.

Остаётся вектором: комбинация знаков — это и есть статус судна.
`_ball`, `_diamond`, `_cone` уже написаны и дают безошибочный результат
за десяток строк.

---

### s-f14 · Звуковые сигналы — не рекомендую вообще

Схема `fig_blasts` — не иллюстрация, а нотация: чёрный прямоугольник
короткий или длинный, по одному на гудок. Восемь строк на странице
различаются только числом и длиной прямоугольников. Промпт для неё
писать нечего: генератор не воспроизведёт восемь наборов прямоугольников
с точной кратностью длин, а именно кратность и есть содержание.

Оставьте вектором.

---

## 6. Чего избегать

Ошибки, которые повторялись:

- имена файлов не совпадали с содержимым
- в кадр попадали английские или русские подписи
- фон приходил цветным или серым вместо белого
- несколько файлов дублировали один сюжет, которого не было в задании
- разрешение около 250 dpi вместо запрошенного

## 7. Приёмка партии

1. Прогнать через `tools/prepare_illustrations.py` — он обрежет поля
   и переведёт в серое.
2. Вставить блоком `("img", ("имя", высота_мм, "подпись"))`.
3. `./build.sh` и просмотр изменённых страниц глазами.
4. Для позиций «фон» — проверить, что векторный слой лёг поверх картинки
   и не разъехался с ней.
