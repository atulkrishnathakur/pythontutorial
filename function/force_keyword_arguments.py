
# after * every argument must be keyword argument. After * every argument is keyword only orgument
# If * not given then you can call with keyword or positional argument myfun(30,40,50) or myfun(a=30,b=40,c=50)
# If * given then you must call with keyword argument myfun(a=30,b=40,c=50)
# If you not give keyword it will give error
# Keyword-only parameters are placed after * . 

def myfun(*,a,b,c):
    s = a + b +c
    return s

s1 = myfun(a=30,b=40,c=50)
print(s1)



def myfun1(m,n,*,a,b,c):
    s = a + b +c + m + n
    return s

s2 = myfun1(100,200,a=30,b=40,c=50)
print(s2)