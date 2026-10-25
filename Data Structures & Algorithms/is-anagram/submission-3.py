class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False 
        map1 = [0]*26
        for i in range(len(s)):
            map1[ord(s[i])- ord('a')] +=1
            map1[ord(t[i])- ord('a')] -=1
        for val in map1:
            if val!=0:
                return False 
        return True 
