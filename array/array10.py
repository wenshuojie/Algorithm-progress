# 567. 字符串的排列（s2是否包含s1的排列）

from collections import defaultdict


def checkInclusion(s1: str, s2: str) -> bool:
    need,window = defaultdict(int),defaultdict(int)
    left,right = 0,0
    valid = 0

    # 初始化need map
    for s1_str in s1:
        need[s1_str] += 1
    
    while right < len(s2):
        s2_str = s2[right]
        right += 1
        if s2_str in need:
            window[s2_str] += 1
            if window[s2_str] == need[s2_str]:
                valid += 1
        
        # 窗口收缩
        while right-left == len(s1):
            if  valid == len(need):
                return True
            
            s2_str = s2[left]
            left += 1
            if s2_str in need:
                if window[s2_str] == need[s2_str]:
                    valid -= 1
                window[s2_str] -= 1
    
    return False

print(checkInclusion('ab','eidboaoo'))
print(checkInclusion('ab','eidbaooo'))               
