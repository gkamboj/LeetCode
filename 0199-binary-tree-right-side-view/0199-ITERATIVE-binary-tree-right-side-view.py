# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result, queue = [], deque([root])
        while queue:
            rightMost = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    rightMost = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightMost: result.append(rightMost.val)
        return result

'''
Approach: Iterative - Level order template. Add the rightmost node value to result instead of every node at a level. Note that we have taken variable
(rightMost) for node insetad of value as taking value will fail the case at line 18 if node.val = 0.
'''
