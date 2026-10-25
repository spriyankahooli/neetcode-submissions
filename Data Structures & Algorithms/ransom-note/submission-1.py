class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {}
        if len(magazine) <= 0:
            return False 
        seen = Counter(magazine)
        for c in ransomNote:
            if seen[c] <=0:
                return False 
            seen[c]-=1
        return True
