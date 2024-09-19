from Constructor.Person import Person


class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self._job_title = job_title
        self._salary = salary

    # Геттер и сеттер для должности
    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        self._job_title = job_title

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    # Метод класса Employee
    def display_employee_info(self):
        print(f"Employee: {self.name}, Job Title: {self.job_title}, Salary: ${self._salary}")

    # Метод для увеличения зарплаты
    def increase_salary(self, amount):
        self._salary += amount
        print(f"Salary increased by ${amount}. New salary is ${self._salary}")