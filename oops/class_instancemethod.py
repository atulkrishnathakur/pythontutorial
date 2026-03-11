class Person:
    def __init__(self,myname,myage):
        self.name = myname  # self.name is instance attribute
        self.age = myage
    def yourname(self):  # yourname is instance methond
        return f"Your name is: {self.name}"
personobj = Person("Rahul",100)
dataname = personobj.yourname() 
print(dataname)
