class Demo:
    pass 

class Employee:
    ''' This is employee class to maintain employee data '''
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag


e1 = Employee("Atul", 21)
e2 = Employee("Krishna",31)


print(isinstance(e1, Employee)) # Return True if e1 is the object of Employee class
print(isinstance(e2, Demo)) # Return True if e1 is the object of Employee class


