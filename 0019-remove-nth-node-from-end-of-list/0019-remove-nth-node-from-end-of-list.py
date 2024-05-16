# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count, nth, rev_nth = 0, head, head
        while count < n:
            nth = nth.next
            count += 1
        if not nth:
            return head.next
        while nth.next:
            nth = nth.next
            rev_nth = rev_nth.next
        rev_nth.next = rev_nth.next.next
        return head
    
'''
Approach: Find nth node and iterate again from start till nth node becomes None.
'''