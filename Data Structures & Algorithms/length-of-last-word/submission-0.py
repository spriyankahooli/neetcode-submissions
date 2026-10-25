class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listS = s.split()
        return len(listS[-1])
        