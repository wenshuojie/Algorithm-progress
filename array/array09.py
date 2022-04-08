# 76. 最小覆盖子串

from cmath import inf
from collections import defaultdict

def minWindow(s: str, t: str) -> str:
    need,window = defaultdict(int),defaultdict(int) # 需要满足的条件，窗口目前的条件
    left,right = 0,0 # 记录窗口的两端（左闭右开）
    valid = 0 # 记录窗口中满足条件数（valid == len(need)）
    
    start,length = 0,inf # 记录最小覆盖子串的起始索引及长度

    for tchar in t:
        need[tchar] += 1

    while right < len(s):
        # 右移窗口
        c = s[right]
        right += 1 

        # 进行窗口内数据的一系列更新
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        # 判断左侧窗口是否要收缩
        while valid == len(need):
            # 更新最小子串
            if right-left < length:
                start = left
                length = right-left
            
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return "" if length == inf else s[start:start+length]

print(minWindow("ADOBECODEBANC","ABC"))