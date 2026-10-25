class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap =[]
        seen ={}
        for num in nums:
            seen[num] = seen.get(num,0)+1
        for num,freq in seen.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) >k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]
