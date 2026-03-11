class Person:
   myname = "Ravi"
   yourame= "Rahul"
   
 
obj = Person()

# print(Person.age)   # age not available. give error
print(getattr(Person,'age','0')) # you can age value to avoid error
