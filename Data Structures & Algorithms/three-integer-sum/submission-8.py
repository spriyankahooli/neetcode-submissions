class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res =[]
        nums.sort()
        for i,a in enumerate(nums):
            if a> 0:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue
            l =i+1
            r = len(nums)-1

            while l<r:
                tsum = nums[l]+nums[r]+a
                if tsum ==0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                elif tsum>0:
                    r-=1
                else:
                    l+=1
        return res 

        