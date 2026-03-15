from threading import Thread, current_thread

def display():
    for i in range(4):
        print("hello world") 

def show():
    for i in range(3):
        print("Welcome")

t1 = Thread(target=display)
t1.name ="first_thread" # Thread name has chaged
t2 = Thread(target=show)

print(t1.name)

current_thread().name = "atul_main_thread" # Main Thread name has changed
print(current_thread().name)

# Thread name show like "Thread-[%d]". Example Thread-1, Thread-2
# Main Thread name is `MainThread`