def calculate_fcfs(processes):
    # Number of processes
    n = len(processes)

    # Initialize waiting time and turn-around time lists
    waiting_time = [0] * n
    turn_around_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = processes[i - 1][1] + waiting_time[i - 1]

    # Calculate turn-around time
    for i in range(n):
        turn_around_time[i] = processes[i][1] + waiting_time[i]

    # Averages
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turn_around_time) / n

    return waiting_time, turn_around_time, avg_waiting_time, avg_turnaround_time


# ---------------------------
# Main program
# ---------------------------
n = int(input("Enter the number of processes: "))
processes = []

# Input burst times
for i in range(n):
    burst_time = int(input(f"Enter burst time for process {i+1}: "))
    processes.append((i + 1, burst_time))

# Calculate FCFS results
waiting_time, turn_around_time, avg_wait, avg_tat = calculate_fcfs(processes)

# Output results
print("\nProcess | Burst Time | Waiting Time | Turn Around Time")
print("--------------------------------------------------------")

for i in range(n):
    print(f"{processes[i][0]:<7} | {processes[i][1]:<10} | {waiting_time[i]:<12} | {turn_around_time[i]:<16}")

# Print averages
print(f"\nAverage Waiting Time: {avg_wait:.2f}")
print(f"Average Turn Around Time: {avg_tat:.2f}")
