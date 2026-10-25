
class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if stack and stack[-1] in paranthesis and char == paranthesis[stack[-1]]:
                stack.pop()
            elif char in paranthesis:
                stack.append(char)
            else:
                return False 
        return True if not stack else False