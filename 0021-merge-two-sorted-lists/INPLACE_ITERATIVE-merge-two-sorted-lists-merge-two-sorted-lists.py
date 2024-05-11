# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        node.next = list1
        while list1 and list2:
            if list1.val < list2.val:
                list1 = list1.next
            else:
                nxt = node.next
                temp = list2.next
                node.next = list2
                list2.next = nxt
                list2 = temp
            node = node.next
        node.next = list1 or list2
        return dummy.next
    
'''
Approch: In-place iterative solution. Refer other solutions for more approaches.
'''
