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
        reverse = self.reverseList(slow)
        prev.next = None
        first, second, mid = head, reverse, None
        while first and second:
            prev = second
            fn = first.next
            sn = second.next
            first.next = second
            second.next = fn
            second = sn
            first = fn
        prev.next = second
        
        return head

        
        
    
    def reverseList(self, node):
        curr, prev = node, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        