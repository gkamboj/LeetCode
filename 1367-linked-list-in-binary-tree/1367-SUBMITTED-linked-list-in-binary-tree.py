# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        return self.helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def helper(self, head, root):
        if not head:
            return True
        if not root or head.val != root.val:
            return False
        return self.helper(head.next, root.left) or self.helper(head.next, root.right)

'''
Approach: For every node, check the entire path as well as recursively call isSubPath for left as well as right nodes.
To check the entire path, keep going downward till current node values matches with LL node.
If the LL node ever becomes None, it means LL is finished and hence, sub path is present.
'''
	
