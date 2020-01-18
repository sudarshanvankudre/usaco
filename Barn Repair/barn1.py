"""
ID: sudarsh11
LANG: PYTHON3
TASK: barn1
"""
with open("barn1.in", "r") as fin:
    M, S, C = map(int, fin.readline().rstrip().split())
    full = set()
    for stall in map(int, fin):
        full.add(stall)
# we have M boards which we can use. The greedy solution is to find the best
# solution for some amount of boards and then use that. we want to iterate
# through every possible number of boards
for possible_boards in range(M):
    
