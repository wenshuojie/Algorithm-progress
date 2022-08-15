

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return 
        return self.build_pre_in(preorder, 0, len(preorder)-1, \
                            inorder, 0, len(inorder)-1)

    # 从前序与中序遍历序列构造二叉树
    def build_pre_in(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        # base case
        if preStart > preEnd:
            return
        
        root_val = preorder[preStart]
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)

        left_size = inorder_index - inStart
        root.left = self.build_pre_in(preorder, preStart+1, preStart+left_size, inorder, inStart, inorder_index-1)
        root.right = self.build_pre_in(preorder, preStart+left_size+1, preEnd, inorder, inorder_index+1, inEnd)
        return root
    
    # 从中序与后序遍历序列构造二叉树
    def build_in_post(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        # base case
        if inStart  > inEnd:
            return
        
        root_val = postorder[postEnd]
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)

        left_size = inorder_index - inStart
        root.left = self.build_in_post(inorder, inStart, inorder_index-1, postorder, postStart, postStart+left_size-1)
        root.right = self.build_in_post(inorder, inorder_index+1, inEnd, postorder, postStart+left_size, postEnd-1)
        return root
        
class Solution_v2:
    # 从前序与中序遍历序列构造二叉树
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        ind = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:ind+1], inorder[:ind])
        root.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
        return root
    
    # 从中序与后序遍历序列构造二叉树
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
            
        root_val = postorder[-1]
        root = TreeNode(root_val)
        ind = inorder.index(root_val)
            
        root.left = self.buildTree(inorder[:ind], postorder[:ind])
        root.right = self.buildTree(inorder[ind+1:], postorder[ind:len(postorder)-1])
        return root

    # 根据前序和后序遍历构造二叉树
    class Solution:
        def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            if not preorder:
                return

            root = TreeNode(preorder[0])
            if len(preorder) == 1:
                return root
            
            leftsize = postorder.index(preorder[1])+1
            root.left = self.constructFromPrePost(preorder[1:1+leftsize],postorder[:leftsize])
            root.right = self.constructFromPrePost(preorder[1+leftsize:],postorder[leftsize:len(postorder)-1])
            return root



