class Employee:
    company_name = "MyComp" # class variable
    def __init__(self,nm,sal):
        self.name = nm
        self.salary = sal 

e1 = Employee("Atul", 21)
e2 = Employee("Krishna",31)

print(Employee.company_name) # access class variable by using class reference
print(e1.company_name) # access class variable by using object
Employee.company_name = "TCS"
print(e1.company_name)
print(e2.company_name)

e2.company_name = "Infosys" # Here new company_name instance variable created. Here company_name is not a class variable of e2 object