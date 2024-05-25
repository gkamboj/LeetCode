# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        node, count, start, dummy = head, 1, head, ListNode()
        prev = dummy
        while node:
            if not count % k:
                nxt = node.next
                self.reverse(prev, start, nxt)
                prev = start
                start = nxt
            else:
                nxt = node.next
            node = nxt
            count += 1
        return dummy.next
                
    def reverse(self, bef, node, end):
        prev = end
        while node != end:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        if bef: bef.next = prev
        return prev
    
'''
Approach: Reverse lists k at a time, but pass prev and end from main method to mainatain the continuity.
Use dummy node for answer to avoid handling edge cases.
'''
