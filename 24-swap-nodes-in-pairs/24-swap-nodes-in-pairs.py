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
            prev.next = nextNode
            prev = curr
            curr = curr.next
        return ans
        
            