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
        
        collisionPoint, loopSize = slow, 1
        while collisionPoint.next != slow:
            collisionPoint = collisionPoint.next
            loopSize += 1
        
        slow, fast = head, head
        while loopSize > 0:
            fast = fast.next
            loopSize -= 1
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
            