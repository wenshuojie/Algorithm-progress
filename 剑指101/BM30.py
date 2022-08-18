# 二叉搜索树与双向链表

class Solution:
    head, pre = None, None
    def Convert(self , pRootOfTree ):
        if not pRootOfTree:
            return
        
        self.Convert(pRootOfTree.left)
        # 找到最小值（双向链表的头节点）
        if not self.pre:
            self.head = pRootOfTree
            self.pre = pRootOfTree
        else:
            self.pre.right = pRootOfTree
            pRootOfTree.left = self.pre
            self.pre = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.head