# 二叉搜索树中的搜索，插入，删除

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 在一棵普通的二叉树中寻找
    def search(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == val:
            return root
        left = self.search(root.left, val)
        right = self.search(root.right, val)
        return left if left else right
    
    # 在一棵BST中寻找
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)
        return root

    # BST插入
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root

    # BST删除
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val == key:
            # case1: 没有左右孩子（叶子节点); case2: 只有一个孩子。一并处理（让孩子代替自己）
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # case3: 有两个孩子，找左子树中的最大值或者右子树的最小值代替自己
            min_node = self.getMin(root.right) # 找右子树中的最小值
            root.right = self.deleteNode(root.right, min_node.val) # 删除右子树的最小节点
            min_node.left = root.left
            min_node.right = root.right
            root = min_node
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
    
    def getMin(self, node):
        while node.left:
            node = node.left
        return node