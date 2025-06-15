class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n = len(s1)
        arr1, arr2 = [0]*26, [0]*26
        for ind in range(n):
            arr1[ord(s1[ind]) - ord('a')] += 1
            arr2[ord(s2[ind]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if arr1[i] == arr2[i] else 0)

        for i in range(n, len(s2)):
            if matches == 26:
                return True
            
            ind1 = ord(s2[i]) - ord('a')
            arr2[ind1] += 1
            if arr2[ind1] - arr1[ind1] == 1:
                matches -= 1
            elif arr2[ind1] == arr1[ind1]:
                matches += 1
            
            ind2 = ord(s2[i-n]) - ord('a')
            arr2[ind2] -= 1
            if arr1[ind2] - arr2[ind2] == 1:
                matches -= 1
            elif arr2[ind2] == arr1[ind2]:
                matches += 1
    
        return matches == 26


# Approach: Similar to other submitted approach (https://github.com/gkamboj/LeetCode/blob/main/0567-permutation-in-string/0567-SUBMITTED_UNOPTIMISED-permutation-in-string.py),
# with optimisation being the reduction of time for equality check of array as it has been replaced with
# with the number of matches between both the arrays. Whenever total matches are 26 for a window, that's
# the window we require.
