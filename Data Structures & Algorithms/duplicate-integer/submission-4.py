class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            seen[num]= seen.get(num,0)+1
        for val in seen.values():
            if val > 1:
                return True
        return False
        