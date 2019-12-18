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

with open("transform.in", 'r') as fin:
    N = int(fin.readline())
    og = [list(fin.readline().rstrip()) for _ in range(N)]
    trans = [list(fin.readline().rstrip()) for _ in range(N)]
