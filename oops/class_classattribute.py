class Person:
    personcounter = 1 # class attribute
    mycounter = 0
    
    def __init__(self,myname,myage):
        self.name = myname  # self.name is instance attribute
        self.age = myage  
        Person.mycounter += 1
        
obj1 = Person("Rahul",25)
obj2 = Person("Mohan",30)
a = Person.personcounter # access class attribute with Class
b = obj1.personcounter   # access class attribute with instance 
c = Person.mycounter
d = Person.mycounter
e = obj2.mycounter

print(a)
print(b)
print(c)
print(d)
print(e)
          
