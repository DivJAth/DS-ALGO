# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0

class Solution:
    def twoSumClosest(self, nums, target):
        mindiff = float("inf")
        i, j = 0, len(nums)-1
        while i < j : 
            val = nums[i] + nums[j]
            diff = target - val 
            if abs(diff) < abs(mindiff):
                mindiff = diff
            if val < target:
                i += 1
            else:
                j -= 1
        return mindiff
                
        
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mindiff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            diff = self.twoSumClosest(nums[i+1:], target-nums[i])
            if abs(diff) < abs(mindiff):
                mindiff = diff
        return target-mindiff
 