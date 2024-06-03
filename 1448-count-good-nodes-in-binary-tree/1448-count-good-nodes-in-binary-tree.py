# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans, queue = 0, deque([(root, root.val)])
        while queue:
            for _ in range(len(queue)):
                node, maxInPath = queue.popleft()
                if node.val >= maxInPath: ans += 1
                if node.left:
                    queue.append((node.left, max(node.val, maxInPath)))
                if node.right:
                    queue.append((node.right, max(node.val, maxInPath)))
        return ans
    
'''
Approach: Iterative - using BFS level order template. Store the maxTillNow along with the node in queue, and check if current node is good node in 
every iteration.
'''