from PyDSCodes.ds.trees.implementations.TreeNode import TreeNode


# root - left - right
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


# left - right - root
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


# Similar to pre-order, but do root-right-left. Reverse the result at end to get post-order.
def post_order_2(root_node):
    stack, ans = [root_node], []
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ans[::-1]


# left - root - right
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


# LC-103
def zig_zag_traversal(root_node):
    queue, ans, level = [(root_node, 0)], [], 0
    curr_level_nodes = []
    while queue:
        node, curr_level = queue.pop(0)
        if curr_level == level:
            curr_level_nodes.append(node.val)
        else:
            ans.append(curr_level_nodes[::-1] if level % 2 else curr_level_nodes)
            curr_level_nodes = [node.val]
            level = curr_level
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    ans.append(curr_level_nodes[::-1] if level % 2 else curr_level_nodes)
    return ans


# LC-103
def zig_zag_traversal_v2(root_node):
    queue, ans, reverse = [root_node], [], 1
    while queue:
        curr_level_nodes = queue
        queue = []
        for node in curr_level_nodes:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append([node.val for node in curr_level_nodes[::reverse]])
        reverse *= -1
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
print(f'Post-order 2 traversal: {post_order_2(root)}')
print(f'Zig-zag traversal: {zig_zag_traversal(root)}')
print(f'Zig-zag traversal v2: {zig_zag_traversal_v2(root)}')

'''
Universal idea of traversing binary trees (YET TO BE CHECKED): https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45559/My-Accepted-code-with-explaination.-Does-anyone-have-a-better-idea/45086
'''
