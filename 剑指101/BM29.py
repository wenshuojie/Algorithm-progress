# 二叉树中和为某一值的路径(一)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and sum-root.val == 0:
            return True
        return self.hasPathSum(root.left, sum-root.val) or \
                self.hasPathSum(root.right, sum-root.val)