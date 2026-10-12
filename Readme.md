# Лабораторная работа № 2 «Сумма двух»

## 1. Цель работы
Реализовать функцию `add(nums, target)`, которая принимает:
- `nums` — массив целых чисел;
- `target` — целое число.

Функция должна вернуть индексы двух элементов массива `nums`, сумма которых равна `target`.  
Если решения нет — вернуть пустой список `[]`. Один и тот же элемент нельзя использовать дважды.

## 2. Реализация

### `main.py`
```python
def add(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []

print(add([3, 3], 6))
```

### `test_main.py`
```python
import unittest
from main import add

class TestAdd(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(sorted(add([2, 7, 11, 15], 9)), [0, 1])

    def test_example_2(self):
        self.assertEqual(sorted(add([3, 2, 4], 6)), [1, 2])

    def test_example_3(self):
        self.assertEqual(sorted(add([3, 3], 6)), [0, 1])

    def test_no_solution(self):
        self.assertEqual(add([1, 2, 3], 100), [])

    def test_negative(self):
        self.assertEqual(sorted(add([-3, 4, 3, 90], 0)), [0, 2])

    def test_zeros(self):
        self.assertEqual(sorted(add([0, 4, 3, 0], 0)), [0, 3])

    def test_at_the_end(self):
        self.assertEqual(sorted(add([1, 2, 100, 5], 105)), [2, 3])


if __name__ == '__main__':
    unittest.main()
```

## 3. Алгоритм работы
Используется хеш-таблица `seen`, где:
- ключ — значение элемента массива;
- значение — его индекс.

Для каждого элемента `num` вычисляется дополнение:
```python
need = target - num
```

Если `need` уже есть в `seen`, значит ранее был элемент, который вместе с текущим даёт `target`.  
Возвращаются индексы `[seen[need], i]`.

Если после прохода решения не найдено, возвращается `[]`.

## 4. Результаты тестирования

| Тест | Входные данные | Ожидаемый результат | Результат |
|---|---|---|---|
| Тест 1 | `nums = [2,7,11,15], target = 9` | `[0,1]` | ✅ PASS |
| Тест 2 | `nums = [3,2,4], target = 6` | `[1,2]` | ✅ PASS |
| Тест 3 | `nums = [3,3], target = 6` | `[0,1]` | ✅ PASS |
| Нет решения | `nums = [1,2,3], target = 100` | `[]` | ✅ PASS |
| Отрицательные числа | `nums = [-3,4,3,90], target = 0` | `[0,2]` | ✅ PASS |
| Нули | `nums = [0,4,3,0], target = 0` | `[0,3]` | ✅ PASS |
| В конце массива | `nums = [1,2,100,5], target = 105` | `[2,3]` | ✅ PASS |

## 5. Запуск тестов
```bash
python -m unittest test_main.py
```

Ожидаемый результат:
```text
......
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK
```

## 6. Вывод
Функция `add` корректно решает задачу поиска двух индексов, сумма элементов которых равна `target`.  
Все предоставленные тесты проходят успешно. Алгоритм эффективен и имеет сложность `O(n)`.