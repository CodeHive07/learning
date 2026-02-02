# FCFS CPU Scheduling with Arrival Time

n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    at = int(input(f"Arrival time of P{i+1}: "))
    bt = int(input(f"Burst time of P{i+1}: "))
    processes.append((i+1, at, bt))

# Sort by arrival time (FCFS rule)
processes.sort(key=lambda x: x[1])

current_time = 0
wt = {}
tat = {}

for pid, at, bt in processes:
    # CPU idle if process arrives later
    if current_time < at:
        current_time = at

    wt[pid] = current_time - at
    current_time += bt
    tat[pid] = wt[pid] + bt

# Display results
print("\nProcess  AT  BT  WT  TAT")
for pid, at, bt in processes:
    print(f"P{pid}\t  {at}   {bt}   {wt[pid]}   {tat[pid]}")

avg_wt = sum(wt.values()) / n
avg_tat = sum(tat.values()) / n

print(f"\nAverage Waiting Time = {avg_wt:.2f}")
print(f"Average Turnaround Time = {avg_tat:.2f}")
