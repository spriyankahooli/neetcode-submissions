class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        seen = {}
        for i,num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num], i]
            seen[num]=i
        return [-1,-1]