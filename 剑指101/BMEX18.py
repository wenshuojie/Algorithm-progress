# 完全二叉树的节点个数

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: # O(logN*logN)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l, r = root, root
        hl, hr = 0, 0

        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        
        if hl == hr:
            return 2^(hl)-1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            # 这两个递归只有一个会真的递归下去，另一个一定会触发 hl == hr 而立即返回，不会递归下去
            # 因为一棵完全二叉树的两棵子树，至少有一棵是满二叉树