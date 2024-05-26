# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue, ans, reverse = [root], [], 1
        while queue:
            curr_level_nodes = queue
            queue = []
            for node in curr_level_nodes:
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append([node.val for node in curr_level_nodes[::reverse]])
            reverse *= -1
        return ans

'''
Approach: For every iteration of for loop, loop over the whole queue and push children of every queue element to queue. This ensures that,
for every iteration, queue always contains all the nodes at current level. Push nodes to ans with order depending on level.
'''
