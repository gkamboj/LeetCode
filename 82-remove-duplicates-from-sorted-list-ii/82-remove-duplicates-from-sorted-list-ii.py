# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-101, head)
        prev, curr = dummy, head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
            else:
                prev.next = curr.next
            curr = curr.next
            
        return dummy.next
            