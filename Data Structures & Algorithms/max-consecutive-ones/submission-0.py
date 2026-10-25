class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if i == len(nums) - 1 and nums[i] == 1:
                    result.append(count)
            else:
                result.append(count)
                count = 0
        return max(result)

        