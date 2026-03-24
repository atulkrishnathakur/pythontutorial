import threading
from time import sleep

def custom_hook(args):
    print("Exception occured in thread")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])


def display():
    for i in range(4):
        sleep(2)
        print("Hello"+2)

def show():
    for i in range(4):
        print("world")
        sleep(0.5)

threading.excepthook=custom_hook # here override custom exception so no need to use try-except in display
t1 = threading.Thread(target=display)
t2 = threading.Thread(target=show)
t1.start()
t2.start()

t1.join()
t2.join()

for i in range(4):
    print("Bye")