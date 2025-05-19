# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ans_prev = ListNode()
        n1, n2 = list1, list2
        while n1 and n2:
            if n1.val <= n2.val:
                curr.next = n1
                n1 = n1.next
            else:
                curr.next = n2
                n2 = n2.next
            curr = curr.next
        while n1:
            curr.next = n1
            curr = curr.next
            n1 = n1.next
        while n2:
            curr.next = n2
            curr = curr.next
            n2 = n2.next
        return ans_prev.next