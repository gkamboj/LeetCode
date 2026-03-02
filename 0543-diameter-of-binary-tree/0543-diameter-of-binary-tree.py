# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack, mp = [root], {None: (0, 0)}
        while stack:
            node = stack[-1]
            if (left := node.left) and left not in mp:
                stack.append(left)
            elif (right := node.right) and right not in mp:
                stack.append(right)
            else:
                node = stack.pop()
                left_ht, left_dia = mp[left]
                right_ht, right_dia = mp[right]
                mp[node] = (
                    max(left_ht, right_ht) + 1,
                    max(left_ht + right_ht, left_dia, right_dia)
                )
        return mp[root][1]

'''
Approach: Perform a post-order traversal. For each node, store the node’s height and its best diameter in a map. After both children have been processed,
compute the height as `1 + max(left subtree height, right subtree height)` and the diameter as `max(left + right subtree height, left subtree dia, right subtree dia)`.
Because each node is processed only after its children and is visited exactly once (using map check), every node is processed exactly one time.
'''