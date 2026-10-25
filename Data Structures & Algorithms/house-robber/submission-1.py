class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) ==1:
            return nums[0]
       
        dp2 =nums[0]
        dp1 = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            curr = max(dp1, nums[i] +dp2)
            dp2=dp1
            dp1= curr

        return dp1

        
        