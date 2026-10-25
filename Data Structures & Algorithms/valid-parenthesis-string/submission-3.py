class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin, cmax = 0, 0
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin = max(cmin - 1, 0)
                cmax -= 1
            else:
                cmin = max(cmin - 1, 0)
                cmax += 1
            if cmax < 0:
                return False
        return cmin == 0