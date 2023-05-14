# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr is not None:
            newHead = curr.next
            curr.next = prev
            prev = curr
            curr = newHead
        return prev
    
#Approach: This is iterative approach.

#See other submission for recursive approach.
        
        
