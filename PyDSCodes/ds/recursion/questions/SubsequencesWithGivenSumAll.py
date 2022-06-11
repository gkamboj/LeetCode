# Given an array, find all the subsequences with the given sum.

def findSubsequencesRecursively1(arr, sum):
    ans = []
    solve1(arr, ans, [], sum, 0)
    return ans


def solve1(arr, ans, seq, target, ind):
    if ind >= len(arr):
        if target == 0:
            ans.append(seq)
        return
    if target < 0:
        return
    solve1(arr, ans, seq + [arr[ind]], target - arr[ind], ind + 1)
    solve1(arr, ans, seq, target, ind + 1)


def findSubsequencesRecursively2(arr, sum):
    ans = []
    solve2(arr, sum, [], ans)
    return ans


def solve2(arr, target, seq, ans):
    if sum(seq) == target:
        ans.append(seq)
    for i in range(len(arr)):
        solve2(arr[i + 1:], target, seq + [arr[i]], ans)


print(findSubsequencesRecursively1([5, 12, 3, 17, 1, 18, 15, 3, 17], 18))
print(findSubsequencesRecursively2([5, 12, 3, 17, 1, 18, 15, 3, 17], 18))


# Approach: Both approaches are similar to LC-78 Subset problem submissions with the sum check being the only added
# condition.
