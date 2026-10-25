class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for number in nums1:
            for i, num in enumerate(nums2):
                if number == num:
                    res.append(i)
                    break
        return res