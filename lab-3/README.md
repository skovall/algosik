# Лабораторная №3
**Выполнила Стецкова Алина, ИДБ-25-07**

### Каждая задача содержит:
- id
- описание
- приоритет

```python
class Task:
    def __init__(self, task_id, description, priority):
        self.id = task_id
        self.description = description
        self.priority = priority
```

### Обязательная часть
- Добавление задачи в очередь (enqueue)
- Извлечение задачи из очереди (dequeue)
- Просмотр первой задачи без извлечения (front)
- Проверка очереди на пустоту (isEmpty)

```python
class TaskQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        if not isinstance(task, Task):
            raise TypeError("Можно добавлять только объекты Task")
        
        inserted = False
        for i in range(len(self.queue)):
            if task.priority < self.queue[i].priority:
                self.queue.insert(i, task)
                inserted = True
                break
        
        if not inserted:
            self.queue.append(task)
        print(f"Задача добавлена: {task}")
  
    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста, извлечение невозможно")
            return None
        task = self.queue.pop(0)
        print(f"Задача извлечена: {task}")
        return task
          
    def front(self):
        if self.is_empty():
            print("Очередь пуста, нет первой задачи")
            return None
        print(f"Первая задача: {self.queue[0]}")
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
```

### Вариативная часть (на выбор)
Реализовать 3 функцию:

*3. Вывести все задачи в очереди*

```python
    def display_all(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        
        print(f"\nВсего задач: {len(self.queue)}")
        for i, task in enumerate(self.queue, 1):
            print(f"{i}. {task}")
```
