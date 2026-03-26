# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_indices = {val: ind for ind, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):  # left/right are inorder boundaries
            if left <= right:
                root_val = preorder[self.pre_idx]
                self.pre_idx += 1
                root = TreeNode(root_val)
                ind = in_indices[root_val]
                root.left = helper(left, ind - 1)
                root.right = helper(ind + 1, right)
                return root
            return None

        return helper(0, len(inorder) - 1)

'''
Approach: Store all indices of inorder to avoid finding index at runtime for every call.
Create a helper function to define left and right recursively using left and right bounds. Note that
these bounds are just for inorder. For preorder, we just need root index which can be tracked separately.
Check below bversion if keeping pre_idx at class level is confusing:

def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    in_indices = {val: ind for ind, val in enumerate(inorder)}

    def helper(pre_idx, in_left, in_right):
        if in_left > in_right:
            return None, pre_idx
        
        root_val = preorder[pre_idx]
        root = TreeNode(root_val)
        ind = in_indices[root_val]
        
        root.left, pre_idx = helper(pre_idx + 1, in_left, ind - 1)
        root.right, pre_idx = helper(pre_idx, ind + 1, in_right)
        
        return root, pre_idx

    node, _ = helper(0, 0, len(inorder) - 1)
    return node
'''
