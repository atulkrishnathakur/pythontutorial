from threading import *
from time import sleep

lock = Lock()

class Bus:
    def __init__(self,name,available_seats,l):
        self.available_seats = available_seats
        self.name = name
        self.l = l

    def reserve(self, need_seats):
        # self.l.acquire(blocking=True,timeout=-1) 
        self.l.acquire() # acquire(blocking=True,timeout=-1) has defautl parameters. it is same acquire()
        print("Available seats are: ",self.available_seats)
        if self.available_seats>=need_seats:
            nm = current_thread().name
            #ticket booking code goes here. Update in to the database.
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats -= need_seats
        else:
            print("Sorry! seats are not available. ")
        self.l.release()

b1 = Bus("Mahalaxmi Travels......",2,lock)
t1 = Thread(target=b1.reserve, args=(2,), name="Jai")
t2 = Thread(target=b1.reserve, args=(1,), name="Raj")
t1.start()
t2.start()
        