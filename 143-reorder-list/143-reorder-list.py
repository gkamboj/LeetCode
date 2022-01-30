# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start, slow, fast = head, head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        midHead = self.reverse(slow.next)
        slow.next = midHead
        while start != slow:
            currStartNext = start.next
            currMidHeadNext = midHead.next
            start.next = midHead
            midHead.next = currStartNext
            start = currStartNext
            midHead = currMidHeadNext
        start.next = midHead
        
    def reverse(self, head):
        prev = None
        while head:
            newHead = head.next
            head.next = prev
            prev = head
            head = newHead
        return prev
            
#Approach: Reverse the linked list from mid. Now, we just need to map alternate nodes from first half with alternate nodes from second half (i.e. reverse half)
