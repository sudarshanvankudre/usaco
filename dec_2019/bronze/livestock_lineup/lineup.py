"""
ID: svankudre
TASK: lineup
LANG: PYTHON3
"""
import itertools
import heapq

def check_constraints(ordering, constraints):
    for c in constraints:
        for i in range(len(ordering)):
            if ordering[i] == c[0]:
                if i == 0 and ordering[1] != c[1]:
                    return False
                elif i == len(ordering) - 1 and ordering[len(ordering) - 2] != c[1]:
                    return False
                elif ordering[i - 1] != c[1] and ordering[i + 1] != c[1]:
                    return False
    return True

cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
constraints = []

with open('lineup.in', 'r') as fin:
    N = int(fin.readline())
    for line in map(str.split, fin):
        cow1 = line[0]
        cow2 = line[5]
        constraints.append((cow1, cow2))

valid_orderings = []

for ordering in itertools.permutations(cows):
    if check_constraints(ordering, constraints):
        heapq.heappush(valid_orderings, ordering)

with open('lineup.out', 'w') as fout:
    o = valid_orderings[0]
    for cow in o:
        fout.write(cow + "\n")
