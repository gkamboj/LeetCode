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
        node_dict = defaultdict(lambda:Node(0))
        node_dict[None], curr = None, head
        while curr:
            node = node_dict[curr]
            node.val = curr.val
            node.next = node_dict[curr.next]
            node.random = node_dict[curr.random]
            curr = curr.next
        return node_dict[head]
    
    
'''
Approach: Create a dictionary with given linkedlist's nodes as key. Iterate over the given list, and for every
node as key, update the val, next and random for value corresponding to key. By  the end of while loop, every
node in dictionary would be updated with corrrect values. Return value from map corresponding to head as key.
'''

'''
Another approach: Without using dictionary, update the given original list such that for every node, insert its
copy at next position. Fetch the new list from original list in next traversal. 
Refer https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
for detail.
'''
