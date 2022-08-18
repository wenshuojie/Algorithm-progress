from queue import Queue

class Solution:
    def isCompleteTree(self , root: TreeNode) -> bool:
        if not root:
            return True
        
        node_list = Queue()
        flag = False # 标记第一个出现的None
        node_list.put(root)

        while not node_list.empty():
            len_node = node_list.qsize()
            for _ in range(len_node):
                cur = node_list.get()
                if not cur:
                    flag = True
                else:
                    if flag:
                        return False
                    node_list.put(cur.left)
                    node_list.put(cur.right)
        return True


        