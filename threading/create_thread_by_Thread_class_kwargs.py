# import Thread class
from threading import Thread

# create a function containing code to be executed parallaly
def display(n,msg):
    for i in range(n):
        print(msg)

#Create new thread here
t1 = Thread(target=display,kwargs={'n':5,'msg':'hello'}) # kwargs is dictionary

#start the new thread
t1.start()