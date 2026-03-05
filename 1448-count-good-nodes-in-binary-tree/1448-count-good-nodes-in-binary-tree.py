# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack, count = [(root, root.val)], 1
        while stack:
            curr, max_val = stack.pop()
            count += self.processNode(curr.left, stack, max_val)
            count += self.processNode(curr.right, stack, max_val)
        return count

    def processNode(self, node, stack, max_val):
        if node:
            curr_max = max(node.val, max_val)
            stack.append((node, curr_max))
            if node.val >= curr_max:
                return 1
        return 0
