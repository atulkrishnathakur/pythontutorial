from threading import Thread

class Example:
    @staticmethod
    def display(n):
        for i in range(n):
            print("hello world")

t1 = Thread(target=Example.display,args=(5,))
t1.start()

for i in range(4):
    print("Welcome")