# import Thread class
from threading import Thread, current_thread

# create a function containing code to be executed parallaly
def display(n):
    print("T1 Thread Detais:", current_thread().name)
    for i in range(n):
        print("Hello World")

#Create new thread here
t1 = Thread(target=display,args=(5,)) # args is tuple

#start the new thread
t1.start()

for i in range(5):
    print("hello")
