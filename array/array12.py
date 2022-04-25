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
