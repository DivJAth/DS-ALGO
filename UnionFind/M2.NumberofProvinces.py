# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Example 2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

# Constraints:
#     1 <= n <= 200
#     n == isConnected.length
#     n == isConnected[i].length
#     isConnected[i][j] is 1 or 0.
#     isConnected[i][i] == 1
#     isConnected[i][j] == isConnected[j][i]

#  Can be done through DFS would be faster O(E+V)
#  Union find is better for dynamic graphs with in coming edges.

class UnionFind:
    def __init__(self, sz):
        self.size = [1]*sz
        self.parent = [i for i in range(0,sz)]
        self.connected = sz
        
    def getComponentCnt(self):
        return self.connected
        
    def find(self, x):
        if x == self.parent[x]:
            return x
        return self.find(self.parent[x])
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        if py == px:
            return
        
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
            self.size[px] = 0
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
            self.size[py] = 0
            
        self.connected-=1
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        for i in range(0,len(isConnected)):
            for j in range(0, len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.union(i,j)
        return uf.getComponentCnt()

