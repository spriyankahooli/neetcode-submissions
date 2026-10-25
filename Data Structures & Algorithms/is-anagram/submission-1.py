class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapst = [0]*26
        for i in range(len(s)):
            mapst[ord(s[i])-ord('a')] += 1
            mapst[ord(t[i])-ord('a')] -= 1
            #mapt[t[i]] = 1+mapt.get(t[i],0)
        for val in mapst:
            if val!=0:
                return False 
        return True 
        