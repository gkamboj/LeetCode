# You are given an integer A which denotes the number of people standing in the queue. A selection process follows a
# rule where people standing on even positions are selected. Of the selected people, a queue is formed, and again out
# of these, only people on even position are selected. This continues until we are left with one person. Find and
# return the position of that person in the original queue.
import math


def findingPosition(n):
    max2Power = int(math.log2(n))
    return 1 << max2Power


print(findingPosition(10))

# Approach: Observe that after any ith iteration, only multiples of 2^i are remaining:
# i = 0 => 1 2 3 4 5 6 7 8 9 10 (multiples of 2^0 = 1)
# i = 1 => 2 4 6 8 10 (multiples of 2^1 = 2)
# i = 2 => 4 8 (multiples of 2^2 = 4)
# i = 3 => 8 (multiple of 2^3 = 8)
# that is at the end, largest power of 2 lesser than n will be remaining. This reduces our problem to finding that largest power of 2.
