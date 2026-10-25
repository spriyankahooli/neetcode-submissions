class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])

        stack = [intervals[0]]
        for interval in intervals:
            if stack and stack[-1][1] < interval[0]:
                stack.append(interval)
            else:
                stack[-1][1] = max(interval[1], stack[-1][1])
        return stack