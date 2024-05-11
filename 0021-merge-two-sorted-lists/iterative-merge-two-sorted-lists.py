# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list2 if list2 else list1
        return dummy.next
    
'''
Approach: This is iterative approach (not in-place). Use dummy along with ans because at the end, ans will point to a node in between 
but we need to return head, so dummy.next will give the actual first node of answer (first node being 0)
'''

# See other submissions for alternative approaches.
        
