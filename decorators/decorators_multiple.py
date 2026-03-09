def msgmodifier(func):
    def wrapper():
        oldmsg = func()
        newmsg = oldmsg+" New hello"
        return newmsg
    return wrapper



@msgmodifier
def mymsg1():
    return "Hello 1"


@msgmodifier
def mymsg2():
    return "Hello 2"


@msgmodifier
def mymsg3():
    return "Hello 3"



dt1 = mymsg1()
dt2 = mymsg2()
dt3 = mymsg3()
print(dt1)
print(dt2)
print(dt3)