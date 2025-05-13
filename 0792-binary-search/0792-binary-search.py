class Solution:
    def search(self, nums: List[int], target: int) -> int:
        fst, snd = 0, len(nums) - 1
        while fst <= snd:
            mid = fst + (snd - fst) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                snd = mid - 1
            else:
                fst = mid + 1
        return -1