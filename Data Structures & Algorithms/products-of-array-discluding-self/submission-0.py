class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count, product = 0,1
        res = [0]*len(nums)
        for num in nums:
            if num:
                product = product*num 
            else:
                zero_count+=1
            
        if zero_count > 1:
            return res
        if zero_count == 1:
            for i, num in enumerate(nums):
                if num == 0:
                    res[i] = product
        else: 
            for i,num in enumerate(nums):
                res[i] = product//num
        return res
        