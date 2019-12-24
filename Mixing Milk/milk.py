"""
ID: sudarsh11
LANG: PYTHON3
TASK: milk
"""
import heapq

market = []
with open("milk.in", "r") as fin:
    N, M = map(int, fin.readline().rstrip().split())
    for line in map(str.rstrip, fin):
        price, amount = map(int, line.split())
        heapq.heappush(market, (price, amount))

min_cost = 0
while N > 0:
    price, amount = heapq.heappop(market)
    if amount > N:
        min_cost += price * (amount - N)
        N -= amount - N
    else:
        min_cost += price * amount
        N -= amount
with open("milk.out", "w") as fout:
    fout.write(str(min_cost) + "\n")
