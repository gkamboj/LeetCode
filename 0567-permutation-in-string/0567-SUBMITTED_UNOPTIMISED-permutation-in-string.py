class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s1)
        arr1, arr2 = [0 for i in range(26)], [0 for i in range(26)]
        for ind in range(n):
            arr1[ord(s1[ind]) - ord('a')] += 1
            arr2[ord(s2[ind]) - ord('a')] += 1
        for i in range(n, len(s2)):
            if arr1 == arr2:
                return True
            arr2[ord(s2[i]) - ord('a')] += 1
            arr2[ord(s2[i-n]) - ord('a')] -= 1
        return arr1 == arr2

# Approach: Create 2 arrays - one each for s1 and s2 - to maintain the count of every character in
# respective strings. Initialise both for n characters [n = len(s1)]. After that, start from index n
# and keep moving the window towards the right. At every step, check if arr1 == arr2. 
# Since equality check of array takes O(k), with ke being array size (26), total complexity is O(26n).
