# 把二叉搜索树转换为累加树
# (利用BST中序遍历的特性：先遍历right就是降序)

from typing import Optional

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    sum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, root):
        if not root:
            return
        
        self.traverse(root.right)
        self.sum = self.sum + root.val
        root.val = self.sum
        self.traverse(root.left)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3

solution = Solution()
print(solution.convertBST(node1).val)
print(solution.convertBST(node1).left.val)
print(solution.convertBST(node1).right.val)