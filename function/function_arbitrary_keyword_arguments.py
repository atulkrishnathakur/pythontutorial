def fun1(**para):
     # here para will be a dictionary
    r = para["num1"] + para["num2"] + para["num3"] + para["num4"]
    
    return r
    
# function calling    
result = fun1(num1=10,num2=20,num3=30,num4=40)
print(result)    
