"""
ID: sudarsh11
LANG: PYTHON3
TASK: dualpal
"""
import itertools

with open("dualpal.in", "r") as fin:
    N, S = map(int, fin.readline().rstrip().split())

def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

def convert(num, b):
    num = int(num)
    powers = []
    div, mod = divmod(num, b)
    while div > 0:
        powers.append(mod)
        div, mod = divmod(div, b)
    powers.append(mod)
    retval = ""
    while len(powers) > 0:
        retval += str(powers.pop())
    return retval

with open("dualpal.out", "w") as fout:
    possible = itertools.count(S + 1)
    for i in possible:
        if N == 0:
            break
        palindromic = 0
        for b in range(2, 11):
            if is_palindrome(convert(i, b)):
                palindromic += 1
        if palindromic >= 2:
            N -= 1
            fout.write(str(i) + "\n")
