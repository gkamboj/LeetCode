# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        count, curr = 1, head 
        while count < n:
            curr = curr.next
            count += 1
        nthNode = head
        if curr.next:
            while curr.next.next:
                curr = curr.next
                nthNode = nthNode.next
            nthNode.next = nthNode.next.next
        else:
            head = head.next
        return head
        
#Approach: First step is to find the nth (or previous node to nth) node from end. To find it in single pass, take 2 pointers: at start and at nth node from start. When 2nd pointer reaches end, first pointer will be at nth node from end. Using this approach, get (n-1)th node from end and set its next to next of node to be removed.