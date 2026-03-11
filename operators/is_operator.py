a = ["Delhi", "Patna"]
b = ["Delhi", "Patna"]
c = a

print(a is c)

# returns True because c is the same object as a

print(a is b)

# returns False because a is not the same object as b, even if they have the same content
