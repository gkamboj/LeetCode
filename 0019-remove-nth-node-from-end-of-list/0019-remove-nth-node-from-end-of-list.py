# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp, count = ListNode(), 1
        temp.next = head
        curr = head
        while count < n:
            curr = curr.next
            count += 1
        back = temp
        while curr.next:
            back = back.next
            curr = curr.next
        back.next = back.next.next
        return temp.next
        