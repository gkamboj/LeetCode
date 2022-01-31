# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        currA, currB = headA, headB
        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        return currA
    
#Approach: Go over explanation in https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len

#See other submission for the approach with calculating length difference