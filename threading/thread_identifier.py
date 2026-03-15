from threading import Thread

def display():
    for i in range(4):
        print("hello world") 

def show():
    for i in range(3):
        print("Welcome")

t1 = Thread(target=display)
t2 = Thread(target=show)

t1.start()
t2.start()

print(t1.ident)
print(t1.native_id)
