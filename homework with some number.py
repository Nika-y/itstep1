class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

class Department:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_name):
        self.employees = [emp for emp in self.employees if emp.name != employee_name]

    def total_salary(self):
        return sum(emp.salary for emp in self.employees)

emp1 = Employee("Josh", "personal bodyguard", 16000)
emp2 = Employee("Kristall", "office girl", 14000)
emp3 = Employee("Aran", "personal driver", 14000)

dept = Department()
dept.add_employee(emp1)
dept.add_employee(emp2)
dept.add_employee(emp3)

print("The total salary of the worker:", dept.total_salary())

dept.remove_employee("Josh")
print("Total salary of workers after removal Josh:", dept.total_salary())

emp4 = Employee("Eric", "personal bodyguard", 16000)
dept.add_employee(emp4)

print("Total salary of employees after hiring Eric:", dept.total_salary())