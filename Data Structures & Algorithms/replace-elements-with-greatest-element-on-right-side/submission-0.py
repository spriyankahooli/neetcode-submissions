# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         res = [-1] * len(arr)
#         maxN = -1
#         for i in range(len(arr) - 1, -1, -1):
#             res[i] = maxN
#             if arr[i] > maxN:
#                 maxN = arr[i]
#         return res























class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []

        for i in range(len(arr)-1):
            result.append(max(arr[i+1:]))
        result.append(-1)

        return result



