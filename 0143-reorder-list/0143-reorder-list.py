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
        n1, n2 = head, self.reverseList(slow)
        while n1 and n2:
            curr = n2
            temp1 = n1.next
            temp2 = n2.next
            n1.next = n2
            n2.next = temp1
            n2 = temp2
            n1 = temp1
        curr.next = n2


    def reverseList(self, head):
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev