from threading import Thread

def display():
    for i in range(4):
        print("hello world") 

def show():
    for i in range(3):
        print("Welcome")

t1 = Thread(target=display)
t2 = Thread(target=show)

print(t1.name)
print(t2.name)


# Thread name show like "Thread-[%d]". Example Thread-1, Thread-2
# Main Thread name is `MainThread`