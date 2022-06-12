# Given an array, find any subsequence with the given sum (if it exists), else return empty list.

def findSubsequenceRecursively1(arr, sum):
    ans = []
    if solve1(arr, sum, [], ans, 0):
        return ans[0]
    return []


def solve1(arr, target, seq, ans, ind):
    if ind >= len(arr):
        if target == 0:
            ans.append(seq)
            return True
        return False

    if solve1(arr, target - arr[ind], seq + [arr[ind]], ans, ind + 1):
        return True
    if solve1(arr, target, seq, ans, ind + 1):
        return True
    return False


def findSubsequenceRecursively2(arr, sum):
    ans = []
    if solve2(arr, sum, [], ans):
        return ans[0]
    return []


def solve2(arr, target, seq, ans):
    if target == sum(seq):
        ans.append(seq)
        return True
    for i in range(len(arr)):
        if solve2(arr[i + 1:], target, seq + [arr[i]], ans):
            return True
    return False


print(findSubsequenceRecursively1([5, 12, 3, 17, 1, 18, 15, 3, 17], 18))
print(findSubsequenceRecursively2([5, 12, 3, 17, 1, 18, 15, 3, 17], 18))


# Approach: This is similar to finding all subsequences with the given sum, with the difference on the point that we
# just need only one instance. So, we can avoid all future recursion calls whenever we encounter any valid
# subsequence. To avoid such calls, functional method is written which returns boolean (unlike the void method in all
# subsequences problem).

# Note-1: Refer https://youtu.be/eQCS_v3bw0Q (from 11:40 to 18:10) for more detail
# Note-2: Refer TUF Recursion playlist L-7 notes for theory
