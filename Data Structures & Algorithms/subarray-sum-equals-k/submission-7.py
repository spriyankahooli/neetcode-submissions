class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        currSum = 0
        count = 0
        for i, num in enumerate(nums):
            currSum+=num

            if currSum-k in seen:
                count+=seen[currSum-k]
            seen[currSum] = seen.get(currSum,0)+1
        return count 
            