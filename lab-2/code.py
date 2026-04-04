class Bus_Stop:
    def __init__(self, name, coordinates, time_to_next):
        self.name = name
        self.coordinates = coordinates
        self.time = time_to_next

    def show_info(self):
        return f"Остановка {self.name}\nКоординаты: {self.coordinates}\nВремя до следующей: {self.time}"

    def to_dict(self):
            return {
                "name": self.name,
                "coordinates": self.coordinates,
                "time_to_next": self.time_to_next
            }
