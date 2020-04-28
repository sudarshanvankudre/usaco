"""
ID: sudarsh11
LANG: PYTHON3
TASK: crypt1
"""
import itertools
import math

with open('crypt1.in', 'r') as fin:
    N = int(fin.readline())
    digits = {int(c) for c in fin.readline().split()}

def is_valid(n, needed_count):
    count = 0
    while n:
        digit = n % 10
        if digit not in digits:
            return False
        n = n // 10
        count += 1
    if count != needed_count:
        return False
    return True

count = 0
for p in itertools.product(digits, repeat=5):
    a, b, c, d, e = p
    abc = a * 100 + b * 10 + c
    p1 = abc * e
    p2 = abc * d
    final_sum = p1 + 10 * p2
    if is_valid(p1, 3) and is_valid(p2, 3) and is_valid(final_sum, 4):
        count += 1

with open('crypt1.out', 'w') as fout:
    fout.write(str(count) + "\n")
