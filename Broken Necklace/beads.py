"""
ID: sudarsh11
LANG: PYTHON3
TASK: beads
"""
def is_uniform(necklace):
    """
    >>> is_uniform('bbbbbb')
    True
    >>> is_uniform('bbbwwbw')
    True
    >>> is_uniform('bbbrbbb')
    False
    """
    color = None
    for b in necklace:
        if not color and b != 'w':
            color = b
        elif b != color and b != 'w':
            return False
    return True

def count(necklace):
    """
    >>> count('bwbrbbr')
    3
    >>> count('bbbrrr')
    3
    >>> count('wwwrwb')
    5
    >>> count('rrwwwwbb')
    6
    """
    beads = 0
    color = None
    stop_index = -1
    for i, b in enumerate(necklace):
        if not color and b != 'w':
            color = b
        elif b != color and b != 'w':
            stop_index = i
            break
        beads += 1
    return beads, stop_index

with open("beads.in", 'r') as fin:
    N = int(fin.readline())
    necklace = fin.readline().rstrip()

max_beads = 0
if is_uniform(necklace):
    print("necklace is uniform")
    max_beads = N
else:
    for i in range(N):
        new_necklace = necklace[i:] + necklace[:i]
        beads1, stop_index = count(new_necklace)
        stop_index = N - stop_index
        new_necklace = new_necklace[::-1][:stop_index]
        beads2 = 0
        color = None
        for b in new_necklace:
            if not color and b != 'w':
                color = b
            elif b != color and b != 'w':
                break
            beads2 += 1
        beads = beads1 + beads2
        max_beads = max(max_beads, beads)
with open("beads.out", 'w') as fout:
    fout.write(str(max_beads) + "\n")
