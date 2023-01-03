#Tutorial 1: Classes and Instances

class Employee:
    def __init__(self, name, salary, department, bonus): #metoda __init__ initializeaza atributele clasei
        self.name = name
        self.salary = salary
        self.department = department
        self.bonus = bonus

    def total_salary(self):   #o functie a unei Clase se numeste metoda. Intotdeauna are 'self' ca argument.
        return self.salary * 12 + self.bonus

emp1 = Employee('Rares', 4100, 'iGestion', 1000)
emp2 = Employee('Bob', 50000, 'sales', 10000)

print (emp1)
print(emp1.salary)
print (emp2.total_salary())
