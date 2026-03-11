def fun1(*para):
     # here para will be a tuple
    r = para[0] + para[1] + para[2] + para[3]
    
    return r
    
# function calling    
result = fun1(10,20,30,40)
print(result)    
