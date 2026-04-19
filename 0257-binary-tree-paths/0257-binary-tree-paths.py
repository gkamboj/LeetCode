# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        queue, ans = deque([(root, str(root.val))]), []
        
        while queue:
            temp = deque()
            while queue:
                node, path = queue.popleft()
                if not node.left and not node.right:
                    ans.append(path)
                else:
                    if node.left:
                        temp.append((node.left, path + '->' + str(node.left.val)))
                    if node.right:
                        temp.append((node.right, path + '->' + str(node.right.val)))
            queue = temp
        
        return ans

'''
Approach: Iterative BFS
- Use a queue for BFS storing (node, path_string).
- Start with (root, str(root.val)), and for each node, append children with "->" concatenation.
- When a leaf node is reached, add its path string to the `ans`.
'''