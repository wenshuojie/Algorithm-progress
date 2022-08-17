# 验证二叉搜索树

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, None, None)

    def helper(self, root, min, max):
        if not root:
            return True

        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False
        return self.helper(root.left, min, root) and self.helper(root.right, root, max)