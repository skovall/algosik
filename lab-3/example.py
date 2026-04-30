class Task:
    def __init__(self, task_id, description, priority):
        self.id = task_id
        self.description = description
        self.priority = priority
    
    def __str__(self):
        return f"ID: {self.id} | Приоритет: {self.priority} | Описание: {self.description}"


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
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display_all(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        
        print(f"\nВсего задач: {self.size()}")
        for i, task in enumerate(self.queue, 1):
            print(f"{i}. {task}")
def main():
    task_queue = TaskQueue()
    
    task1 = Task(1, "Написать отчет", 3)
    task2 = Task(2, "Проверить код", 1)
    task3 = Task(3, "Ответить на письма", 2)
    task4 = Task(4, "Провести встречу", 1)
    task5 = Task(5, "Обновить документацию", 4)
    
    print("=== Добавление задач ===")
    task_queue.enqueue(task1)
    task_queue.enqueue(task2)
    task_queue.enqueue(task3)
    task_queue.enqueue(task4)
    task_queue.enqueue(task5)
    
    print("\n=== Вывод всех задач ===")
    task_queue.display_all()
    
    print("\n=== Проверка isEmpty ===")
    print(f"Очередь пуста: {task_queue.is_empty()}")
    print(f"Размер очереди: {task_queue.size()}")
    
    print("\n=== Просмотр первой задачи (front) ===")
    first = task_queue.front()
    if first:
        print(f"Первая задача: {first}")
    
    print("\n=== Извлечение задач (dequeue) ===")
    while not task_queue.is_empty():
        task = task_queue.dequeue()
        print(f"Извлечено: {task}")
    
    print("\n=== Проверка после извлечения ===")
    print(f"Очередь пуста: {task_queue.is_empty()}")
    task_queue.display_all()
    
    print("\n=== Попытка извлечь из пустой очереди ===")
    result = task_queue.dequeue()
    if result is None:
        print("Очередь пуста, извлечение невозможно")
    
    print("\n=== Проверка front на пустой очереди ===")
    result = task_queue.front()
    if result is None:
        print("Очередь пуста, нет первой задачи")

if __name__ == "__main__":
    main()
