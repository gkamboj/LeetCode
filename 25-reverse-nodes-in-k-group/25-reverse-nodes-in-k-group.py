# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head or not head.next:
            return head
        curr, count, ans = head, 0, None
        while curr:
            count += 1
            if count == k:
                ans = curr
            curr = curr.next
        passes = count // k
        while head and passes > 0:
            head = self.reverseLinkedList(head, k)
            passes -= 1
        return ans
    
    def reverseLinkedList(self, head, k):
        prev, tail, chunkSize = None, head, k #Tail for current chunk after reversing will be head before reversing
        while k > 0:
            newHead = head.next
            head.next = prev
            prev = head
            head = newHead
            k -= 1
        tailNext = head #Curret value of head corresponds to next chunk's first node
        while chunkSize > 1 and tailNext: #Check till we have reached kth node from new tail
            tailNext = tailNext.next
            chunkSize -= 1
        if chunkSize == 1 and tailNext: #If next chunk is possible, set kth node as next of tail
            tail.next = tailNext
        else:
            tail.next = head #If next chunk is not possible, set next node as tail.next
        return head
       
#Approach: Reverse each chunk separately and set next of new tail as next reversed list head if next chunk is possible, else next value as it is from the list.

#Note: Instead of iterating to find the ans at start, dummy node can also be used instead by returning dummy.next at end

#Explore more for recursive approach