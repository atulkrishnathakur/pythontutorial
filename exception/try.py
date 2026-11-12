try:
    print(a)

# by default it use BaseException class because here no any class writtent
# It is called Bare exception. If you want to cach any exception then write only 'except:' without any class
# When you want to catch any exception, you can use the bare exception handlers. A bare exception handler does not specify an exception type
# A bare exception handler will catch any exceptions including the SystemExit and KeyboardInterupt exceptions.
except: 
    print("Exception found")    
