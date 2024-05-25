# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        node, count, start, prev = head, 1, head, None
        ans = None
        while node:
            if not count % k:
                nxt = node.next
                temp = self.reverse(prev, start, nxt)
                if not ans: ans = temp
                prev = start
                start = nxt
            else:
                nxt = node.next
            node = nxt
            count += 1
        return ans
                
    def reverse(self, bef, node, end):
        # print(f'bef: {bef}, node: {node}, end: {end}')
        prev = end
        while node != end:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        if bef: bef.next = prev
        return prev