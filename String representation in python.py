#String representation in python

#The use of __str__() method:
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary  

    #Add the __str__() method
    def __str__(self):
        emp="""
            Employee
                Employee name:{name}
                Employee salary:{salary}
        """.format(name=self.name,salary=self.salary)
        return emp

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)


#The use of __repr__() method:
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    #Add the __repr__method  
    def __repr__(self):
        return "Employee('{name}',{salary})".format(name=self.name, salary=self.salary)      
    
emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))