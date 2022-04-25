# 316. 去除重复字母

from collections import defaultdict

def removeDuplicateLetters(s):
    stack = [] # 单调栈
    count = defaultdict(int) # 计数器，tips：defaultdict(val)，val是值的类型
    instack = defaultdict(bool)

    for char in s:
        count[char] += 1

    for char in s:
        count[char] -= 1

        if instack[char] == True:
            continue

        while stack and stack[-1] > char:
            if count[stack[-1]] == 0: # 如果后面没有这个字符就不能pop出去了，否则无法保证字符的相对顺序
                break 
        
            instack[stack.pop()] = False
            
        stack.append(char)
        instack[char] = True

    return "".join(stack) # 输出得时候就不看做是栈了，join方法：list -> char

print(removeDuplicateLetters("bcabc"))
