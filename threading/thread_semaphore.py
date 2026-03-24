from threading import *
import time 

#obj = Semaphore(3) #default count is 1 and bydefault it behave like RLock. But if you give the count the it execute number of thread at same time.
obj = BoundedSemaphore(4) # BoundedSemaphore is safe from Semaphore. so use BoundedSemaphore instead of Semaphore
# create instance 

def display(name):
    # calling acquire method
    # acquire:- decrement count
    obj.acquire()
    for i in range(4):
        print('hello')
        print(name)
        time.sleep(4)
    # calling release method
    obj.release()
    # release:- increment count

# creating multiple thread
t1 = Thread(target=display, args=("Thread-1",))
t2 = Thread(target=display, args=("Thread-2",))
t3 = Thread(target=display, args=("Thread-3",))
t4 = Thread(target=display, args=("Thread-4",))
t5 = Thread(target=display, args=("Thread-5",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

