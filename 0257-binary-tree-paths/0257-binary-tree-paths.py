# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        queue, ans = deque([[root]]), []
        
        while queue:
            temp = deque()
            while queue:
                path = queue.popleft()
                last = path[-1]
                if not last.left and not last.right:
                    ans.append(path)
                else:
                    if last.left:
                        temp.append(path + [last.left])
                    if last.right:
                        temp.append(path + [last.right])
            queue = temp
        
        return ['->'.join([str(node.val) for node in path]) for path in ans]