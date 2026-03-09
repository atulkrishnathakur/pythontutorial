def msgmodyfier(func):
    def wrapper():
        oldmsg = func()
        return oldmsg+" and new hello"
    return wrapper

@msgmodyfier
def msg():
    return "hello"

dt = msg()
print(dt)

