class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen ={0:1}
        count =0
        currSum =0
        for num in nums:
            currSum+=num
            if currSum-k in seen:
                count+=seen[currSum-k]
            seen[currSum] = seen.get(currSum,0)+1
        return count