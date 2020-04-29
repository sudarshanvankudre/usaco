"""
ID: sudarsh11
LANG: PYTHON3
TASK: combo
"""
import itertools

with open('combo.in', 'r') as fin:
    N = int(fin.readline())
    john_combo = [int(i) for i in fin.readline().split()]
    master_combo = [int(i) for i in fin.readline().split()]

def tolerance(x):
    """Returns a set of numbers that are "close" to x for combination purposes"""
    ans = set()
    for i in range(-2, 3):
        ans.add((x - 1 + i) % N + 1)
    return ans

def john_valid(combo):
    """Returns true if combo is valid for john_combo"""
    for j, i in zip(john_combo, combo):
        # print("j: ", j)
        # print("i: ", i)
        if i not in tolerance(j):
            return False
    return True

def master_valid(combo):
    """Returns true if combo is valid for master_combo"""
    for m, i in zip(master_combo, combo):
        if i not in tolerance(m):
            return False
    return True

count = 0
for c in itertools.product(range(1, N + 1), repeat=3):
    if john_valid(c) or master_valid(c):
        count += 1

with open('combo.out', 'w') as fout:
    fout.write(str(count) + "\n")
