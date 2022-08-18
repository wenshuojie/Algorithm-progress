# 二叉搜索树构造

class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = [[0]*(n+1) for _ in range(n+1)] # 为了对齐
        return self.helper(left=1, right=n)
    
    def helper(self, left, right):
        if left > right:
            return 1
        
        if self.memo[left][right] != 0:
            return self.memo[left][right]
        
        res = 0
        for mid in range(left, right+1):
            left_count = self.helper(left, mid-1)
            right_count = self.helper(mid+1, right)
            res += left_count * right_count
        self.memo[left][right] = res

        return res
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return
        return self.build(1, n)

    def build(self, left, right):
        res = []
        if left > right:
            res.append(None)
            return res
        
        for mid in range(left, right+1):
            leftTree = self.build(left, mid-1)
            rightTree = self.build(mid+1, right)
            for leftNode in leftTree:
                for rightNode in rightTree:
                    root = TreeNode(mid)
                    root.left = leftNode
                    root.right = rightNode
                    res.append(root)
        
        return res
