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


# Built-in functions for threading