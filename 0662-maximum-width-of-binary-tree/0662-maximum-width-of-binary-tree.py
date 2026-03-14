# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue, ans = deque([(root, 1)]), 1
        while queue:
            ans = max(ans, queue[-1][1] - queue[0][1] + 1)
            temp = []
            while queue:
                node, num = queue.popleft()
                if left := node.left:
                    temp.append((left, 2 * num))
                if right := node.right:
                    temp.append((right, 2 * num + 1))
            queue = deque(temp)
        return ans

# Approach: Do BFS/level order traversal and store node numbering along with the node
# in queue. After every level, get the level's width from the difference of numbering
# of first and last node of level.