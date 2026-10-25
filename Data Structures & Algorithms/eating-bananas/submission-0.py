class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(speed):
            total_hours = 0
            for pile in piles:
                total_hours+=math.ceil(pile/speed)
            return total_hours <=h
        lo =1
        hi = max(piles)
        while lo < hi:
            mid = lo + (hi -lo) //2
            if check(mid):
                hi = mid
            else:
                lo =mid+1
        return lo