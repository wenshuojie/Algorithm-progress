# 层序遍历二叉树

from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_traverse(root):
    tree_queue = deque()

    tree_queue.append(root)
    while tree_queue:
        node = tree_queue.popleft()
        print(node.val)

        if node.left:
            tree_queue.append(node.left)
        if node.right:
            tree_queue.append(node.right)

p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p5 = TreeNode(5)

p1.left = p2
p1.right = p3
p3.left = p4
p3.right = p5

level_traverse(p1)