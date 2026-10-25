class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda  interval: interval[0])
        merged = [intervals[0]]
        for interval in intervals[1:]:
            if  merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged