class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = zero = 0
        two = len(nums) - 1
        while curr <= two:
            if not nums[curr]:
                nums[curr], nums[zero] = nums[zero], nums[curr]
                zero += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[two] = nums[two], nums[curr]
                two -= 1

'''
Approach: Dutch National Flag Algorithm

- Use three pointers: zero (next position for 0), curr (current index), and two (next position for 2).
- Traverse the array while curr <= two, maintaining partitions for 0s, 1s, and 2s.
- If nums[curr] == 0, swap with nums[zero] and increment both zero and curr.
- If nums[curr] == 1, just increment curr.
- If nums[curr] == 2, swap with nums[two] and decrement two without incrementing curr.

- Time Complexity: O(n), Space Complexity: O(1)

PS: We can also initialise curr as len(nums) - 1, change while condition to `curr >= zero` and add `curr -= 1` to last else (after removing `curr += ` to first if),
algo will work same.
'''