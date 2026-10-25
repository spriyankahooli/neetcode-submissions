class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map1 ={0:1}
        curSum =0
        count =0
        for num in nums:
            curSum+=num 
            if curSum -k in map1:
                count+=map1[curSum-k]
            map1[curSum] = map1.get(curSum,0)+1
        return count