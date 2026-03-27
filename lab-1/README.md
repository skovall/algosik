# Лабораторная №1
**Выполнила Стецкова Алина, ИДБ-25-07**

### 1. Проверка наличия элемента в массиве
Алгоритмическая сложность: O(n)
```python
def search(arr, element): 
    for x in arr:
        if x == element:
            return True
    return False
```
| n | Время (сек) |
|---|---|
| 10 | 0.00000360 |
| 100 | 0.00000620 |
| 1000 | 0.00003580 |
| 10000 | 0.00026820 |

### 2. Поиск второго максимального элемента
Алгоритмическая сложность: O(n)
```python
def second_max(arr):
    if len(arr) < 2:
        return False
    max1 = max2 = arr[0]
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2 = x
    return max2
```
| n | Время (сек) |
|---|---|
| 10 | 0.00000570 |
| 100 | 0.00000800 |
| 1000 | 0.00006750 |
| 10000 | 0.00060640 |

### 3. Бинарный поиск
Алгоритмическая сложность: O(log n)
```python
def bin_search(arr, element):
    sorted_arr = sorted(arr)
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if element > sorted_arr[mid]:
            left = mid + 1
        elif element < sorted_arr[mid]:
            right = mid - 1
        else:
            return True
    return False
```
| n | Время (сек) |
|---|---|
| 10 | 0.00000890 |
| 100 | 0.00001340 |
| 1000 | 0.00020030 |
| 10000 | 0.00146710 |

### 4. Построение таблицы умножения
Алгоритмическая сложность: O(n²)
```python
def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row += i * j
        table += row
    return table
```
| n | Время (сек) |
|---|---|
| 10 | 0.00002850 |
| 50 | 0.00024720 |
| 100 | 0.00157560 |

### 5. Сортировка выбором
Алгоритмическая сложность: O(n²)

Пространственная сложность: O(n)
```python
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    return arr
```
| n | Время (сек) |
|---|---|
| 10 | 0.00002400 |
| 100 | 0.00025750 |
| 1000 | 0.03413470 |
| 10000 | 2.94866770 |
