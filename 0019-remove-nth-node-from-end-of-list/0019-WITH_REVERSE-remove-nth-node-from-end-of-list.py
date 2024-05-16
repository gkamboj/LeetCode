# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        lnt = 0
        node = prev_head = self.reverse(head)
        if n == 1: return self.reverse(node.next)
        count = 1
        while count < n-1:
            count += 1
            node = node.next
        node.next = node.next.next
        return self.reverse(prev_head)
        
    def reverse(self, node):
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev
    
'''
Approach: Reverse the list, remove nth node and again reverse. Handle edge cases separately like n = 1
'''
