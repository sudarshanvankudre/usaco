"""
ID: svankudre
TASK: gymnastics
LANG: PYTHON3
"""
import itertools

def position(cow, ranking):
    return

with open('gymnastics.in', 'r') as fin:
    K, N = map(int, fin.readline().split())
    rankings = [list(map(int, line.split())) for line in fin]

ans = 0
for i, j in list(itertools.combinations(range(1, N+1), 2)):
    if all(r.index(i) < r.index(j) for r in rankings) or all(r.index(i) > r.index(j) for r in rankings):
        ans += 1

with open('gymnastics.out', 'w') as fout:
    fout.write(str(ans) + "\n")
