# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-101, head)
        prev, curr, ans = dummy, head, dummy
        
        while curr and curr.next:
            if prev.val != curr.val and curr.val != curr.next.val:
                ans.next = curr
                ans = ans.next
            prev = curr
            curr = curr.next
        
        if prev.val != curr.val: #To handle last node separately if it's not duplicate
            ans.next = curr
        else:
            ans.next = None #Else if last node is duplicate, then set next of ans as None
        
        return dummy.next
            
#Approach: Take dummy node prior to head with val out of range from given list (here -101 as node val ranges in [-100, 100]). For every node, check if it's different from prev's val and next's val. If it is, set it as next of ans and move ans to next. After while loop, remember to check separately for last node (as while loop will break before checking last node) and set ansnext accordingly.
