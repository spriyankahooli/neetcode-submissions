class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        result =[]
        for i,a in enumerate(nums):
            if a>0:
                break
            if i>0 and nums[i-1] ==nums[i]:
                continue 
            l=i+1
            r = len(nums)-1
            while l<r:
                tsum = a+nums[l]+nums[r]
                if tsum==0:
                    result.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                elif tsum > 0:
                    r-=1
                else:

                    l+=1

        return result