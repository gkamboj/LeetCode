# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = self.reverseList(slow)
        while mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        return True
    
    def reverseList(self, node):
        curr, prev = node, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
#Approach: Reverse the list from next element of middle element. Then match each corresponding element starting from head and mid.
# Observe the use of mid in line-13 while condition instead of head because first half may have one more node in case of even number of nodes.
