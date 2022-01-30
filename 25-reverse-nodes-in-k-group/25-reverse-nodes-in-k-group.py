# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        curr, count, ans = head, 0, None
        while curr:
            count += 1
            if count == k:
                ans = curr
            curr = curr.next
        passes = count // k
        while head and passes > 0:
            head = self.reverseLinkedList(head, k, head)
            passes -= 1
        return ans
    
    def reverseLinkedList(self, head, k, tail):
        prev, tail, num = None, head, k
        while k > 0:
            newHead = head.next
            head.next = prev
            prev = head
            head = newHead
            k -= 1
        curr = head
        while num > 1 and curr:
            curr = curr.next
            num -= 1
        if num == 1 and curr:
            tail.next = curr
        else:
            tail.next = head
        return head
       