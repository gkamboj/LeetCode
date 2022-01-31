# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        startA, startB = headA, headB
        sizeA, sizeB = 0, 0
        while startA:
            sizeA += 1
            startA = startA.next
        while startB:
            sizeB += 1
            startB = startB.next
        if startA != startB:
            return None
        if sizeA > sizeB:
            headA = self.iterateNnodes(headA, sizeA - sizeB)
        elif sizeB > sizeA:
            headB = self.iterateNnodes(headB, sizeB - sizeA)
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
        
    def iterateNnodes(self, head, n):
        while n > 0:
            n -= 1
            head = head.next
        return head
    
#Approach: Traverse over both nodes till last node. If last nodes are not same, then there is no intersection. If they are same, traverse the list with higher size x times where x = abs(size1 - size2). Once this traversal is done, traverse both nodes simultaneously till there is intersection.

#See other submission for approach without calculating length difference.