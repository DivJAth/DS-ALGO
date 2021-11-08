# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]


class Solution:
    def generateParenthesisHelper(self, curComb, ans, maxCnt, openCnt, closeCnt):
        if len(curComb) == maxCnt*2:
            ans.append("".join(curComb))
            return
        
        if openCnt < maxCnt:
            curComb.append('(')
            self.generateParenthesisHelper(curComb, ans, maxCnt, openCnt+1, closeCnt)
            curComb.pop()
        
        if closeCnt < openCnt:
            curComb.append(')')
            self.generateParenthesisHelper(curComb, ans, maxCnt, openCnt, closeCnt+1)
            curComb.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curComb = []
        self.generateParenthesisHelper(curComb, ans, n, 0, 0)
        return ans

# efficient BFS
class Solution:
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        q = deque()
        q.append(["",0,0])
        
        while q:
            ele = q.popleft()
            if len(ele[0]) == n*2 and ele[1]==ele[2]:
                ans.append(ele[0])
            if  ele[1]<n:
                q.append( [ele[0]+'(', ele[1]+1, ele[2]])
            if  ele[1] > ele[2]:
                q.append( [ele[0]+')', ele[1], ele[2]+1])
        return ans