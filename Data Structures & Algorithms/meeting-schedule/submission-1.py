"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)
        previous = intervals[0]

        for interval in intervals[1:]:
            if previous.end > interval.start:
                return False 
            else:
                previous = interval
        return True
