class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            pos = nums2.index(num)
            for j in range(pos + 1, len(nums2)):
                if nums2[j] > num:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
        return res
