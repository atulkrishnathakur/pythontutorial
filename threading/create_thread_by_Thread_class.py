# import Thread class
from threading import Thread

# create a function containing code to be executed parallaly
def display():
    for i in range(4):
        print("Hello World")

#Create new thread here
t1 = Thread(target=display)

#start the new thread
t1.start()