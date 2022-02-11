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
            
#Approach: Take dummy node prior to head with val out of range from given list (here -101 as node val ranges in [-100, 100]). Keep iterating till curr.val == curr.next.val. After this, if prev.next == curr, this means there is not duplicate => move prev to next, else current is duplicate => set next of prev as curr.next.