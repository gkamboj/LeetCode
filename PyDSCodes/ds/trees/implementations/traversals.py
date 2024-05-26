from PyDSCodes.ds.trees.implementations.TreeNode import TreeNode


def pre_order(root_node):
    stack, ans = [root_node], []
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ans


def post_order(root_node):
    stack, ans = [], []
    curr = root_node
    while curr or stack:
        if curr:
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            if stack and curr.right == stack[-1]:
                stack.pop()
                stack.append(curr)
                curr = curr.right
            else:
                ans.append(curr.val)
                curr = None
    return ans


def in_order(root_node):
    stack, ans = [], []
    curr = root_node
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
    return ans


def level_order(root_node):
    queue, ans = [root_node], []
    while queue:
        node = queue.pop(0)
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ans


'''
Tree with below level order traversal (with null nodes) is input. Check ./resources/example_1.png for visualisation of input tree.
[1,2,3,4,5,6,7,8,null,null,9,10,null,null,null,null,null,null,null,11,12]
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.right.right = TreeNode(9)
root.right.left.left = TreeNode(10)
root.right.left.left.left = TreeNode(11)
root.right.left.left.right = TreeNode(12)

print(f'Level order traversal: {level_order(root)}')
print(f'Inorder traversal: {in_order(root)}')
print(f'Pre-order traversal: {pre_order(root)}')
print(f'Post-order traversal: {post_order(root)}')
