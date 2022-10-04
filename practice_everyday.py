from typing import List

# 链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 二叉树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2022-09-16
class Solution: # 反转链表
    def ReverseList(self, head: ListNode) -> ListNode:
        pre, curr = None, head

        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        
        return pre

class Sort: # 各种排序
    pass

class Solution: # 实现二叉树先序，中序和后序遍历
    def threeOrders(self, root: TreeNode) -> List[List[int]]:
        self.res = [[], [], []]
        self.Orders(root)
        return self.res

    def Orders(self, root):
        if not root:
            return

        self.res[0].append(root.val)
        self.threeOrders(root.left)
        self.res[1].append(root.val)
        self.threeOrders(root.right)
        self.res[2].append(root.val)

# 2022-09-17
class Solution: # 最小的K个数
    def GetLeastNumbers_Solution(self , input: List[int], k: int) -> List[int]:
        left, right = 0, len(input)-1

        while left <= right:
            p = self.partition(input, left, right)
            if p < k-1:
                left = p+1
            elif p > k-1:
                right = p-1
            else:
                return input[:p+1]            

        return []

    def partition(self, nums, left, right):
        pivot = left

        i, j = pivot+1, right
        while i <= j:
            while i < right and nums[i] <= nums[pivot]:
                i += 1
            while j > left and nums[j] > nums[pivot]:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[pivot], nums[j] = nums[j], nums[pivot]
        return j

solution = Solution()
print(solution.GetLeastNumbers_Solution([0,1,2,1,2],3))
print(solution.GetLeastNumbers_Solution([4,5,1,6,2,7,2,8], 2))

class Solution: # 求二叉树的层序遍历
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [] # Queue()
        ass_list = []

        ass_list.append(root)
        while ass_list:
            row = []
            row_len = len(ass_list)
            for _ in range(row_len):
                node = ass_list.pop(0)
                row.append(node.val)
                if node.left:
                    ass_list.append(node.left)
                if node.right:
                    ass_list.append(node.right)
            res.append(row)
        return res

# 2022-09-18
class Solution: # 寻找第K大
    def findKth(self , a: List[int], n: int, K: int) -> int:
        k = n - K
        left, right = 0, n-1
        while left <= right:
            p = self.partition(a, left, right)
            if p > k:
                right = p-1
            elif p < k:
                left = p+1
            else:
                return a[p]
        return -1
    
    def partition(self, a, left, right):
        i, j = left+1, right

        while i <= j:
            while i < right and a[i] <= a[left]:
                i += 1
            while j > left and a[j] > a[left]:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        
        a[left], a[j] = a[j], a[left]
        return j

class Solution: # 两数之和
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from collections import defaultdict

        ass_hash = defaultdict(int)
        for i, num in enumerate(numbers):
            temp = target-num
            if temp in ass_hash:
                return [ass_hash[temp], i+1]
            
            ass_hash[num] = i+1
        
        return [-1, -1]

solution = Solution()
print(solution.twoSum([0,4,3,1], 7))

# 2022-09-24
class Solution: # 最小覆盖子串
    def minWindow(self , S: str, T: str) -> str:
        from collections import defaultdict
        import math
        
        need = defaultdict(int)
        win = defaultdict(int)
        valid = 0
        for t in T:
            need[t] += 1
        
        left, right = 0, 0
        start, length = 0, math.inf
        while right < len(S):
            # 扩大窗口
            s = S[right]
            right += 1
            if s in need:
                win[s] += 1
                if win[s] == need[s]:
                    valid += 1
            
            # 缩小窗口
            while valid == len(need):
                # 更新结果
                if right-left < length:
                    start = left
                    length = right - left
                s = S[left]
                left += 1
                if s in need:
                    if win[s] == need[s]:
                        valid -= 1
                    win[s] -= 1
        return S[start:start+length] if length != math.inf else ""

