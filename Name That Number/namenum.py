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


def possible_names(num):
    """Returns an iterable of all possible names based on num"""
    num = str(num)
