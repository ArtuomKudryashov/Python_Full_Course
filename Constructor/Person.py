class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Геттер и сеттер для имени
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # Геттер и сеттер для возраста
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Возраст не может быть отрицательным")

    # Метод класса Person
    def display_info(self):
        print(f"Person: {self.name}, Age: {self.age}")
