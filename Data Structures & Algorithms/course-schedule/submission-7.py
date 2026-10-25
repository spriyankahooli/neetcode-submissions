class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course,pre in prerequisites:
            graph[course].append(pre)
        visited = [0]*numCourses

        def hasCycle(course):
            if visited[course] ==1: return True 
            if visited[course] == 2: return False
            visited[course] =1
            for pre in graph[course]:
                if hasCycle(pre):
                    return True 
            visited[course] = 2
            return False 
        for course in range(numCourses):
            if hasCycle(course):
                return False 
        return True
 
       