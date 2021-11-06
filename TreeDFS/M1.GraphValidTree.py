# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false


# check for cycle in the graph. handles disjoint graphs
# union find is the better option cause this can be treated as dynamic graph ith incoming edges.

class Solution:
    def isCycle(self, i, G, visited, parent):
        visited[i] = True
        for child in G[i]:
            if visited[child] == False:
                if self.isCycle(child, G, visited, i) == True:
                    return True
            elif parent != child:
                return True
        return False
        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: 
            return False
        
        G = defaultdict(list)
 
        # build Graph
        for edge in edges:
            G[edge[0]].append(edge[1])
            G[edge[1]].append(edge[0])            
        visited = [False]*n
        
        for i in range(n):
            if visited[i] == False:
                if self.isCycle(i, G, visited,-1) == True:
                    return False
        return True