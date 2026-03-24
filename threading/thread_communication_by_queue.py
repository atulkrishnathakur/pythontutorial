from time import sleep
from threading import Thread
from queue import Queue

def producer(my_que):
    print("producer:running")
    n = int(input("Enter number of Students:"))
    for i in range(n):
        marks = float(input("Enter marks: "))
        my_que.put(marks)
    my_que.put(None)

    print("Producer: end")

def consumer(my_que):
    print("Consumber: running...")
    while True:
        item = my_que.get()
        if item is None:
            break
        print(f"Got {item}")
    print("Consumer end")


my_que = Queue()

t1 = Thread(target=producer,args=(my_que,))
t2 = Thread(target=consumer,args=(my_que,))
t1.start()
t2.start()