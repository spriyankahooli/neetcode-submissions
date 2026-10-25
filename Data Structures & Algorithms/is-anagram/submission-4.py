class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False 
        map1={}
        for a in s:
            map1[a]=map1.get(a,0)+1
        for b in t:
            if b not in map1:
                return False 
            map1[b]-=1

            if map1[b] < 0:
                return False 
        return True