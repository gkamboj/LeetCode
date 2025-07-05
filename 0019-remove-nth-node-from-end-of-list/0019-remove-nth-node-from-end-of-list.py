# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count, nth = 1, head
        while count < n:
            count += 1
            nth = nth.next
        if not nth.next:
            return head.next
        curr, prev = head, None
        while nth.next:
            nth = nth.next
            prev = curr
            curr = curr.next
        prev.next = prev.next.next
        return head
        