print("***********START 1***************")

try:
    print(a)
except Exception as e:
    print(e)

print("***********END 1*****************")


print("***********START 2***************")

try:
    print(b)
except Exception as e1:
    print(e1)

print("***********END 2*****************")



print("***********START 3***************")

try:
    colors = ['red', 'green', 'blue']
    print(colors[3])
except Exception as e2:
    print(e2)

print("***********END 3*****************")