# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [ [1,1,6],[1,2,5],[1,7],[2,6]]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: [[1,2,2],[5]]

class Solution:
    def combHelper(self, candidates, target, ans, curComb, start):
        if target == 0:
            ans.append(list(curComb))
        elif target < 0:
            return
       
        for i in range(start, len(candidates)):
            # Using a for loop with fixed start and end.
            # You shouldnt use a while to increment the i
            if i > start and candidates[i]==candidates[i-1]:
                 continue
            curComb.append(candidates[i])
            self.combHelper(candidates, target-candidates[i], ans, curComb, i+1)
            curComb.pop()
        
                  
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        curComb = []
        candidates = sorted(candidates)
        self.combHelper(candidates, target, ans, curComb, 0)
        return ans
        


