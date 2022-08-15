#%% 1. 两数之和
from ast import Num
from cmath import inf
from collections import defaultdict
from platform import node
from turtle import pen
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num], i] # 前面几个不会出现，所以target-num必定在前面
            
            hashmap[num] = i

        return []


#%% 2. 两数相加
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_p, l2_p = l1, l2
        dumpy = ListNode()
        l3_p = dumpy
        
        self.remain = 0
        while l1_p and l2_p:
            sum = l1_p.val + l2_p.val + self.remain
            self.remain = 0
            if sum >= 10:
                sum = sum - 10
                self.remain = 1

            l3_p.next = ListNode(sum)
            l1_p = l1_p.next
            l2_p = l2_p.next
            l3_p = l3_p.next

        while l1_p:
            sum = l1_p.val + self.remain
            self.remain = 0
            if sum >= 10:
                sum = sum - 10
                self.remain = 1
            
            l3_p.next = ListNode(sum)
            l1_p = l1_p.next
            l3_p = l3_p.next

        while l2_p:
            sum = l2_p.val + self.remain
            self.remain = 0
            if sum >= 10:
                sum = sum - 10
                self.remain = 1
            
            l3_p.next = ListNode(sum)
            l2_p = l2_p.next
            l3_p = l3_p.next

        if self.remain == 1:
            l3_p.next = ListNode[1]

        return dumpy.next

#%% 3. 无重复字符的最长子串
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        window = defaultdict(int)
        max_len = 0

        while right < len(s):
            char = s[right]
            window[char] += 1
            right += 1

            while window[char] > 1:
                # max_len = max(max_len,right-left-1)
                window[s[left]] -= 1
                left += 1
            
            max_len = max(max_len,right-left)

        return max_len

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring(" "))

# %%
from collections import deque

a = deque()
print(a)

from queue import Queue
b = Queue()
print(b)
# %%
a = [1,2,3]

b = [x for x in a]

a[0] = 2
print(b)
# %%
a = [1,2,3,4]
def change(a):
    a[0], a[3] = a[3], a[0]

change(a)
print(a)

# %%
def partition(nums, l, r):
    pivot = nums[l]
    i, j = l+1, r
    while i <= j:
        while i < r and nums[i] <= pivot:
            i += 1
        while j > l and nums[j] > pivot:
            j -= 1

        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        
    nums[l], nums[j] = nums[j], nums[l]

a = [5 ,9 ,1 ,6 ,8 ,14 ,6 ,49 ,25 ,4 ,6 ,3]
partition(a, 0, len(a)-1)
print(a)
# %%
from collections import deque

a = deque([])
print(a[0])
# %%
import math

print(math.inf>0)
# %%
envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
print(envelopes)
# %%
a = 'a'
print(ord(a))
# %%
from queue import PriorityQueue

test_queue = PriorityQueue()
test_queue.put((5,0))
test_queue.put((1,1))
print(test_queue.get())
# %%
for i in range(5, 3, -1):
    print(i)
# %%
a = [1,2,3]
a.extend([2,3,4])
print(a)
# %%
from queue import Queue

q = Queue()
q.put([2,3,4])
print(q)

# %%
from queue import Queue

q = Queue()
q.put(1)
q.put(2)
print(q.get())
# %%
from collections import deque
node_list = deque()
node_list.append(1)
node_list.appendleft(2)
print(node_list.pop())

# %%
a = 'a,b,c'
b = a.split(',')
print(b.pop(1))
print(b)
# %%
