class Solution:
    def isValid(self, s: str) -> bool:
        map1  = {')':'(','}':'{',']':'['}
        stack  = []
        for char in s:
            if char in map1:
                if stack and map1[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        
        