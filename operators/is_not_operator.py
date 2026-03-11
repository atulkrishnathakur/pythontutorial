a = ["Delhi", "Patna"]
b = ["Delhi", "Patna"]
c = a

print(a is not c)

# returns False because c is the same object as a

print(a is not b)

# returns True because a is not the same object as b, even if they have the same content
