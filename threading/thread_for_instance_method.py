from threading import Thread

class Example:
    def display(self,n):
        for i in range(n):
            print("hello world")

e1 = Example()
t1 = Thread(target=e1.display,args=(5,))
t1.start()

for i in range(4):
    print("Welcome")