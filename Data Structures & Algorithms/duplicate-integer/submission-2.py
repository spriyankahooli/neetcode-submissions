class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen ={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        for val in seen.values():
            if val!=1:
                return True 
        return False
        