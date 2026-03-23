from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = [[] for _ in range(numCourses)]
        
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)

            indegree[course] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        completed = 0

        while queue:
            current = queue.popleft()
            completed += 1

            for neighbour in graph[current]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return completed == numCourses


        