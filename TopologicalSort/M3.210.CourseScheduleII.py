# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = {}
        inDeg = {}
        ordering = []
        
        for i in prerequisites:
            G[i[1]] = G.get(i[1],[]) +[i[0]]
            inDeg[i[0]] = inDeg.get(i[0], 0) + 1
        
        q = deque()
        for j in range(numCourses):
            if inDeg.get(j, 0) == 0:
                q.append(j)
        
        while q:
            ele = q.popleft()
            ordering.append(ele)
            for child in G.get(ele, []):
                inDeg[child] -= 1
                if inDeg[child] == 0:
                    q.append(child)

        if len(ordering) != numCourses:
            return None
        return ordering
                    