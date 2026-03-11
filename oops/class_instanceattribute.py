class Person:
    def __init__(self,myname,myage):
        self.name = myname  # self.name is instance attribute
        self.age = myage
    
personobj = Person("Rahul",100)
print(personobj.name)  
