# multitasking
1. Executing multiple task at the same time.
2. There are two types of multitasking: 1. process based multi tasking, 2. Thread based multitasking
  
# process based multi tasking
1. Each task is an independent programm/process. Used in OS level.

# Thread based multitasking
1. Each task is an independent thread (Separate part of program). Used in programmatic level.

# What is Thread
1. A thread is operating system object that executes instructions/program
2. A thread is separate flow of execution in program
3. Each thread has separate task/sub-program

# Main Thread
1. A thread always available to execute program. It is main thread. Main Thread is OS object.
2. If you do not use thread in program then main thread will work always.
3. Supose you running a simple python script then python interpreter starts python interpreter request os for creating the thread called as main thread.
4. Any process have at least one default thread called as main thread. 
5. Main Thread is created by PVM(interpretor). PVM stands for Python Virtual Machine.
6. Main Thread is an object of `threading.Thread()` class.
7. Main Thead is also called parent thread.


# current_thread()
1. It return current working thread object details.
```
import threading
print(threading.current_thread())
```

# There are two way to create threads.
1. Using `Thread` class present in threading module
2. By Extending `Thread` class


# Thread Name
1. Thread name show like "Thread-[%d]". Example Thread-1, Thread-2
2. Main Thread name is `MainThread`


# Thread Name
1. Thread name show like "Thread-[%d]". Example Thread-1, Thread-2
2. Main Thread name is `MainThread`


# Thread Identifier
1. Each thread has a unique identifier(id) within a python process.
2. Assigned by python iterpreter
3. Read - only positive integer and unique in process.
4. assigned after starting thread
5. This identifier is stored in an instance variable:- ident.


# Native Identifier 
1. Each thread has unique identifier assigned by the operating system
2. property name: native_id(assigned after thread has started)


# thread join
1. If a thread wants to wait for some other thread, then we should go for join() method.


# What is race condition?
1. It is a bug generated when you do multi-processing. It occures because two or more threads tries to update the save variable and results into unreliable output.
2. Concurrent access to shared resource can lead to race condition.
3. There are some technique to fix race condition bug. 1. Using Locks, 2. Using R-lock, 3. Using Semaphores.


# Locks in python threading
1. threading module provides a lock class to deal with the race conditions.
2. Locks has two states.  
    2.1 **Locked:** The lock has been acquired by one thread and any thread that makes an attempt to acquire it must wait until it is released.  
    2.2 **Unlocked:** The lock has not been acquired and can be acquired by the next thread that makes an attempt.
3. follow the below steps  
    3.1 Step-1(Create an object of Lock class).  
    ```
    from threading import *
    mylock = Lock()
    ```  
    3.2 Step-2(Acquire lock using acquire())
    ```
    myloc.acquire(blocking=True,timeout=-1)
    ```  
    3.3 Step-3(Releas lock using release())
    ```
    mylock.release()
    ```   

# Rlocks in python threading
1. You cannot acquire multiple times using Lock mechanism. By using Rlock, you can acquire() multiple times.
2. Rlock is just a modified version of Lock 
3. follow the below steps  
    3.1 Step-1(Create an object of RLock class).  
    ```
    from threading import *
    mylock = RLock()
    ```  
    3.2 Step-2(Acquire lock using acquire())
    ```
    myloc.acquire()
    ```  
    3.3 Step-3(Releas lock using release())
    ```
    mylock.release()
    ``` 


# Semaphore in python threading
1. Semaphore can be used to limit the access to the shared resources with limited capacity.
2. follow the below steps  
    2.1 Step-1(Create an object of RLock class).  
    ```
    from threading import *
    s = Semaphore()
    ```  
    2.2 Step-2(Acquire lock using acquire())
    ```
    s.acquire()
    ```  
    2.3 Step-3(Releas lock using release())
    ```
    s.release()
    ``` 

# Exception in thread
1. If in one thread exception occured then other thread will work because every thread has separate memory
2. The interpreter calles threading.excepthook() with one argument i.e named tuple with 4 arguments.  
    2.1 the exception class
    2.2 exception instance/value
    2.3 A traceback object
    2.4 Thread name
3. For main thread sys.excepthook() will call
4. For the created thread threading.excepthook() will call


# Thread communication
1. In concurrent programming, sometimes we need to co-ordinate threads.
2. Thread communicate with each other via signals.
3. Three ways for thread communication:  
    3.1 By creating event object
    3.2 By creating condition object
    3.3 By using queue module 

# communicate thread using `event`
1. By `event` only two thread will communicate from each other
```
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

```

# communicate thread using `condition object`
1. It solve limitations of `event` communication

