# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack, ans = [(0, root)], []
        while stack:
            level, curr = stack.pop()
            if curr:
                stack.append((level + 1, curr.right))
                stack.append((level + 1, curr.left))
                if len(ans) < level + 1:
                    ans.append([curr.val])
                else:
                    ans[level].append(curr.val)
        return ans

