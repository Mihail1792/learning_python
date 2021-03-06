### **Какая пора года??**

Ваша задача — реализовать функцию `get_season(date)`, которая принимает объект `Date` и возвращает соответствующую ему пору года. Пора года должна быть типа `string`.

---
<details>

<summary>Названия пор года в англиийском языке</summary>
В английском поры года имеют следующие наименования: весна — spring, лето — summer, осень — autumn (fall), зима — winter.

</details>

---

Если аргумент `date` не был передан, функция должна выбросить исключение `'Unable to determine the time of year!'` Если аргумент `date` **некорректный**, функция должна выбросить исключение (`Error`).

Напишите свой код в `.{your_name}/what_season.py`.

---

### **Ханойская башня**

![Визуализация алгоритма](https://ioecapsule.com/wp-content/uploads/2019/08/tower_of_hanoi_3_disks.gif)

[Ханойская башня](https://www.britannica.com/topic/Tower-of-Hanoi) — знаменитая математическая головоломка 18 столетия.
Она состоит из трех стержней и некоторого числа дисков разных размеров, которые могут быть надеты на стержень. Головоломка начинается с того, что диски расположены друг на друге, причем наименьший расположен сверху. Диски образуют конус.

Цель головоломки — переместить всю стопку на другой стержень, следуя этим простым **правилам**:
* перемещать можно только **один** диск за раз
* можно брать только **верхний** диск с одной из стопок и помещать на **верхушку** другой стопки или на пустой стержень
* диск **большего** размера нельзя класть на диск **меньшего** размера

Ваша задача значительно легче, чем придумывать алгоритм, решающий эту задачу :)

Реализуйте функцию `calculate_hanoi`, которая принимает параметры `disk_number` и `turns_speed`. `disk_number` — это число **дисков**, а `turns_speed` — скорость перемещения дисков (в **ходах** в **час**). Оба параметра являются числами (тип `int`)

Функция `calculate_hanoi` возвращает объект с 2 свойствами:
* `turns` (минимальное число (тип `int`) ходов, необходимое для решения головоломки)
* `seconds` (минимальное число (тип `int`) **секунд**, необходимое для решения головоломки при заданной скорости; должно быть целым числом, полученным в результате округления результата расчетов в меньшую сторону)

Вам не нужно валидировать входные параметры.

Например:

`calculate_hanoi(9, 4308) => { turns: 511, seconds: 427 }`

Напишите свой код в `.{your_name}/hanoi_calc.py`.

---

### **Преобразование массива**

Ваша задача — реализовать функцию `transform(arr)`, которая принимает массив (тип `list`) и возвращает **преобразованный** массив, основываясь на **управляющих последовательностях**, которые содержит `arr`. **Управляющие последовательности** — это определенные строковые элементы вышеупомянутого массива:
* `--discard-next` исключает следующий за ней элемент исходного массива из преобразованного массива.
* `--discard-prev` исключает предшествующий ей элемент исходного массива из преобразованного массива.
* `--double-next` удваивает следующий за ней элемент исходного массива в преобразованном массиве.
* `--double-prev` удваивает предшествующий ей элемент исходного массива в преобразованном массиве.

Например:

`transform([1, 2, 3, '--double-next', 4, 5])` => `[1, 2, 3, 4, 4, 5]`

`transform([1, 2, 3, '--discard-prev', 4, 5])` => `[1, 2, 4, 5]`

Функция не должна изменять исходный список. Управляющие последовательности применяются **последовательно, слева направо** к элементам из исходного списка. Управляющие последовательности **не попадают** в преобразованный массив. Управляющие последовательности в исходном массиве не встречаются подряд (не следуют одна за другой). Если около управляющей последовательности **нет элемента**, к которому она может быть применена в исходном списке, либо он был удален в процессе преобразования списка, **она не делает ничего**. Функция должна выбросить ошибку, если `arr` не является списком.

Напишите свой код в `.{your_name}/transform_list.py`.

---
### **Рекурсивный вычислитель глубины**
![Идти глубже](https://i.imgur.com/k7lADiM.jpg)

Ваша задача — реализовать класс `DepthCalculator` с методом `calculate_depth`, который принимает массив и возвращает его **глубину**.

Метод `calculate_depth` должен проходить полученный массив **рекурсивно**. Глубина **плоского** массива — 1. Метод должен корректно работать с массивами, не содержащими элементов или содержащими пустые массивы, метод должен быть свойством класса.

Например:
 
 `some_arr = [[[]]]`
 
`depth_calc = DepthCalculator(arr: list = some_arr);`

`depth_calc.calculate_depth([[[]]])` => `3`


Напишите ваш код в `./{your_name}/recursive_depth.py`.