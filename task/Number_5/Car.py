class Car:
    def __init__(self, make, max_speed):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0

    def __str__(self):
        return f"Car make:{self.make}, Max speed:{self.max_speed} km/h, Curent speed: {self.speed}km/h"

    def display_speed(self):
        print(self.speed)

    def accelerate(self):
        if self.speed + 10 > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += 10

    def brake(self):
        if self.speed - 10 < 0:
            self.speed = 0
        else:
            self.speed -= 10

    def increase_speed(self):
        for speed in range(self.speed, self.max_speed + 1, 3):
            print(f"Current speed of {self.make}: {speed} km/h")
