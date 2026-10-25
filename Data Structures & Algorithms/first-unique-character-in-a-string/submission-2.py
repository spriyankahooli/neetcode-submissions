class Solution:
    def firstUniqChar(self, s: str) -> int:
        map1 = {}
        for char in s:
           map1[char] = map1.get(char,0)+1
        for i,char in enumerate(s):
            if map1[char] ==1:
                return i
        return -1
        