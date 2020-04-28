"""
ID: sudarsh11
LANG: PYTHON3
TASK: crypt1
"""

with open('combo.in', 'r') as fin:
    N = int(fin.readline())
    john_combo = [int(i) for i in fin.readline().split()]
    master_combo = [int(i) for i in fin.readline().split()]

def min_tolerance(n):
    return ((n - 2) % N) + 1

def max_tolerance(n):
    return ((n + 2) % N) + 1

range1 = 0
range2 = 0
range3 = 0

for i in range(3):
    n1 = john_combo[i]
    n2 = master_combo[i]
    
