# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        revHead = self.reverse(slow.next)
        while revHead:
            if head.val != revHead.val:
                return False
            head = head.next
            revHead = revHead.next
        return True
        
    def reverse(self, head):
        prev = None
        while head:
            newHead = head.next
            head.next = prev
            prev = head
            head = newHead
        return prev
    
#Approach: Reverse the list from next element of middle element. Then match each corresponding element starting from head and mid. Keep in mind boundary condition as well as while condition when finding mid (don't forget to check fast.next.next)