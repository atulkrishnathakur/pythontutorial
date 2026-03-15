from threading import Thread, active_count

def display():
    for i in range(4):
        print("hello world")
   
def show():
    for i in range(3):
        print("hii")

t1 = Thread(target=display)
print("Before:",active_count()) # before start print 1 only for the main thread
t1.start()
print("After:",active_count()) # After start count = total thread + 1(for the main thread) 