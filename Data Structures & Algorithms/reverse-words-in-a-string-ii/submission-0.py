class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        left = right = 0
        while right < len(s):
            while right < len(s) and s[right] != " ":
                right += 1
            
            start, end = left, right - 1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            
            left = right + 1
            right = left