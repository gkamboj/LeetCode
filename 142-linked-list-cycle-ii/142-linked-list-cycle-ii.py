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
    
#Approach: Use fast and slow pointers to check for existence of loop (see other submission for explanation). If loop exists, find the size of cycle by looping over the cycle taking collision point as start. Let this size of cycle be c. Now, start with two pointers: p1 at head and p2 at c distance from head. Keep moving them at same speed of one step at a time, they will meet at starting point of cycle. This is because p2 will cover the extra distance of c (by the time p1 reaches at starting point of cycle) and hence both will meet.
            