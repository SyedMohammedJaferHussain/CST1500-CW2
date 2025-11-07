from threading import Thread, Lock
from time import sleep

class CWThreads (Thread): #Creating class CWThreads to contain thread burst time and threat number
    def __init__ (self, burstTime: int, tNo: int):
        Thread.__init__(self)
        self.burstTime: int = burstTime
        self.tNo: int = tNo
    
    def run(self): #Overwriting existing Thread().run() function
        tLock.acquire() #Using Lock().acquire() and .release() to allow for synchronisation between threads
        ExecThread(self)
        tLock.release()
        return

processCounter: int = 0
tLock = Lock()

def ExecThread(thread: CWThreads) -> None:
    print(f"Thread {thread.tNo} started")
    sleep(thread.burstTime)   
    print(f"Thread {thread.tNo} ended")      

threadBurst: dict[int, list[CWThreads]] = dict() #Dictionary of form burstTime: list[CWThreads]. This allows for sorting burstTime and knowing which burstTime is mapped to which thread
burstTimes: list[int] = [] #List containing all burst times
threads: list[CWThreads] = [] #List containing all threads
tNo: int = 1 #Thread Number
while True:
    userCh: str = input("1) Add a new thread\n2) Exit Loop\n")
    if userCh == "2":
        break
    
    burstTime: int = int(input("Enter burst time(secs): "))
    
    thread: CWThreads = CWThreads(burstTime, tNo)
    threads.append(thread)
    if burstTime in threadBurst:   
        threadBurst[burstTime] += [thread]
    else:
        threadBurst[burstTime] = [thread]
    burstTimes.append(burstTime)
    
    tNo += 1

burstTimes.sort() 

for burstTime in burstTimes:
    for thread in threadBurst[burstTime]:
        thread.start()

for thread in threads:  
    thread.join()
    
print("All threads ended")