
def f1deco(func):
    def wrapper():
        func()
        print("new hello")
    return wrapper

@f1deco
def f1():
    print("hello")

f1()