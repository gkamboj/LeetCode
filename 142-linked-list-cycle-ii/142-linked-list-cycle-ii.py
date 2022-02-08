# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow, fast, isLoop = head, head, False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isLoop = True
                break
        if not isLoop:
            return None
        slow = head
        while slow != fast:
            print(slow.val, fast.val)
            slow = slow.next
            fast = fast.next
        return slow
            