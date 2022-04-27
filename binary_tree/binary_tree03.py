# 144. 二叉树的前序遍历

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.preTraverse = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.preTraverse

    def traverse(self,node):
        if not node:
            return

        self.preTraverse.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)