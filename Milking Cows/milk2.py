"""
ID: sudarsh11
LANG: PYTHON3
TASK: milk2
"""
with open("milk2.in", 'r') as fin:
    N = int(fin.readline())
    milking_intervals = []
    for line in map(str.rstrip, fin):
        interval = tuple(map(int, line.split()))
        milking_intervals.append(interval)

max_milking_time = 0
for i in range(N):
    max_milking_time = max(max_milking_time, milking_intervals[i][1] - milking_intervals[i][0])
    for j in range(N):
        if i != j:
            if milking_intervals[i][0] <= milking_intervals[j][0] <= milking_intervals[i][1]:
                max_milking_time = max(max_milking_time, milking_intervals[j][1] - milking_intervals[i][0])
