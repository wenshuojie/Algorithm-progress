# 104. 二叉树的最大深度

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.res = 0
        self.depth = 0
# method 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    # 二叉树遍历
    def traverse(self, root):
        if not root:
            self.res = max(self.res, self.depth) # 叶子节点，更新最大深度
            return

        self.depth += 1 # 前序位置，进入节点的时间点，所以深度加1
        self.traverse(root.left)
        self.traverse(root.right)
        self.depth -= 1 # 后序位置，离开节点的时间点，所以深度减1

# method 2：分解问题的思路
    def maxDepth_v2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # 将问题分解为：寻找左右子树最大深度
        leftMax = self.maxDepth_v2(root.left)
        rightMax = self.maxDepth_v2(root.right)
        res = max(leftMax, rightMax) + 1 # 再加上自己

        return res
