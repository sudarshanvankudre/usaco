"""
ID: sudarsh11
LANG: PYTHON3
TASK: transform
"""

def ninety_rotation(pattern):
    """Rotates and returns pattern, which is an NxN matrix by 90 degrees clockwise.
    >>> ninety_rotation([['@', '-', '@'], ['-', '-', '-'], ['@', '@', '-']])
    [['@', '-', '@'], ['@', '-', '-'], ['-', '-', '@']]
    """
    pattern = pattern[::-1]
    transpattern = [[] for _ in range(len(pattern))]
    for i in range(len(pattern)):
        for p in pattern:
            transpattern[i].append(p[i])
    return transpattern

def one_eighty_rotation(pattern):
    """Returns pattern rotated clockwise by 180 degrees"""
    return ninety_rotation(ninety_rotation(pattern))

def two_seventy_rotation(pattern):
    """Returns pattern rotated clockwise by 270 degree"""
    return one_eighty_rotation(ninety_rotation(pattern))

def reflection(pattern):
    """Returns pattern reflected across horizontal axis.
    >>> reflection([['@', '-', '@'], ['-', '-', '-'], ['@', '@', '-']])
    [['@', '-', '@'], ['-', '-', '-'], ['-', '@', '@']]
    """
    transpattern = []
    for p in pattern:
        transpattern.append(p[::-1])
    return transpattern

def combo1(pattern):
    """Reflect and then 90 rotate"""
    return ninety_rotation(reflection(pattern))

def combo2(pattern):
    """Reflect and then 180 rotate"""
    return one_eighty_rotation(reflection(pattern))

def combo3(pattern):
    """Reflect and then 270 rotate"""
    return two_seventy_rotation(reflection(pattern))

with open("transform.in", 'r') as fin:
    N = int(fin.readline())
    og = [list(fin.readline().rstrip()) for _ in range(N)]
    trans = [list(fin.readline().rstrip()) for _ in range(N)]

transformation = 7
if trans == ninety_rotation(og):
    transformation = 1
elif trans == one_eighty_rotation(og):
    transformation = 2
elif trans == two_seventy_rotation(og):
    transformation = 3
elif trans == reflection(og):
    transformation = 4
elif any((trans == combo1(og), trans == combo2(og), trans == combo3(og))):
    transformation = 5
elif trans == og:
    transformation = 6

with open("transform.out", 'w') as fout:
    fout.write(str(transformation) + "\n")
