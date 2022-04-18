# 710. 黑名单中的随机数
# 尽量不调用语言内置函数

from collections import defaultdict
from typing import List
from random import random


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.hashmap = defaultdict(int)
        self.sz = n - len(blacklist) # 合法白名单长度

        last = n - 1
        for b in blacklist:
            self.hashmap[b] = -1 # 占位，存放黑名单
        
        for b in blacklist:
            if b >= self.sz: # 不用映射
                continue
            while last in self.hashmap:
                last -= 1
            
            self.hashmap[b] = last
            last -= 1

    def pick(self) -> int:
        index = random.randint(0,self.sz-1)
        if index in self.hashmap:
            return self.hashmap[index]
        
        return index

# def temp(n,blacklist):
#     sz = n - len(blacklist)
#     mapping = defaultdict(int)
#     for b in blacklist:
#         mapping[b] = -1
    
#     last = n - 1
#     for b in blacklist:
#         if b >= sz:
#             continue
#         while last in mapping:
#             last -= 1
#         mapping[b] = last
#         last -= 1

#     return mapping

print(temp(2,[]))
