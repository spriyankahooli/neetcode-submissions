class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sets = set(nums)
        maxlen = 0
        length = 0
        for num in sets:
            if num-1 not in sets:
                length = 1
                while num+1 in sets:
                    length+=1
                    num+=1
            maxlen = max(maxlen,length)
        return maxlen
