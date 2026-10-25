class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map1 ={0:1}
        curr_sum = 0
        count =0
        for num in nums:
            curr_sum+=num
            if curr_sum-k in map1:
                count += map1[curr_sum-k]
            map1[curr_sum] = map1.get(curr_sum,0)+1
        return count