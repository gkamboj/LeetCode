class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        
        ans = curr = sum(cardPoints[:k])
        i, j = k - 1, len(cardPoints) - 1
        while i >= 0:
            curr -= cardPoints[i]
            i -= 1
            curr += cardPoints[j]
            j -= 1
            ans = max(ans, curr)
        
        return ans

'''
Approach: Start with a window of size k of the first k elements. Keep shrinking it and adding an element from end.
Update ans wherever applicable.
'''
