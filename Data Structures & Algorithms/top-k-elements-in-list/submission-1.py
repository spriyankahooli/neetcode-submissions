class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        heap = []
        for num,freq in freq.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]
        