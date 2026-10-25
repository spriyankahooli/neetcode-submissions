class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i,num in enumerate(nums):
            temp = target -num
            if temp in map1:
                return [map1[temp],i]
            map1[num]= i
        return[-1,-1]
        