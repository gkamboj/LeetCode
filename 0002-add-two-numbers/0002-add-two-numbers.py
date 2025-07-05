# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, carry, curr1, curr2 = ListNode(0), 0, l1, l2
        temp = ans
        while curr1 and curr2:
            tot = curr1.val + curr2.val + carry
            temp.next = ListNode(tot % 10)
            carry = tot // 10
            curr1 = curr1.next
            curr2 = curr2.next
            temp = temp.next
        curr = curr1 or curr2
        while curr:
            tot = curr.val + carry
            temp.next = ListNode(tot % 10)
            carry = tot // 10
            curr = curr.next
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return ans.next

        