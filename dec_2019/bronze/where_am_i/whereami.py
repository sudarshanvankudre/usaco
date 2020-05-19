"""
ID: svankudre
TASK: whereami
LANG: PYTHON3
"""
import itertools

def length_k_substrings(string, k):
    for i in range(0, len(string) - k + 1):
        yield string[i:i+k]


with open('whereami.in', 'r') as fin:
    N = int(fin.readline())
    mailboxes = fin.readline().rstrip()

for k in range(1, N + 1):
    substrings = set()
    valid = True
    for s in length_k_substrings(mailboxes, k):
        if s in substrings:
            valid = False
        else:
            substrings.add(s)
    if valid:
        break

with open('whereami.out', 'w') as fout:
    fout.write(str(k) + "\n")
