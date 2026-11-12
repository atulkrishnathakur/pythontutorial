def fun1():
    # It will execute
    print("************Start fun1***************")
    # Give exception because 'a' not defined
    print(a)
    # It will not execute because this statement written after print(a)
    print("**********End fun2************")


def fun2():
    # It will execute
    print("************Start fun2***************")
    try:
        print("before b")
        print(b)

        # It will not execute because it written after exception error statment
        print("after b")

    except Exception as e:
        print("Exception details: ",e)

    # It will execute because exception handled
    # And it written out of try and except
    print("**********End fun2************")

def fun1():
    # It will execute
    print("************Start fun1***************")
    # Give exception because 'a' not defined
    print(a)
    # It will not execute because this statement written after print(a)
    print("**********End fun2************")


def fun2():
    # It will execute
    print("************Start fun2***************")
    try:
        print("before b")
        print(b)

        # It will not execute because it written after exception error statment
        print("after b")

    except Exception as e:
        print("Exception details: ",e)

    # It will execute because exception handled
    # And it written out of try and except
    print("**********End fun2************")

fun1()

# fun() not executed becuase fun1() not handle exception and executed first
fun2()
