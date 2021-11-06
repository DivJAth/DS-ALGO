# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#     For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        G = defaultdict(list)
        inDeg = {}
        order = 0
        
        for i in prerequisites:
            G[i[1]] = G.get(i[1], []) + [i[0]]
            inDeg[i[0]] = inDeg.get(i[0], 0)+1
        q = deque()
        
        for j in range(numCourses):
            if inDeg.get(j, 0) == 0:
                q.append(j)
        
        while q:
            ele = q.popleft()
            order+=1
            for child in G.get(ele,[]):
                inDeg[child]-=1
                if inDeg[child] == 0:
                    q.append(child)
        
        if order !=  numCourses:
            return False
        
        return True
