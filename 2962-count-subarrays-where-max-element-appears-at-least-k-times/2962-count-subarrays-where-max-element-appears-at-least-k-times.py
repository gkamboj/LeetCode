class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val, count = max(nums), 0
        ans, start = 0, 0
        for ind in range(len(nums)):
            if nums[ind] == max_val:
                count += 1
                if count == 1: start = ind
            while count > k:
                start += 1
                if nums[start] == max_val:
                    count -= 1
                
            if count == k:
                print(start, ind)
                ans += start + 1
        return ans