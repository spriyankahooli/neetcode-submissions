class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1= {}
        heap =[]
    
        for num in nums:
            map1[num] = map1.get(num,0)+1
        for num,freq in map1.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) >k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]

