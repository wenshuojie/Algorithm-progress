# 114. 二叉树展开为链表

from turtle import left, right
from matplotlib.cbook import flatten


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        # 根据函数的定义，反转左右子树
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.right = left
        root.left = None

        p = root
        while p.right:
            p = p.right
        
        p.right = right

