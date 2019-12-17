"""
ID: sudarsh11
LANG: PYTHON3
TASK: milk2
"""
import heapq

with open("milk2.in", 'r') as fin:
    N = int(fin.readline())
    milking_intervals = []
    for line in map(str.rstrip, fin):
        temp = tuple(map(int, line.split()))
        heapq.heappush(milking_intervals, (temp[0], temp[1]))

mint = milking_intervals[:]
prev = list(heapq.heappop(mint))
max_milking_time = prev[1] - prev[0]
while len(mint) > 0:
    temp = heapq.heappop(mint)
    if prev[0] <= temp[0] <= prev[1] <= temp[1]:
        max_milking_time = max(max_milking_time, temp[1] - prev[0])
        prev[1] = temp[1]
    elif temp[0] > prev[1]:
        max_milking_time = max(max_milking_time, temp[1] - temp[0])
        prev = list(temp)

max_idle_time = 0
t = heapq.heappop(milking_intervals)
curr = t[1]
while len(milking_intervals) > 0:
    temp = heapq.heappop(milking_intervals)
    if curr < temp[0]:
        max_idle_time = max(max_idle_time, temp[0] - curr)
    if curr < temp[1]:
        curr = temp[1]

with open("milk2.out", 'w') as fout:
    fout.write("{} {}\n".format(str(max_milking_time), str(max_idle_time)))
