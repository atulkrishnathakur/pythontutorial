import threading
print(threading.current_thread())
print(threading.current_thread().name) # name of thread
print(threading.current_thread().ident) # thread indentity. it is vary when you run again.
print(threading.current_thread().is_alive()) # true if thread started