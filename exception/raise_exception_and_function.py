def fun1():
    print("******** start fun1 *************")
    try:
        a = 100
        print(a)
    except Exception as e:
        raise Exception("message: variable a is not defined")

    try:
        colors = ['red', 'green', 'blue']
        c = colors[3]
        print(c)
    except IndexError as ie:
        raise IndexError("Index not found")
    except Exception as e:
        raise Exception("Error found")

    print("******** end fun1 *************")

def fun2():
    try:
        print("******** start fun2 *************")
        print(b)
        print("******** end fun2 *************")
    except Exception as e:
        raise Exception("message: variable b is not defined")



def main():
    try:
        fun1()
        fun2()
    except Exception as e:
        print("details:",e)

main()

'''
fun1() handle the exception and raise exception because it is called by main() function
fun2() handle the exception and raise exception because it is called by main() function
main() function handle the exception but not raise because it is main function that call and executed every thing
'''