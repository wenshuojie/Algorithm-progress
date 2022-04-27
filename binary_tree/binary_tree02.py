# 543. 二叉树的直径

# 左子树和右子树最大深度之和

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxD = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.maxD

    def maxDepth(self, root):
        if not root:
            return 0

        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        self.maxD = max(self.maxD, (leftMax+rightMax))

        return max(leftMax,rightMax)+1

        

        
        