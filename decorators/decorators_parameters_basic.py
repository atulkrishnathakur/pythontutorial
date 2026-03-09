
def myfun1modifier(func):
    def wrapper(a):
        msg = func(a)
        return msg+" Bye!"
    return wrapper


@myfun1modifier
def myfun1(para1):
    return para1+" OK"

dt1 = myfun1("hello india")
print(dt1)
