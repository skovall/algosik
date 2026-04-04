import base64
import json

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
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["coordinates"], data["time_to_next"])
    
    def to_base64(self):
        json_str = json.dumps(self.to_dict())
        return base64.b64encode(json_str.encode()).decode()
    
    @classmethod
    def from_base64(cls, base64_str):
        json_str = base64.b64decode(base64_str).decode()
        data = json.loads(json_str)
        return cls.from_dict(data)
