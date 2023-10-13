# https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        
        visited = [0]*numCourses

        def isAcyclic(v):
            if visited[v] == -1:
                return False
            if visited[v] == 1: 
                return True
            visited[v] = -1
            for postCourse in graph[v]:
                if not isAcyclic(postCourse):
                    return False
            visited[v] = 1
            return True
        
        for n in range(numCourses):
            if not isAcyclic(n):
                return False
        return True