from queue import Queue

class Solution:
    def solve(self , xianxu: List[int], zhongxu: List[int]) -> List[int]:
        root = self.reConstructBinaryTree(xianxu, zhongxu)
        return self.rightViewer(root)

    def reConstructBinaryTree(self , pre: List[int], vin: List[int]) -> TreeNode:
        if not pre:
            return
        
        root_val= pre[0]
        ind = vin.index(root_val)
        root = TreeNode(root_val)

        root.left = self.reConstructBinaryTree(pre[1:ind+1], vin[:ind])
        root.right = self.reConstructBinaryTree(pre[ind+1:], vin[ind+1:])
        return root

    def rightViewer(self, root):
        res = []
        node_list = Queue()
        node_list.put(root)

        while not node_list.empty():
            node_len = node_list.qsize()
            while node_len > 0:
                node = node_list.get()
                if node.left:
                    node_list.put(node.left)
                if node.right:
                    node_list.put(node.right)
                if node_len == 1:
                    res.append(node.val)
        return res
