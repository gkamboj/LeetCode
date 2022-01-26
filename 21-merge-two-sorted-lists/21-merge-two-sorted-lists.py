# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = dummy = ListNode(0)
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                ans.next = list1
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            ans = ans.next
        if list1 is not None:
            ans.next = list1
        elif list2 is not None:
            ans.next = list2
        return dummy.next
    
#Approach: This is iterative approach using extra variable (that is not in-place). NWe are using dummy along with ans because at the end, ans will point to a node in between but we need to return head, so dummy.next will give the actual first node of answer (first node being 0)

#See other submissions for alternative approaches.
        