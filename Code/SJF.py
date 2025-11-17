from threading import Thread, Lock #Import necessary objects from modules
from time import sleep
from tabulate import tabulate


class CWThreads (Thread): #Creating class CWThreads to contain thread burst time and threat number
    def __init__ (self, burstTime: int, tNo: int):
        '''
            Initialise CWThreads Object with burst time and thread number as parameter
        '''
        Thread.__init__(self)
        self.burstTime: int = burstTime
        self.tNo: int = tNo
        self.waitTime: int = 0
        self.taT: int = 0 #Turnaround Time
    
    
    def run(self) -> None: #Overwriting existing Thread.run() function
        '''
            Using Lock().acquire() and .release() to allow for synchronisation between threads
        '''
        tLock.acquire() 
        ExecThread(self)
        tLock.release()


def ExecThread(thread: CWThreads) -> None:
    '''
        Prints thread started/ended and simulates thread running using time.sleep()
        Returns: None
    '''
    print(f"Thread {thread.tNo} started (BurstTime: {thread.burstTime})")
    sleep(thread.burstTime)   
    print(f"Thread {thread.tNo} ended (BurstTime: {thread.burstTime})")      


def SortThreads(lst: list[CWThreads]) -> None: 
    '''
        Uses bubble sort algorithm to sort the threads in ascending order of burst time
        Returns: None
    '''
    lenLst: int = len(lst) 
    
    for i in range(lenLst):
        swapped: bool = False
        for j in range(0, lenLst - i - 1):
            if lst[j].burstTime > lst[j + 1].burstTime:
                lst[j], lst[j+1] = lst[j+1], lst[j] #Swap if not in correct order
                swapped = True

        if (not swapped):
            break


def CreateThreads() -> list[CWThreads]: 
    '''
        Using user input to get burst times and create threads
        Returns: List containing all threads created
    '''
    threads: list[CWThreads] = []
    tNo: int = 1 #Thread Number
    while True:
        userCh: str = input("1) Add a new thread\n2) Exit Loop\n")
        if userCh != "1": #Loop terminates when user gives input
            break
        
        burstTime: int = int(input("Enter burst time(secs): "))
        threads.append(CWThreads(burstTime, tNo))
        
        tNo += 1
        
    return threads


def RunAndJoinThreads() -> None:
    '''
        Runs all threads in for loop using .start() and then joins in another for loop using .join()
    '''
    for thread in threads:        
        thread.start()

    for thread in threads:
        thread.join()


def GetWaitingAndTaT():
    '''
        Iterates through threads: list[CWThreads] and calculates waiting and turnaround time for each thread
    '''
    waitTime = taT = totalWaitTime = totalTaT = 0 #Int values
    for thread in threads:
        taT += thread.burstTime #Get wait and turnaround time
        thread.taT, thread.waitTime = taT, waitTime
        
        totalWaitTime += waitTime #Increment to totalWaitTime
        totalTaT += taT #Increment to total Turnaround Time
        
        waitTime += thread.burstTime
    
    global avgWaitTime
    global avgTaT #Float values
    avgWaitTime, avgTaT = totalWaitTime / len(threads), totalTaT / len(threads) #Get average of wait and turnaround time
    

def DisplayThreads() -> None:
    '''
        Creates a 2d matrix of form list[list] containing all details of every thread and prints a table using tabulate.tabulate()
    '''
    tDetailsMatrix: list[list] = []
    for thread in threads:
        tDetailsMatrix.append([thread.tNo, thread.burstTime, thread.waitTime, thread.taT])

    print( tabulate( tDetailsMatrix, headers = ["Process Number", "Burst Time", "Waiting Time", "Turnaround Time"], tablefmt = "psql") )
    print( tabulate( [[avgWaitTime, avgTaT]], headers = ["Average Wait Time", "Average Turnaround Time"], tablefmt = "psql") )


if __name__ == "__main__":  #In __main__
    tLock: Lock = Lock() #Create lock for synchronisation of threads
    threads: list[CWThreads] = CreateThreads() #Create all variables and store in global variable threads
    SortThreads(threads)
    RunAndJoinThreads()
    GetWaitingAndTaT()
    DisplayThreads() #Display final output after all calculations and simulations
