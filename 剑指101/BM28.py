# 二叉树的最大深度

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: # 遍历
    max_depth, depth = 0, 0

    def maxDepth(self , root: TreeNode) -> int:
        self.traverse(root)
        return self.max_depth

    def traverse(self, node):
        # base case
        if not node:
            return
        
        self.depth += 1
        if not node.left and not node.right:
            self.max_depth = max(self.depth, self.max_depth)
        self.traverse(node.left)
        self.traverse(node.right)
        self.depth -= 1

class Solution: # 递归
    def maxDepth(self , root: TreeNode) -> int:
        if not root:
            return 0
        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)
        return max(max_left, max_right) + 1
