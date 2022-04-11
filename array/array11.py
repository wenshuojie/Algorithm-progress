# 438. 找到字符串中所有字母异位词
# 找到 s 中所有 p 的 异位词 的子串

from collections import defaultdict


def findAnagrams(s: str, p: str):
    window, need = defaultdict(int),defaultdict(int)
    left,right = 0,0
    valid = 0
    index = []

    # 构造need map
    for p_str in p:
        need[p_str] += 1
    
    while right < len(s):
        s_str = s[right]
        right += 1
        if s_str in need:
            window[s_str] += 1
            if window[s_str] == need[s_str]:
                valid += 1
        
        while right-left == len(p):
            if valid == len(need):
                index.append(left)

            s_str = s[left]
            left += 1
            if s_str in need:
                if window[s_str] == need[s_str]:
                    valid -= 1
                window[s_str] -= 1

    return index

print(findAnagrams("cbaebabacd","abc"))