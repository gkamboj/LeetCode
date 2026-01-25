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
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        n1, n2 = head, self.reverseList(slow.next)
        slow.next = None

        while n1 and n2:
            n1nxt = n1.next
            n2nxt = n2.next
            n1.next = n2
            n2.next = n1nxt
            n1 = n1nxt
            n2 = n2nxt
    
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev