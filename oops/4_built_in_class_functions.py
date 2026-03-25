class Employee:
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag


e1 = Employee("Atul", 21)
e2 = Employee("Krishna",31)

e1age = getattr(e1,'age')
print(e1age) # 21
setattr(e2,'name','Jay')
print(e2.__dict__)
delattr(e2,'age')
print(e2.__dict__)
print(hasattr(e2,'age')) # False

