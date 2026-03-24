import threading
import time 

def write_data():
    con.acquire()
    with open('report.txt','w') as file1:
        days = ['Monday','Tuesday','wednesday','thursday','friday','Saturday','Sunday']
        for day in days:
            temp = input(f"Enter the temperatur for {day}")
            file1.write(temp+"\n"
                       )
    con.notify_all() # use notify_all() for the all thread and notify() for the one thread
    con.release()
    
def max_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt','r') as file1:
        data=file1.readlines() # return list 
        max1=float(data[0].strip("\n")) # strip \n
        for temp in data[1:]:
            temp = float(temp.strip("\n"))
            if temp > max1:
                max1 = temp
    print("Maximum temprature is:",max1)
    con.release()

def avg_temp():
    con.acquire()
    con.wait(timeout=0)
    with open('report.txt','r') as file1:
        data=file1.readlines() # return list 
        sum1 = 0
        for temp in data:
            temp = float(temp.strip("\n"))
            sum1 = sum1+temp
            avg = sum1/len(data)
    print("avarage temprater for week:",avg)
    con.release()

con = threading.Condition()
t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)
t1.run() # run the thread
t2.run()
t3.run()