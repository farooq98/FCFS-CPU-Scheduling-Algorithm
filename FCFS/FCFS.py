from prettytable import PrettyTable

num = int(input("Please Enter Number of Processes: "))
process_lst = []
process_names = []
average_WT = 0
average_TAT = 0

for i in range(num):
    arrival_time = int(input(f"Please Input Arrival time for P{i+1}: "))
    burst_time = int(input(f"Please Input Burst Time for P{i+1}: "))
    process_lst.append([arrival_time, burst_time])
    process_names.append(f"P{i+1}")

sorted_lst = sorted(process_lst, key = lambda x : x[0])
for val in sorted_lst:
    idx = process_lst.index(val)
    val.insert(0, process_names[idx])

process_lst = []
for i, val in enumerate(sorted_lst):
    pname, arrival_time, burst_time = val 
    completion_time = burst_time + arrival_time if len(process_lst) == 0 else burst_time + process_lst[i-1][3] if arrival_time < process_lst[i-1][3] else burst_time + process_lst[i-1][3] + (arrival_time - process_lst[i-1][3])
    TAT = completion_time - arrival_time
    WT = TAT - burst_time
    average_WT += WT
    average_TAT += TAT
    process_lst.append([pname, arrival_time, burst_time, completion_time, TAT, WT])

pt = PrettyTable()
pt.field_names = ["Process", "Arrival Time", "Burst Time", "Completion Time", "TAT", "WT"]
pt.add_rows(process_lst)
print(pt)
print(f"Average Waiting Time: {average_WT/num}")
print(f"Average Turn Around Time: {average_TAT/num}")

