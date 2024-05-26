# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue, ans, level = [(root, 0)], [], 0
        curr_level_nodes = []
        while queue:
            node, curr_level = queue.pop(0)
            if curr_level == level:
                curr_level_nodes.append(node.val)
            else:
                ans.append(curr_level_nodes[::-1] if level % 2 else curr_level_nodes)
                curr_level_nodes = [node.val]
                level = curr_level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        ans.append(curr_level_nodes[::-1] if level % 2 else curr_level_nodes)
        return ans