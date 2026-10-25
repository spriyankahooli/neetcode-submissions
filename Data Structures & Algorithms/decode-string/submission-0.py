class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        currString = ""
        currnum =0
        stack = []

        for char in s:
            if char.isdigit():
                currnum = currnum*10+int(char)
            elif char =='[':
                stack.append((currString,currnum))
                currString = ""
                currnum =0
            elif char == ']':
                prevString, repC = stack.pop()
                currString = prevString+currString*repC
            else:
                currString +=char
        return currString