class Employee:
    def __init__(self):
        self.salary = 24000
        self.age = 21


e1 = Employee()
e2 = Employee()

print(e1.__dict__) # show the content of object in dictionary