class Employee:
    def __init__(self, name, salary):
        self.name=name
        self._dept="IT"
        self.__salary=salary

    def get_salary(self):
        return self.__salary
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount.")
emp = Employee("Dee", 50000)
print(emp.name)  
print(emp.get_salary())
emp.set_salary(60000)
emp.set_salary(-100)