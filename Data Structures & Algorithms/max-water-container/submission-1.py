class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        l = 0
        r = len(heights)-1
        maxWater = 0
        while l<r:
            maxWater = max(maxWater, min(heights[l],heights[r])*(r-l))
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return maxWater


        