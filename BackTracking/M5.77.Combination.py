# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output:[[2,4], [3,4], [2,3], [1,2], [1,3],[1,4]]

# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]

class Solution:
    def combHelper(self, candidates, target, ans, curComb, start):
        # acceptance criteria
        if target == 0:
            ans.append(list(curComb))
        # rejection criteria
        elif target < 0:
            return
        
        # continued exploratioon
        # If the start value is not passed you will get all combination of the number. 
        # e.g. [2,2,3], [2,3,2], [3,2,2] . So once your done with an index you 
        # dont wont to start from the begining        
        for i in range(start, candidates+1):
            curComb.append(i)
            self.combHelper(candidates, target-1, ans, curComb, i+1)
            curComb.pop()
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curComb = []
        self.combHelper(n, k, ans, curComb, 1)
        return ans

 