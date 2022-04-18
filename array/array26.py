# 380. O(1) 时间插入、删除和获取随机元素

from collections import defaultdict
from random import random
from typing import List

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.hashmap = defaultdict(int) # 原来储存元素和对应索引

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        
        self.hashmap[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False

        def_index = self.hashmap[val]
        last_val = self.nums[-1]

        self.nums[self.hashmap[val]],self.nums[-1] = self.nums[-1],self.nums[self.hashmap[val]]
        self.hashmap[last_val] = def_index

        del self.hashmap[val]
        self.nums.pop()

        return True
        
    def getRandom(self) -> int:
        return random.choice(self.nums) # choice(): 返回list中的随机值