class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0)+1
        bucket = [[] for _ in range(len(nums)+1)]

        for key, item in seen.items():
            bucket[item].append(key)
        res = []
        for i in range(len(bucket)-1,0,-1):
            for val in bucket[i]:
                res.append(val)
                if len(res)==k:
                    return res