class Solution:
    def isValid(self, s: str) -> bool:
        map1 = {'(':')','[':']','{':'}'}
        stack = []
        for char in s:
            if char in map1:
               stack.append(char)
            else: 
                if not stack or map1[stack[-1]] != char:
                    return False
                stack.pop()
        return len(stack) ==0
            
