# There are A pairs and therefore 2A people. Each person has a unique number ranging from 1 to 2A. An array of
# integers B shows the arrangement of these 2A people. A matrix C of size A x 2 is given describing pairs i.e. people
# that are partner of each other. C[i][0] and C[i][1] are partner of each other. Find the minimum number of swaps
# required to arrange these pairs such that all pairs become adjacent to each other.

# Input Format:
# The first argument given is the integer array B.
# The second argument given is matrix C.

def minSwapsToArrangePairs(people, pairs):
    return solve(people, pairs, 0)


def solve(people, pairs, ind):
    if ind >= len(people):
        return 0
    if people[ind + 1] == findPair(pairs, people[ind]):
        return solve(people, pairs, ind + 2)

    indPair = findPair(pairs, people[ind])
    indPairIndex = people.index(indPair)
    people[ind + 1], people[indPairIndex] = indPair, people[ind + 1]
    swaps1 = 1 + solve(people, pairs, ind + 2)
    people[ind + 1], people[indPairIndex] = people[indPairIndex], indPair

    indNextPair = findPair(pairs, people[ind + 1])
    indNextPairIndex = people.index(indNextPair)
    people[ind], people[indNextPairIndex] = indNextPair, people[ind]
    swaps2 = 1 + solve(people, pairs, ind + 2)
    people[ind], people[indNextPairIndex] = people[indNextPairIndex], indNextPair

    return min(swaps1, swaps2)


def findPair(pairs, person):
    for pair in pairs:
        if person in pair:
            return pair[0] if person == pair[1] else pair[1]


print(minSwapsToArrangePairs([3, 5, 6, 4, 1, 2], [[1, 3], [2, 6], [4, 5]]))

# Approach: Start from the beginning and recur for the remaining elements.
# If first and second elements are pair, then simply recur for remaining n-1 pairs and return the value returned by
# recursive call.
# If first and second are NOT pair, then there are two ways to arrange. Try both of them return the minimum of two:
# a) Swap second with pair of first and recur for n-1 elements. Let the value returned by recursive call be x1.
# b) Revert the changes made by previous step.
# c) Swap first with pair of second and recur for n-1 elements. Let the value returned by recursive call be x2.
# d) Revert the changes made by previous step before returning control to parent call.
# e) Return 1 + min(x1, x2)

# Note: LC-765 (https://leetcode.com/problems/couples-holding-hands/) is similar to this, but gives TLE on above
# recursive solution. Explore optimised solution for LC problem.
