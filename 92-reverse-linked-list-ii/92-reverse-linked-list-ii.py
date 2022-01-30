# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy, pos = ListNode(0,head), 0
        curr = dummy
        while pos < right:
            if pos == (left - 1):
                leftPrev = curr
            curr = curr.next
            pos += 1
        rightNode = curr
        reversePartHead = self.reverse(leftPrev.next, right - left, rightNode.next)
        leftPrev.next = reversePartHead
        return dummy.next
        
    def reverse(self, head, count, prev):
        while count >= 0:
            newHead = head.next
            head.next = prev
            prev = head
            head = newHead
            count -= 1
        return prev
        