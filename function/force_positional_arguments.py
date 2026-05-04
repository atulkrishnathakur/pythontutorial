# Before /(forward-slash) every argument must be positional argument. Before / every argument is positional-only orgument

# If / not given then you can call with keyword or positional argument myfun(30,40,50) or myfun(a=30,b=40,c=50)

# If / given then you must call with positional argument myfun(a=30,b=40,c=50)

# If you not give as positional it will give error
# Positional-only parameters are placed before a / (forward-slash). 

def myfun(a,b,c,/):
    s = a + b +c
    return s

s1 = myfun(30,40,50)
print(s1)


def myfun1(a,b,c,/,m,n):
    s = a + b +c + m + n
    return s

s2 = myfun1(30,40,50,100,200)
print(s2)