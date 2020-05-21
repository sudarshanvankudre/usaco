"""
ID: svankudre
TASK: moobuzz
LANG: PYTHON3
"""

def moo(n):
    return n % 3 == 0 or n % 5 == 0 or n % 15 == 0

with open('moobuzz.in', 'r') as fin:
    N = int(fin.readline())

div, mod = divmod(N, 8)
if mod == 0:
    curr = (div - 1) * 15 + 1
    N = 8
else:
    curr = div * 15 + 1
    N = mod


count = 0
while count < N:
    if not moo(curr):
        count += 1
    curr += 1

ans = curr - 1


with open('moobuzz.out', 'w') as fout:
    fout.write(str(ans) + "\n")
