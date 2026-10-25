class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq= math.ceil(len(nums)/2)
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        for num ,val in count.items():
            if val>= freq:
                return num
        return -1

        