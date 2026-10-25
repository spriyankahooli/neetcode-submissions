class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        if not nums:
            return maxSum
        currSum =float('-inf')
        for num in nums:
            currSum = max(currSum+num, num)
            maxSum =max(maxSum,currSum)
        return maxSum
        