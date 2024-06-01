class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums2[j] < nums1[i]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
    
'''
Approach: Take pointers from the end of expected length of both arrays (i.e. m-1 and n-1) and another point 
from actual length of nums1 (m + n - 1) to store the numberss in empty spaces. Apply the merge sort algo and
handle the case if first nums1 index gets over first (if while loop is on nums2 index) .
'''
