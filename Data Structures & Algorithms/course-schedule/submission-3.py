class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph =defaultdict(list)

        for crs,pre in prerequisites:
            graph[crs].append(pre)
        visited = [0]*numCourses
        def hasCycle(crs):
            if visited[crs] == 1: return True 
            if visited[crs] == 2: return False
            visited[crs] =1
            for pre in graph[crs]:
                if hasCycle(pre):
                    return True
            visited[crs] =2 
            return False 
        for course in range(numCourses):
            if hasCycle(course):
                return False 
        return True
        
        