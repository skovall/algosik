### 1. Проверка наличия элемента в массиве
def search(arr, element): 
    for x in arr:
        if x == element:
            return True
    return False
  
### 2. Поиск второго максимального элемента
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

### 3. Бинарный поиск
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

### 4. Построение таблицы умножения
def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row += i * j
        table += row
    return table

### 5. Сортировка выбором
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


import time
def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

import random

sizes = [10, 100, 1000, 10000]
print("1. Проверка наличия элемента в массиве")
for size in sizes:
    test_arr = list(range(size))
    random.shuffle(test_arr)
    start = time.perf_counter()
    search(test_arr, -1)
    end = time.perf_counter()
    print(f"Размер {size}: {end - start:.8f} сек")

print("2. Поиск второго максимального элемента")
for size in sizes:
    test_arr = list(range(size))
    random.shuffle(test_arr)
    start = time.perf_counter()
    second_max(test_arr)
    end = time.perf_counter()
    print(f"Размер {size}: {end - start:.8f} сек")

print("3. Бинарный поиск")
for size in sizes:
    test_arr = list(range(size))
    random.shuffle(test_arr)
    start = time.perf_counter()
    bin_search(test_arr, test_arr[0])
    end = time.perf_counter()
    print(f"Размер {size}: {end - start:.8f} сек")


sizes_table = [10, 50, 100]
print("4. Построение таблицы умножения")
for size in sizes_table:
    start = time.perf_counter()
    multiplication_table(size)
    end = time.perf_counter()
    print(f"Размер {size}: {end - start:.8f} сек")

print("5. Сортировка выбором")
for size in sizes:
    test_arr = list(range(size))
    random.shuffle(test_arr)
    start = time.perf_counter()
    selection_sort(test_arr)
    end = time.perf_counter()
    print(f"Размер {size}: {end - start:.8f} сек")
