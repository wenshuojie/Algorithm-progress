# 3. 无重复字符的最长子串

# from collections import defaultdict

# def lengthOfLongestSubstring(s: str) -> int:
#     window = defaultdict(int)
#     left,right = 0,0
#     maxlength = 0

#     while right < len(s):
#         s_str = s[right]
#         right += 1
#         window[s_str] += 1
        
#         # 某一个字母在window中出现的次数大于1了，就要收缩窗口了
#         while window[s_str] > 1:
#             s_str = s[left]
#             left += 1
#             window[s_str] -= 1

#         maxlength = max(maxlength,right-left)
        
#     return maxlength


def lengthOfLongestSubstring(s: str) -> int:
    window = set()
    right,max_len = -1,0

    for i in range(len(s)):
        if i != 0:
            window.remove(s[i-1])
        
        while right+1 < len(s) and s[right+1] not in window:
            window.add(s[right+1])
            right += 1

        max_len = max(max_len,right-i+1)

    return max_len

print(lengthOfLongestSubstring("pwwkew")) # 3
print(lengthOfLongestSubstring("abcabcbb")) # 3
