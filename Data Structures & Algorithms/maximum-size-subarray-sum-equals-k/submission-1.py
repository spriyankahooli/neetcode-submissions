class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_indices = {0: -1}
        curr_sum = 0
        max_len = 0
        
        for i, num in enumerate(nums):
            curr_sum += num
            if curr_sum - k in prefix_indices:
                max_len = max(max_len, i - prefix_indices[curr_sum - k])
            if curr_sum not in prefix_indices:
                prefix_indices[curr_sum] = i
                
        return max_len