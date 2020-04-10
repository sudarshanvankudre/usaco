"""
ID: sudarsh11
LANG: PYTHON3
TASK: barn1
"""
from itertools import *
from collections import *
from heapq import *


class Board:
    def __init__(self, start, stop, blocked_stalls):
        self.start = start
        self.stop = stop
        self.blocked_stalls = blocked_stalls
        self.longest_start, self.longest_stop, self.empty_length = self.greatest_empty_section()
        self.total_blocked = stop - start + 1

    def split(self):
        """
        :return: a pair of boards, one from the left side of the empty section and another from the right side
        """
        return Board(self.start, self.longest_start - 1, self.blocked_stalls), Board(self.longest_stop + 1, self.stop, self.blocked_stalls)

    def greatest_empty_section(self):
        """
        Method to calculate the greatest empty section of this board.
        :return: A triple (start, stop, length), inclusive, that is the longest empty section of this board as well as the length of that section
        """
        longest_start = -1
        longest_stop = -1
        max_empty_length = 0
        start_stall = self.start
        while start_stall < self.stop + 1:
            if start_stall in self.blocked_stalls:
                start_stall += 1
            else:
                count = 0
                curr_stall = start_stall
                while curr_stall < self.stop + 1 and curr_stall not in self.blocked_stalls:
                    count += 1
                    curr_stall += 1
                if count > max_empty_length:
                    longest_start = start_stall
                    longest_stop = curr_stall - 1
                    max_empty_length = count
                start_stall = curr_stall
        return longest_start, longest_stop, max_empty_length

    def __eq__(self, other):
        return other.empty_length == self.empty_length

    def __lt__(self, other):
        return self.empty_length > other.empty_length


def solve():
    M, S, C = map(int, fin.readline().split())
    blocked_stalls = set()
    lowest_blocked_stall = S
    highest_blocked_stall = 1
    for line in map(str.rstrip, fin):
        stall_num = int(line)
        lowest_blocked_stall = min(lowest_blocked_stall, stall_num)
        highest_blocked_stall = max(highest_blocked_stall, stall_num)
        blocked_stalls.add(stall_num)
    greedy = {}
    board_situation = [Board(lowest_blocked_stall, highest_blocked_stall, blocked_stalls)]
    for stall_num in range(1, M + 1):
        if stall_num == 1:
            greedy[stall_num] = board_situation[0].total_blocked
        else:
            board = heappop(board_situation)
            left, right = board.split()
            heappush(board_situation, left)
            heappush(board_situation, right)
            greedy[stall_num] = greedy[stall_num - 1] - board.empty_length
    return greedy[M]


with open('barn1.in', 'r') as fin:
    ans = solve()

with open('barn1.out', 'w') as fout:
    fout.write(str(ans) + "\n")
