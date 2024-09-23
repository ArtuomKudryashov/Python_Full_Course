from Rectangle import  Rectangle
from Car import Car
from Car2 import Car2
from BankAccount import BankAccount
from OverdraftAccount import OverdraftAccount
class App:
    def runner (self):
        print("<<<<<<<<<<<<<<<<<<<<SquareRectangle>>>>>>>>>>>>>>>>>>")

        rectangle = Rectangle(5,6)
        rectangle.area_info()

        rectangle._width = 15
        rectangle.area_info()

        rectangle._width=10
        rectangle.height = 20
        rectangle.area_info()

        rectangle._width=2
        rectangle.height =4
        rectangle.area_info()
        rectangle.perimetr_info()

        print("<<<<<<<<<<<<<<<<<<<<Car>>>>>>>>>>>>>>>>>>")
        toyota = Car("Toyota",180)
        print(toyota.__str__())
        toyota.accelerate()
        print(toyota.__str__())
        toyota.brake()
        print(toyota.__str__())

        toyota.increase_speed()
        print(toyota.__str__())


        print("<<<<<<<<<<<<<<<<<<<<Car2>>>>>>>>>>>>>>>>>>")
        cars = []


        for i in range(4):
            make = f"Car {i + 1}"
            max_speed = 150 + i * 50
            car = Car2(make, max_speed)

            if i == 1:
                car.color = "Red"
            elif i == 2:
                car.color = "Blue"
                car.engine_type = "V6"
            elif i == 3:
                car.color = "Black"
                car.engine_type = "V8"
                car.year = 2023

            cars.append(car)


        print("<<<<<<<<<<<<<<<<<<<<Print Car2>>>>>>>>>>>>>>>>>>")
        for car2 in cars:
            print(car2)
        print(car.__str__())
        print(toyota.__str__())


        print("<<<<<<<<<<<<<<<<<<<<BankAccount>>>>>>>>>>>>>>>>>>")
        account = BankAccount("Maria",1000)
        account.deposit(700)
        account.withdraw(200)
        print(account.get_balance())
        account.withdraw(2000)
        print(account.get_balance())

        print("<<<<<<<<<<<<<<<<<<<<OverDraft>>>>>>>>>>>>>>>>>>")
        overDraft = OverdraftAccount("Jack",0)
        overDraft.deposit(500)
        rem=overDraft.get_balance()
        print(rem)
        # for remain in range(rem,-1,-100):
        #     print(remain)

        while rem > -1000:
            print(rem)
            rem -= 100  # Уменьшаем на 100 на каждом шаге

        print("Цикл завершён, так как остаток достиг -1000 или меньше")




if __name__ == "__main__":
    print("Код выполняется на прямую")
    app = App()
    app.runner()