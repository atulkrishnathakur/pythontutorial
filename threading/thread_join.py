from threading import Thread 
from time import sleep

def upload():
    print("uploading start...")
    sleep(3)
    print("video uploaded...")


def notification():
    print("Sending notification to subscribers code")

t1 = Thread(target=upload)
t2 = Thread(target=notification)

t1.start()
t1.join()
t2.start()
t2.join()

for i in range(4):
    print("Hello.............")


'''
1. If a thread wants to wait for some other thread, then we should go for join() method.
2. t1.join() used so t2 will wait for the t1 execution ater that t2 will be execute
3. t2.join() used so main thread code will wait of t2 thread execution

'''
