#CODE BY SAIFANA KURADIELA MARYAM M01088086

from tabulate import tabulate   # for table formatting, must be installed
# Round Robin Algorithm Function
def round_robin_scheduling(processes, arrival_times, burst_times, quantum):
    # Variables to be used
    n = len(processes)
    # List slicing and indexing
    remaining_bt = burst_times[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    # Flags to check process statuses
    visited = [False] * n   # Checks if process is in queue
    complete = [False] * n   # Checks if process is executed fully
    queue = []   # Empty queue list
    time = 0    # Starting time of algorithim
    # List to display Gantt-Chart process order
    execution_order = []
    
    while True:
        # Adds new processes
        for i in range(n):
            if arrival_times[i] <= time and not visited[i]:
                queue.append(i)
                visited[i] = True
        # Case where arrival nothing happens, or still waiting
        if not queue:
            time += 1
            continue
        # Removes first index of queue and stores in current
        current = queue.pop(0)
        # Adds the current process that is running to Gantt Chart
        execution_order.append(processes[current])
        # Time quantum calculations and conditions
        if remaining_bt[current] > quantum:
            time += quantum
            remaining_bt[current] -= quantum
        else:  # Calculating the TA and waiting times respective to TQ
            time += remaining_bt[current]
            waiting_time[current] = time - arrival_times[current] - burst_times[current]
            turnaround_time[current] = time - arrival_times[current]
            completion_time[current] = time
            remaining_bt[current] = 0
            complete[current] = True

        # Add newly arrived processes during execution
        for i in range(n):
            if arrival_times[i] <= time and not visited[i]:
                queue.append(i)
                visited[i] = True

        if not complete[current]:   # Program that has not yet been executed
            queue.append(current)

        if all(complete):   # All programs have been executed
            break
            
    # Tabulating data
    table_data = []
    for i in range(n):
        table_data.append([
            processes[i],
            arrival_times[i],
            burst_times[i],
            waiting_time[i],
            turnaround_time[i],
            completion_time[i]
        ])
    headers = ["Process", "Arrival", "Burst", "Waiting", "Turnaround", "Completion"]
    print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))

    avg_wait = sum(waiting_time) / n
    avg_turn = sum(turnaround_time) / n
    print(f"\nAverage Waiting Time: {avg_wait:.2f}")
    print(f"Average Turnaround Time: {avg_turn:.2f}")
    # Printing the Execution Order
    print("\nExecution Order:")
    print(" -> ".join(execution_order))

# Variable lists for RR function
listprocess = []
listburst = []
listarrival = []

# User input of processes, burst times and time quantum
quantum = int(input("Enter Time Quantum: "))
process = int(input("Enter Number of Processes: "))
for i in range(process):
    burst = int(input(f"Enter Burst Time (P{i+1}): "))
    arrival = int(input(f"Enter Arrival Time (P{i+1}): "))
    listprocess.append("P" + str(i+1))
    listburst.append(burst)
    listarrival.append(arrival)
    
# Calling RR function
round_robin_scheduling(listprocess, listarrival, listburst, quantum)

