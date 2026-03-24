import threading
import time 

e = threading.Event()

def task():
    print("Game is started ......")
    time.sleep(5)
    e.set()  # change the thread flag from "False" to "True"


def end():
    e.wait() # wait for t1 thread
    if e.is_set(): # is_set return True when t1 thread set True then code will execute 
        print("Code for destroying session")


t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)

t1.start()
t2.start()