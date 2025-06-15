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
        if not head.next:
            return
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        mid = self.reverseList(prev.next)
        prev.next = None
        n1, n2 = head, mid
        while n1 and n2:
            curr = n1
            temp1 = n1.next
            temp2 = n2.next
            n1.next = n2
            n2.next = temp1
            n2 = temp2
            n1 = temp1
        if n2:
            curr.next.next = n2
        # print("n1 is " + str(n1))
        # print("n2 is " + str(n2))
        # print("temp1 is " + str(temp1))
        # print("temp2 is " + str(temp2))
        # print("curr is " + str(curr))
        # print("head is " + str(head))



    def reverseList(self, head):
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev