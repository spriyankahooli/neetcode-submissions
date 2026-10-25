class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        overlap_interval = 0
        previous = intervals[0]
        for current  in intervals[1:]:
            if previous[1] > current[0]:
                overlap_interval +=1

                if current[1] < previous[1]:
                    previous = current
            else:
                previous =current 

        return overlap_interval
