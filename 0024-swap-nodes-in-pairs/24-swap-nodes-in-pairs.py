# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr, ans = ListNode(0), head, head.next
        while curr and curr.next:
            nextNode = curr.next
            curr.next = nextNode.next
            nextNode.next = curr
            prev.next = nextNode #Setting next of tail from previous iteration
            prev = curr #Updating prev value for next iteration
            curr = curr.next
        return ans
        
#Approach: Save 2nd node initially as that will be the final head node. Now, swap every pair and keep saving the first value so as to use it as prev in next iteration.

#Explore for iterative approach.