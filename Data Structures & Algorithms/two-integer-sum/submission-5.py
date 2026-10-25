# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         map1  = {}
#         for i, num in enumerate(nums):
#             if target-num in map1:
#                 return [map1[target-num],i]
#             map1[num] = i
#         return [-1,-1]
        


























class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result 
