class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palRange(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False 
                l+=1
                r-=1
            return True

        l =0
        r =len(s)-1
        count =0
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1

            else:
                return palRange(l+1,r) or palRange(l,r-1)
        return True

        