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
