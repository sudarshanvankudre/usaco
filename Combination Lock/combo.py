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
    ans = []
    for i in range(-2, 3):
        ans.append((x - 1 + i) % N + 1)
    return ans

seen = set()
count = 0
for x in tolerance(john_combo[0]):
    for y in tolerance(john_combo[1]):
        for z in tolerance(john_combo[2]):
            if (x, y, z) not in seen:
                seen.add((x, y, z))
                count += 1

for x in tolerance(master_combo[0]):
    for y in tolerance(master_combo[1]):
        for z in tolerance(master_combo[2]):
            if (x, y, z) not in seen:
                seen.add((x, y, z))
                count += 1

with open('combo.out', 'w') as fout:
    fout.write(str(count) + "\n")
