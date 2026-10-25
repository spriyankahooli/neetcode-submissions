class Solution:
    def isValid(self, s: str) -> bool:
        map1 = {'(':')', '[':']','{':'}'}
        stack = []
        for c in s:
            if c in map1:
                stack.append(c)
            else:
                if stack and map1[stack[-1]]==c:
                    stack.pop()
                else:
                    return False
    
        return not stack
