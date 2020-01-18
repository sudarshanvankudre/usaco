"""
ID: sudarsh11
LANG: PYTHON3
TASK: barn1
"""
def interval(start, end):
    return start, end

def start(interval):
    return interval[0]

def end(interval):
    return interval[1]

def size(interval):
    return interval[1] - interval[0] + 1
    
with open("barn1.in", "r") as fin:
    M, S, C = map(int, fin.readline().rstrip().split())
    full_stalls = sorted(stall for stall in map(int, fin))


# we have M boards which we can use. The greedy solution is to find the best
# solution for some amount of boards and then use that. we want to iterate
# through every possible number of boards
stalls_blocked = full_stalls[len(full_stalls) - 1] - full_stalls[0] + 1
for possible_boards in range(M):
