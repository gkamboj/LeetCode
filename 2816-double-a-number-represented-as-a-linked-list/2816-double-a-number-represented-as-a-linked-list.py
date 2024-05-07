# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_head = self.reverseList(head)
        carry, node, prev = 0, reverse_head, None
        while node:
            val = 2 * node.val + carry
            node.val = val % 10
            carry = val // 10
            prev = node
            node = node.next
        if carry: prev.next = ListNode(carry, None)
        new_head = self.reverseList(reverse_head)
        return new_head
    
    
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev