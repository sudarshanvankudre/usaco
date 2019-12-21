"""
ID: sudarsh11
LANG: PYTHON3
TASK: namenum
"""
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

    else:
        ret_val = []
        for m in mapping[brand[0]]:
            ret_val.append([[m] + [c] for c in possible_names(brand[1:])])
        return ret_val
        return [[brand[0]] + [c] for c in possible_names(brand[1:])]

print(possible_names(4734))
