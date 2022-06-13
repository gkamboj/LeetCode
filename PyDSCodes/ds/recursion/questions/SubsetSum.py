# Given an array, return an array of sum of subsets.

def subsetSum(arr):
    result = []
    solve(arr, result, 0, 0)
    return result


def solve(arr, result, sum, ind):
    if ind >= len(arr):
        result.append(sum)
        return
    solve(arr, result, sum + arr[ind], ind + 1)
    solve(arr, result, sum, ind + 1)


print(subsetSum([1, 2, 3]))

# Approach: Similar to subsequences with given sum - take or not take approach for every element.

# TC: O(2^n)

# Another approach is using Power Set with TC O(n * 2^n)
