# 反转字符串

class Solution:
    def solve(self , str: str) -> str:
        str = list(str) # python的字符串是不可变类型
        left, right = 0, len(str)-1
        while left <= right:
            str[left], str[right] = str[right], str[left]
            left += 1
            right -= 1
        return ''.join(str) # list => str

solution = Solution()
print(solution.solve('abc'))