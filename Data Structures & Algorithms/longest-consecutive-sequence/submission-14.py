class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        maxlen =0
        length =0
        for num in s:
            if num-1 not in s:
                length =1 
                while num+1 in s:
                    num = num+1
                    length+=1
                maxlen = max(maxlen,length)
        return maxlen
