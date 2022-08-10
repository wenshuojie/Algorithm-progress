# 二叉树的直径
from typing import Optional

from bcrypt import re

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        self.traverse(root)
        return self.max_d

    def traverse(self, node):
        if not node:
            return 0
        
        max_left = self.traverse(node.left)
        max_right = self.traverse(node.right)
        self.max_d = max(self.max_d, (max_left+max_right))
        return max(max_left, max_right) + 1

