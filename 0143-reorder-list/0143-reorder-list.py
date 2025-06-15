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
        slow, fast, prev = head, head.next, None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        n1, n2 = head, self.reverseList(slow.next)
        slow.next = None
        while n2:
            curr = n2
            temp1, temp2 = n1.next, n2.next
            n1.next = n2
            n2.next = temp1
            n1, n2 = temp1, temp2


    def reverseList(self, head):
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev