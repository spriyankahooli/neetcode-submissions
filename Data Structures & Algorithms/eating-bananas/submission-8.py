class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours =0 
            for bananas in piles:
                hours+=(bananas+k-1)//k
            return hours<=h
        
        l =1 
        r= max(piles)
        while l<=r:
            m=(l+r)//2
            if check(m):
                r =m-1
            else:
                l =m+1
        return l