# 226. 翻转二叉树
# 让每个节点的左右孩子交换

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 遍历的思想
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root

    def traverse(self, node):
        if not node:
            return

        node.left, node.right = node.right, node.left
        self.traverse(node.left)
        self.traverse(node.right)

    # 递归的思想
    def invertTree_v2(self, root):
        if not root:
            return None

        # 先翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        # 然后交换左右子节点
        root.left = right
        root.right = left

        return root
