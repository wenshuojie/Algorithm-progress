# 20. 有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if stack and self.turn(c) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack

    def turn(self,s):
        if s == ')':
            return '('
        elif s == ']':
            return '['
        else:
            return '{'

solution = Solution()
print(solution.isValid(']'))