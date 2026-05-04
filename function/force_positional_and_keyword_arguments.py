# you can call as postional-only or keyword-only
def myfun(a,b,c):
    s = a + b +c
    return s

s = myfun(a=30,b=40,c=50)
print(s)
s1 = myfun(30,40,50)
print(s1)


# Here x,y,z is positional or keyword parameter
def myfun1(a,b,c,/,x,y,z,*,m,n):
    s = a + b + c + m + n + x + y + z
    return s

s2 = myfun1(30,40,50,x=1000,y=2000,z=3000,m=100,n=200)
print(s2)

s2 = myfun1(30,40,50,1000,2000,3000,m=100,n=200)
print(s2)
