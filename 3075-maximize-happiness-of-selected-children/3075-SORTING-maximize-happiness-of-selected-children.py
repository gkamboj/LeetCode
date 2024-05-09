class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        happiness.sort(reverse=True)
        for ind in range(k):
            ans += max(happiness[ind] - ind, 0)
        return ans
    
'''
Approach: Sort the array and take top-k elements along with adjusting the given conditions.
'''
