from Constructor.Employee import Employee


class Manager(Employee):
    def __init__(self, name, age, job_title, salary, department):
        super().__init__(name, age, job_title, salary)
        self._department = department

    # Геттер и сеттер для департамента
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    # Метод класса Manager
    def display_manager_info(self):
        print(f"Manager: {self.name}, Department: {self.department}")

    # Метод для изменения департамента
    def change_department(self, new_department):
        self._department = new_department
        print(f"Department changed to {self.department}")