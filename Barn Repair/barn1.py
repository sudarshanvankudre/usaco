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
    cow_stalls = sorted(stall for stall in map(int, fin))


# we have M boards which we can use. The greedy solution is to find the best
# solution for some amount of boards and then use that. we want to iterate
# through every possible number of boards
num_stalls_blocked = cow_stalls[len(full_stalls) - 1] - cow_stalls[0] + 1
covered_stalls = [interval(cow_stalls[0], cow_stalls[1])]
for possible_boards in range(2, M + 1):
        for _ in range(possible_boards):
            
