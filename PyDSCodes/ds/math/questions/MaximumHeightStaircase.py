# Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to
# create a staircase of max-height using these blocks. The first stair would require only one block, and the second
# stair would require two blocks, and so on. Find and return the maximum height of the staircase.

def maximumHeightStaircase(n):
    return int((-1 + (1 + 8 * n) ** 0.5) / 2)

# Approach: For a given k, number of staircase will be k * (k + 1) / 2. This can be formed into a quadratic equation
# and solved to get the answer.

# Note: This can also be solved using binary search in O(log n), but mathematical approach is O(1).
