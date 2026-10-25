class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0)+1
        bucket = [[] for _ in range(len(nums)+1)]

        for key,val in seen.items():
            bucket[val].append(key)
        res =[]
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res