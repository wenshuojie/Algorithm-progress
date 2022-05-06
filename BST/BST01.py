# 230. 二叉搜索树中第K小的元素

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.times = 0
        self.traverse(root, k)
        return self.res
    
    def traverse(self, root, k):
        if not root:
            return

        self.traverse(root.left, k)
        self.times += 1
        if self.times == k:
            self.res = root.val
            return
        self.traverse(root.right, k)