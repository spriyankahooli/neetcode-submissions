class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        stack = [intervals[0]]
        for interval in intervals[1:]:
            if stack and stack[-1][1] < interval[0]:
                stack.append(interval)
            stack[-1][1] = max(stack[-1][1], interval[1])
        return stack