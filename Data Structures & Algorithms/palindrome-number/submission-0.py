class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        og = x
        rev =0
        while x >0:
            dg = x%10
            rev = rev*10+dg
            x =x//10
        if og!=rev:
            return False 
        return True 


        