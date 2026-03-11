def sum(a, b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b


def calculation(a,b):
    abc = sum(a, b)
    efg = sub(a, b)
    hij = mul(a, b)
    return abc + efg + hij

result = calculation(20,10)
print(result)  # 20
