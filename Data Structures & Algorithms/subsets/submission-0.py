class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(0,nums,[],res)
        return res 

    def backtrack(self,i,nums,candidate,res):
        if i == len(nums):
            res.append(candidate[:])
            return 
        candidate.append(nums[i])
        self.backtrack(i+1,nums,candidate,res)
        candidate.pop()
        self.backtrack(i+1,nums,candidate,res)
        