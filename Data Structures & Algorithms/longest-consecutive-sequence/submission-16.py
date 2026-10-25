class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxlen = 0
        numset = set(nums)
        length =0
        for num in numset:
            if num-1 not in numset:
                length =1
                while num+1 in numset:
                    length+=1
                    num+=1
            maxlen = max(length,maxlen)
        return maxlen
