"""
ID: sudarsh11
LANG: PYTHON3
TASK: milk2
"""

class Interval:
    def __init__(self, s, e):
        assert s <= e, "The start must be <= the end"
        self.start = s
        self.end = e

    def contained_in(self, interval):
        return self.start >= interval.start and self.end <= interval.end

    def intersects_above(self, interval):
        return self.start <= interval.end

    def intersects_below(self, interval):
        return self.end >= interval.start

with open("milk2.in", 'r') as fin:
    N = int(fin.readline())
    intervals = set()
    for _ in range(N):
    	
