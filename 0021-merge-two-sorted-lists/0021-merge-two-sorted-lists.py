# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ans_prev = ListNode()
        curr.next = list1
        while list1 and list2:
            if list1.val <= list2.val:
                list1 = list1.next
            else:
                nxt = curr.next
                curr.next = list2
                temp = list2.next
                list2.next = nxt
                list2 = temp
            curr = curr.next
        curr.next = list1 or list2
        return ans_prev.next