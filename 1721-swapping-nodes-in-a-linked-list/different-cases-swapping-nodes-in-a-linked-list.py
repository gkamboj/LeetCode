# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        curr, count, isHeadCase = head, 1, False
        if k == 1:
            kthNodePrev = None
            while curr.next.next:
                curr = curr.next
            kthFromEndPrev = curr
            isHeadCase = True
        else:
            while count < (k - 1):
                curr = curr.next
                count += 1
            if not curr.next.next:
                kthNodePrev = curr
                kthFromEndPrev = None
                isHeadCase = True
            else:
                kthNodePrev, kthFromEndPrev = curr, head
                curr = curr.next
                while curr.next.next:
                    curr = curr.next
                    kthFromEndPrev = kthFromEndPrev.next
        
        if kthNodePrev == kthFromEndPrev:
            return head
        
        if kthNodePrev and kthNodePrev.next == kthFromEndPrev:
            head = self.swapAdjacentNodes(head, kthNodePrev, kthNodePrev.next, kthFromEndPrev.next)
        elif kthFromEndPrev and kthFromEndPrev.next == kthNodePrev:
            head = self.swapAdjacentNodes(head, kthFromEndPrev, kthFromEndPrev.next, kthNodePrev.next)
        elif isHeadCase:
            if not kthNodePrev:
                head = self.swapHeadAndNode(head, kthFromEndPrev)
            else:
                head = self.swapHeadAndNode(head, kthNodePrev)
        else:
            self.swapNonAdjacentNodes(kthFromEndPrev, kthNodePrev)
        return head
            
    def swapAdjacentNodes(self, head, prev, node1, node2):
        if prev:
            prev.next = node2
        else:
            head = node2
        node1.next = node2.next
        node2.next = node1
        return head
    
    def swapHeadAndNode(self, head, nodePrev):
        if head == nodePrev:
            tail = head.next
            tail.next = head
            head.next = None
            newHead = tail
        else:
            currHeadNext = head.next
            head.next = None
            newHead = nodePrev.next
            nodePrev.next = head
            newHead.next = currHeadNext
        return newHead
    
    def swapNonAdjacentNodes(self, node1Prev, node2Prev):
        node1 = node1Prev.next
        node2 = node2Prev.next
        currNode1Next = node1.next
        node2Prev.next = node1
        node1.next = node2.next
        node2.next = currNode1Next
        node1Prev.next = node2
        
#Approach: Find kth node from start and end. To find these in a single pass, use two pointer approach (as used in Q-19) Handle scenarios like adjacent nodes, non-adjacent nodes, head node, etc. Remember to handle all cornr cases like ([1], 1), ([1,2], 1), etc.

#Explore other approaches like using dummy node before head (https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained)
