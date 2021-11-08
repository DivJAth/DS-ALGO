# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curComb = []
        self.permHelper(nums, len(nums), ans, curComb, 0)
        return ans
    
    def permHelper(self, candidates, target, ans, curComb, start):
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
        for i in range(start, len(candidates)):
            for j in range(len(curComb)+1):
                inter = list(curComb)
                inter.insert(j,candidates[i])
                self.permHelper(candidates, target-1, ans, inter, i+1)
                inter.pop()

# Non recursive solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numsLength = len(nums)
        result = []
        permutations = deque()
        permutations.append([])
        for currentNumber in nums:
            # we will take all existing permutations and add the current number to create new permutations
            n = len(permutations)
            for _ in range(n):
                oldPermutation = permutations.popleft()
                # create a new permutation by adding the current number at every position
                for j in range(len(oldPermutation)+1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(j, currentNumber)
                    if len(newPermutation) == numsLength:
                        result.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
                