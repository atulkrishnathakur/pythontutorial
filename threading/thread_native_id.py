from threading import Thread, get_native_id

def display():
    print("native id of t1:",get_native_id())
    for i in range(4):
        print("hello world")
   
def show():
    for i in range(3):
        print("hii")

t1 = Thread(target=display)
t1.start()
print("Native id of main thread:",get_native_id()) # Print a list with thread details