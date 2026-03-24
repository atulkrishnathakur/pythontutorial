from threading import *
from time import sleep

l = RLock()

class Bus:
    def __init__(self,name,available_seats,rlock):
        self.available_seats = available_seats
        self.name = name
        self.rlock = rlock

    def reserve(self, need_seats):
        # self.l.acquire(blocking=True,timeout=-1) 
        self.rlock.acquire() # acquire(blocking=True,timeout=-1) has defautl parameters. it is same acquire()
        self.rlock.acquire()
        print(self.rlock)
        print("Available seats are: ",self.available_seats)
        if self.available_seats>=need_seats:
            nm = current_thread().name
            #ticket booking code goes here. Update in to the database.
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats -= need_seats
        else:
            print("Sorry! seats are not available. ")
        self.rlock.release()
        self.rlock.release()

b1 = Bus("Mahalaxmi Travels......",2,l)
t1 = Thread(target=b1.reserve, args=(2,), name="Jai")
t2 = Thread(target=b1.reserve, args=(1,), name="Raj")
t1.start()
t2.start()
        