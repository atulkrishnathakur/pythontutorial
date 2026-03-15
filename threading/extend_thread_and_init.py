from time import sleep
from threading import Thread
videos = ['OOP sylabus', 'constructor', 'file handling']

class Myclass(Thread):
    def __init__(self,val):
        self.kid = val
        Thread.__init__(self)
    def compression(self):
        print("Video compression code")

    def run(self): # run method of Thread class is overloaded here
        self.compression()
        if self.kid:
            print("Suitable for kid")
            
        for vid in videos:
            print(f"{vid} started uploading... ")
            sleep(3)
            print(f"{vid} uploaded... ")


t1 = Myclass(True)
t1.start()

for i in range(4):
    sleep(0.5)
    print("Checking copyrights")