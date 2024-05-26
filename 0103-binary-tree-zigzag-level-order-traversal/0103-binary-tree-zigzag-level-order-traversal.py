# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue, ans, level = [root], [], 0
        while queue:
            curr_level_nodes = queue
            queue = []
            for node in curr_level_nodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2:
                curr_level_nodes.reverse()
            ans.append([node.val for node in curr_level_nodes])
            level += 1
        return ans