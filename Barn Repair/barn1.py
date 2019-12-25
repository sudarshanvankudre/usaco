"""
ID: sudarsh11
LANG: PYTHON3
TASK: barn1
"""
with open("barn1.in", "r") as fin:
    M, S, C = map(int, fin.readline().rstrip().split())
# realization: the more 'granular' the number of boards, the less wasted space.
# realization: we must use all of the available boards
# conclusion: we have to find the least wasteful partition of the stalls using
# the max number of boards possible
