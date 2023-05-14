"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        llDict = defaultdict(lambda: Node(0))
        llDict[None] = None
        curr = head
        while curr:
            node = llDict[curr]
            node.val = curr.val
            node.next = llDict[curr.next]
            node.random = llDict[curr.random]
            curr = curr.next
        return llDict[head]
            
#Approach: Create a dictionary to store the current data of linkedlist with default node val as 0. Iterate over the given list, and for every node, update the corresponding node in dictionary. By the end of while loop, every node in dictionary would be updated with corrrect values. Return value from map corresponding to head as key.

#Another approach: Without using dictionary, we can also update the given list such that for every need, a copy of that node is inserted as its next. Refer https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N) for detail.