class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        minLen = float('inf')
        currSum  =0

        for right in range(len(nums)):
            currSum+=nums[right]

            while currSum >= target:
                minLen = min(minLen, (right-left)+1)
                currSum -=nums[left]
                left+=1
        return minLen  if minLen != float("inf") else 0
            