def fun(m):
    return lambda a,b: a + b + m
    
lmd = fun(100)
print(lmd(10,20))
