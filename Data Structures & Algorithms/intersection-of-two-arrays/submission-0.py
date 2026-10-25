class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ints = []
        for num in nums1:
            if num not in ints and num in nums2:
                ints.append(num)
        return ints
        