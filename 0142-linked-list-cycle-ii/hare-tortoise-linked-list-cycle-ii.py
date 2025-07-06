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
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
            
#Approach:
# A. To check if loop exists: Take start and fast pointers. If they both ever meet after starting from head, then there is a loop.
# This works because:
#   Say, loop size is c and currently slow is at loop entry point & fast is at some point k from entry point i.e. distance between
#   both pointers is k. From this point, every iterative movement of slow and fast will inrease their distance by 1. Both pointers
#   will continue to move till distance increases from k to c. Once this distance is k, it's equivalent to zero distance (because
#   we are in loop) and hence there is a meeting between both pointers. This proves both pointers will always meet if there is a loop.

# B. To find the entry/beginning point of loop, move one pointer from the collision point (found above) to head and keep moving both
# pointers (from head and collision point) by a single distance They will meet at entry point. This works because:
#   Refer Beginning_point_of_cycle_in_linked_list.py

# Check https://www.youtube.com/watch?v=-YiQZi3mLq0 & https://stackoverflow.com/a/6110767 for more detail on this approach

# See other submission for alternative approach.
