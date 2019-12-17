"""
ID: sudarsh11
LANG: PYTHON3
TASK: milk2
"""
def interval(start, end):
    return start, end

def start(interval):
    return interval[0]

def end(interval):
    return interval[1]

def merge(a, b):
    """Returns a merged interval of overlapping intervals"""
    if start(a) <= start(b) <= end(a) <= end(b):
        return start(a), end(b)
    elif start(b) <= start(a) <= end(b) <= end(a):
        return start(b), end(a)

def overlap(a, b):
    """Returns true if a and b overlap"""
    return start(a) <= start(b) <= end(a) <= end(b) or start(b) <= start(a) <= end(b) <= end(a)

def inside(a, b):
    """True if a is within b. ie, start(b) <= start(a) < end(a) <= end(b)"""
    return start(b) <= start(a) <= end(a) <= end(b)

def merge_list(lst):
    """Merges all intervals in lst and returns the resulting list"""


with open("milk2.in", 'r') as fin:
    N = int(fin.readline())
    milking_intervals = []
    for line in map(str.rstrip, fin):
        temp = tuple(map(int, line.split()))
        milking_intervals.append(interval(temp[0], temp[1]))


max_milking_time = 0
for i in range(N):
    max_milking_time = max(max_milking_time, milking_intervals[i][1] - milking_intervals[i][0])
    for j in range(N):
        if i != j:
            if milking_intervals[i][0] <= milking_intervals[j][0] <= milking_intervals[i][1]:
                max_milking_time = max(max_milking_time, milking_intervals[j][1] - milking_intervals[i][0])

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
