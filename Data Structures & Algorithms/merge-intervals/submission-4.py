class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda key:key[0])
        stack = [intervals[0]]
        
        for interval in intervals[1:]:
            if stack and stack[-1][1] >= interval[0]:
                stack[-1][1] = max(stack[-1][1],interval[1])
            else:
                stack.append(interval)
        return stack
        