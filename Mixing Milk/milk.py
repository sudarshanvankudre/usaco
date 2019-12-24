"""
ID: sudarsh11
LANG: PYTHON3
TASK: milk
"""
import heapq

market = []
with open("milk.in", "r") as fin:
    N, M = map(int, fin.readline().rstrip().split())
    for line in map(lambda x: x.rstrip().split(), fin):
        price, amount = map(int, list(line))
        print(price, amount)
