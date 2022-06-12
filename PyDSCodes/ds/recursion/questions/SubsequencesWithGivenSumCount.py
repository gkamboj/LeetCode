# Given an array, find count of all subsequences with the given sum

def findSubsequencesCount1(arr, sum):
    return solve1(arr, sum, 0)


def solve1(arr, target, ind):
    if ind >= len(arr):
        if target == 0:
            return 1
        else:
            return 0
    elif target < 0:
        return 0
    take = solve1(arr, target - arr[ind], ind + 1)
    ignore = solve1(arr, target, ind + 1)
    return take + ignore


def findSubsequencesCount2(arr, sum):
    return solve2(arr, sum, [])


def solve2(arr, target, seq):
    if sum(seq) == target:
        return 1
    elif sum(seq) > target:
        return 0
    count = 0
    for i in range(len(arr)):
        count += solve2(arr[i + 1:], target, seq + [arr[i]])
    return count


print(findSubsequencesCount1([5, 12, 3, 17, 1, 18, 15, 3, 17], 18))
print(findSubsequencesCount2([5, 12, 3, 17, 1, 18, 15, 3, 17], 18))

# Approach: This is similar to finding all subsequnces. To get just the count, change the method return type from
# void to int and return int value for every recursive call.

# Note-1: Refer TUF Recursion playlist L-7 notes for theory
