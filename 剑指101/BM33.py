# 二叉树的镜像

from logging import root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: # 遍历
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        self.traverse(pRoot)
        return pRoot

    def traverse(self, node):
        if not node:
            return
        
        self.traverse(node.left)
        self.traverse(node.right)
        node.left, node.right = node.right, node.left

class Solution: # 递归
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # func定义：将以 root 为根的这棵二叉树翻转，返回翻转后的二叉树的根节点
        if not pRoot:
            return
        
        left = self.Mirror(pRoot.left)
        right = self.Mirror(pRoot.right)
        pRoot.left, pRoot.right = right, left
        return pRoot
