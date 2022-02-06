# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small, large = ListNode(0), ListNode(0)
        smallHead, largeHead = small, large
        curr = head
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next
            curr = curr.next
        small.next = largeHead.next
        large.next = None
        return smallHead.next
    
#Approach: Take two pointers for storing heads of two linked lists head: one with elements smaller than x and other with larger than or equal to x. Intialise heads with dummy node and keep updating next according to value of current node. Here note that no extra memory is being used, only next pointers are being changed.