# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = dummy = ListNode(0)
        while l1 and l2:
            val = carry + l1.val + l2.val
            carry = val // 10
            ans.next = ListNode(val % 10)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        rem = l1 or l2
        while rem:
            val = carry + rem.val
            ans.next = ListNode(val % 10)
            carry = val // 10
            rem = rem.next
            ans = ans.next
        if carry: ans.next = ListNode(carry)
        return dummy.next

'''
Approach: Traverse over both list till they are not null, and remaining list after that. Handle carry at every step.
'''