"""
ID: sudarsh11
LANG: PYTHON3
TASK: beads
"""
def beads_right(necklace):
    count = 1
    prev = len(necklace) - 1
    for i in range(len(necklace) - 2, -1, -1):
        if necklace[i] == necklace[prev] or necklace[prev] == 'w':
            count += 1
            prev -= 1
        else:
            break
    return count

def beads_left(necklace):
    count = 1
    prev = 0
    for i in range(1, len(necklace)):
        if necklace[i] == necklace[prev] or necklace[prev] == 'w':
            count += 1
            prev += 1
        else:
            break
    return count

def beads_collected(cut, necklace):
    if cut == 0:
        print(cut, necklace)
        return beads_right(necklace) + beads_left(necklace)
    else:
        cut_necklace = necklace[cut:] + necklace[:cut]
        print(cut, cut_necklace)
        return beads_right(cut_necklace) + beads_left(cut_necklace)

with open("beads.in", "r") as fin:
    N = int(fin.readline())
    necklace = fin.readline().rstrip()
max_beads = 0
for i in range(N):
    collected = beads_collected(i, necklace)
    print(i, collected)
    if collected > max_beads:
        max_beads = collected
print(max_beads)
