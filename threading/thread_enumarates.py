from threading import Thread, enumerate

def display():
    for i in range(4):
        print("hello world")
   
def show():
    for i in range(3):
        print("hii")

t1 = Thread(target=display)
print("Before:",enumerate()) # Print a list with thread details
t1.start()
print("After:",enumerate()) # Print a list with thread details