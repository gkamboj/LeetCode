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
            val = -101
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    val = node.val
                    queue.append(node.left)
                    queue.append(node.right)
            if val != -101: result.append(val)
        return result
                    #[1,2,3,4,5,6,7,8,null,null,9,10,null,null,null,null,null,null,null,11,12]