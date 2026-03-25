class Student:
    def __init__(self,nm,m):
        self.name = nm # name is instance variable
        self.marks = m  # marks is instance variable


std1 = Student("Atul",70)
std2 = Student("Krishna",80)

std2.age = 30 # instance variable created outside of class
print(std1.__dict__)
print(std2.__dict__)