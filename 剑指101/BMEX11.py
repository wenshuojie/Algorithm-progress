# 二叉搜索树中第K小的元素
# (利用BST中序遍历的特性：正常中序遍历就是升序)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    tag = 0
    res = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverse(root, k)
        return self.res
    def traverse(self, root, k):
        if not root:
            return
        
        self.kthSmallest(root.left, k)
        self.tag += 1
        if self.tag == k:
            self.res = root.val
        self.kthSmallest(root.right, k)
        