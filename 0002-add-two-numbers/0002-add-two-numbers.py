# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result, carry = ListNode(), 0
        curr = result
        
        while l1 and l2:
            tot = l1.val + l2.val + carry
            curr.next = ListNode(tot % 10)
            carry = tot // 10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        rem = l1 or l2
        while rem:
            tot = rem.val + carry
            curr.next = ListNode(tot % 10)
            carry = tot // 10
            curr = curr.next
            rem = rem.next
        
        if carry:
            curr.next = ListNode(carry)

        return result.next