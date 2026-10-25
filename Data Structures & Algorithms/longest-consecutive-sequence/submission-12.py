class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxlen = 0 
        for num in s:
            if num-1 not in s:
                length = 1
                while num+1 in s:
                    length+=1
                    num = num+1
                maxlen = max(length,maxlen)
        return maxlen