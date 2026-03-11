employee = {
      "name":"Ravi",
      "friends":['Mohan','Sohan','Amit','Rahul'],
      "country":"India"
}

name = employee.get("name")
friends = employee.get("friends")
abc = employee.get("abc") # abc key does not exist
xyz = employee.get("xyz","Value not found") # xyz does not exist 
print(name)
print(friends)
print(abc)
print(xyz)
