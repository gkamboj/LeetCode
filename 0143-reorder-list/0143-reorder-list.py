# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None            
        mid, start, prev = self.reverseList(slow), head, None
        while start and mid:
            prev = mid
            start_next, mid_next = start.next, mid.next
            start.next = mid
            mid.next = start_next
            start, mid = start_next, mid_next
        prev.next = mid
        
        
    
    def reverseList(self, node):
        curr, prev = node, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        