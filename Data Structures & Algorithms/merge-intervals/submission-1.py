class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda  interval: interval[0])
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if  merged[-1][1] < interval[0]:
                merged.append(interval)
            merged[-1] = [min(merged[-1][0],interval[0]),
            max(merged[-1][1],interval[1])]
        return merged

        
