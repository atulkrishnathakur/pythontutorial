class Person:
    def __init__(self,myname,myage):
        self.name = myname  # self.name is instance attribute
        self.age = myage
        
    @classmethod
    def msg(cls): # you can write anything instead of cls
       print("Hello Friends")
       
       
obj = Person("Rave",25)
obj.msg()
Person.msg()

