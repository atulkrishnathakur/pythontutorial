from time import sleep
from threading import Thread
videos = ['OOP sylabus', 'constructor', 'file handling']

class Myclass(Thread):
    def run(self): # run method of Thread class is overloaded here
        for vid in videos:
            print(f"{vid} started uploading... ")
            sleep(3)
            print(f"{vid} uploaded... ")


t1 = Myclass()
t1.start()

for i in range(4):
    sleep(0.5)
    print("Checking copyrights")