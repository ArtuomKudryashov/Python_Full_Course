class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


my_car = Car()
print(my_car)
print(type(my_car))
print(isinstance(my_car,Car))
print(isinstance(my_car,object))

my_second_car = Car()
print(id(my_car))
print(id(my_second_car))

my_car.move()
my_car.stop()

Car.move(my_second_car)
Car.move(my_car)
