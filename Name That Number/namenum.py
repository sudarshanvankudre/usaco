"""
ID: sudarsh11
LANG: PYTHON3
TASK: namenum
"""
import heapq

names = set()
with open("dict.txt", "r") as dictionary:
    for name in map(str.rstrip, dictionary):
        names.add(name)
fin = open("namenum.in", "r")
brand = fin.readline().rstrip()
mapping = {'2': ["A", "B", "C"], '3': ["D", "E", "F"], \
'4': ["G", "H", "I"], '5': ["J", "K", "L"], '6': ["M", "N", "O"], \
'7': ["P", "R", "S"], '8': ["T", "U", "V"], '9': ["W", "X", "Y"]}

def possible_names(brand):
    brand = str(brand)
    if len(brand) == 0:
        return [brand]
    else:
        return [m + c for m in mapping[brand[0]] for c in possible_names(brand[1:])]

valid_names = []
possible = possible_names(brand)
for n in possible:
    if n in names:
        heapq.heappush(valid_names, n)
with open("namenum.out", "w") as fout:
    if len(valid_names) == 0:
        fout.write("NONE\n")
    else:
        while len(valid_names) > 0:
            fout.write(heapq.heappop(valid_names) + "\n")
