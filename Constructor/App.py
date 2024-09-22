from Manager import Manager
from Person import Person
from Employee import Employee


class App:
    def run(self):
        print("<<<<<<<<<<<<<<<<<<Person>>>>>>>>>>>>>>>>")
        person = Person("John", 45)
        person.display_info()
        print("<<<<<<<<<<<<<<<<<<Employee>>>>>>>>>>>>>>>>")

        employee = Employee("Anna", 30, "Developer", 50000)
        employee.display_info()
        employee.display_employee_info()
        employee.increase_salary(60000)
        employee.salary=100000
        employee.increase_salary(15000)


        print("<<<<<<<<<<<<<<<<<<Manager>>>>>>>>>>>>>>>>")
        manager = Manager ("Mike",40, "Team Lead", 70000,"IT")
        manager.display_info()
        manager.display_employee_info()
        manager.display_manager_info()
        manager.change_department("HR")



if __name__ == "__main__":
    print("Код выполняется на прямую")
    app = App()
    app.run()
