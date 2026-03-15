from threading import Thread, main_thread

def display():
    print("main thread details:", main_thread()) # print the main thread status
    for i in range(4):
        print("hello world")

    
def show():
    for i in range(3):
        print("hii")

t1 = Thread(target=display)
print("Before:",t1.is_alive()) # print status before running thread
t1.start()
print("After:",t1.is_alive()) # print status after running thread