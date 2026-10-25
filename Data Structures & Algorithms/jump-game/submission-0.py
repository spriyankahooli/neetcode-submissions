class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False 
        maxreach =0
        for i, num in enumerate(nums):
            if i>maxreach:
                return False
            maxreach = max(maxreach,i+num )
            if maxreach >= len(nums)-1:
                return True 
        return True
        