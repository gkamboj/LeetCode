import heapq as h

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = max(stones)
        freq = [0 for i in range(n + 1)]
        for stone in stones:
            freq[stone] += 1
        ans, left, right = n, n, n
        while right:
            if not freq[right] % 2:
                right -= 1
                continue
            left = min(right - 1, left)
            while left and not freq[left]:
                left -= 1
            if not left:
                return right
            freq[right - left] += 1
            freq[left] -= 1
            right = max(right - left, left)
        return right

# Approach: Bucket sort, which uses the given information that the maximum weight of stones is a small constant (30),
# so we can create an array to store the frequency for every weight. We can then start from the right end and keep canceling
# weights as we move towards the left.
# Note that, at any moment, `right` represents the largest weight and we need to consider it only if the frequency is odd, as even
# frequency will cancel itself.
