# You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

# In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

# Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

 

# Example 1:

# Input: n = 3, relations = [[1,3],[2,3]]
# Output: 2
# Explanation: The figure above represents the given graph.
# In the first semester, you can take courses 1 and 2.
# In the second semester, you can take course 3.

# Example 2:

# Input: n = 3, relations = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: No course can be studied because they are prerequisites of each other.

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        inDeg = {}
        G = {}
        order = 0
        q = deque()
        
        for i in relations:
            G[i[0]] = G.get(i[0], []) + [i[1]]
            inDeg[i[1]] = inDeg.get(i[1],0) + 1
        
        for j in range(1,n):
            if inDeg.get(j, 0 ) == 0:
                q.append(j)
        cnt = 0
        while q: 
            l = len(q)
            cnt+=1
            while l > 0:
                ele = q.popleft()
                order+=1
                for child in G.get(ele, []):
                    inDeg[child]-=1
                    if inDeg[child] == 0:
                        q.append(child)
                l-=1
        
        if order != n:
            return -1
            
        return cnt
                