class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        res= [1]*n
        prefix =1
        suffix =1 
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
        for j in range(n-1,-1,-1):
            res[j]*=suffix
            suffix*=nums[j]
        return res