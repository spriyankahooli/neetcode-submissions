class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        for num in nums:
            if num-1 not in s:
                length = 1
                while num+1 in s:
                    length += 1
                    num = num+1
                count = max(count,length)
        return count