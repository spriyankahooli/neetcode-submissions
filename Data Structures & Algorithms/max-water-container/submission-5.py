class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        if not heights:
            return maxWater
        left = 0 
        right = len(heights)-1
        while left<right:
            area = min(heights[left],heights[right])*(right-left)
            maxWater = max(maxWater, area)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return maxWater 

        
