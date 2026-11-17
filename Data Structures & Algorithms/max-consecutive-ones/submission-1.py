class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxlen = 0
        result = []
        for num in nums:
            if num==1:
                count+=1
            maxlen = max(maxlen,count)
            if num!=1:
                count=0
        return maxlen

        