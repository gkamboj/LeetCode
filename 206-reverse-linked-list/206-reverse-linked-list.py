# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListRec(head, None)
    
    def reverseListRec(self, head, prev):
        if head is None:
            return prev
        newHead = head.next
        head.next = prev
        return self.reverseListRec(newHead, head)
        
#Approach: This is recursive approach.

#See other submission for iterative approach.
        
        