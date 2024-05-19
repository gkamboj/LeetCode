# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow, fast = head, head.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
    
'''
Approach: Using EAFP (Easier to ask for forgiveness than permission): take slow and fast pointers starting from head. If they, ever meet before fast reaching end, cycle exists. If there's any exception (which will come when fast is None), return False.
Reference: https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python

Read Floyd cycle detection algorithm for more detail.
'''

