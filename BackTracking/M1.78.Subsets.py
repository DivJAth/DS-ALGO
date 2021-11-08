
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for i in nums:
            l = len(subsets)
            for j in range(l):
                new_sub = list(subsets[j]+[i])
                subsets.append(new_sub)
        return subsets

class Solution:
    def combHelper(self, candidates, ans, curComb, start):
        ans.append(list(curComb))     
        for i in range(start, len(candidates)):
            curComb.append(candidates[i])
            self.combHelper(candidates, ans, curComb, i+1)
            curComb.pop()
    
    def subsets(self, candidates: List[int]) -> List[List[int]]:
        ans = []
        curComb = []
        self.combHelper(candidates, ans, curComb, 0)
        return ans