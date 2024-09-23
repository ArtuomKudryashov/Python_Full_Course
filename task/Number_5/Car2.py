class Car2:
    def __init__(self, make, max_speed):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0

    def __str__(self):
        result = f"Car make: {self.make}, Max speed: {self.max_speed} km/h, Current speed: {self.speed} km/h-rerwe"

        for attr, value in self.__dict__.items():
            if attr not in ["make", "max_speed", "speed"]:
                result += f", {attr.capitalize()}: {value}"
        return result





