# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack, heights = [root], defaultdict(int)
        while stack:
            curr = stack[-1]
            if (left := curr.left) and left not in heights:
                stack.append(left)
            elif (right := curr.right) and right not in heights:
                stack.append(right)
            else:
                curr = stack.pop()
                left_ht, right_ht = heights[left], heights[right]
                if abs(left_ht - right_ht) > 1:
                    return False
                heights[curr] = max(left_ht, right_ht) + 1
        return True

'''
Approach: Do post-order traversal and store the height for every node. At any point, if diff between the left and right height
for any node is greater than 1, return False.
'''
