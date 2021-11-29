# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:

# Input: nums = []
# Output: []

# Example 3:

# Input: nums = [0]
# Output: []

class Solution:
    def twoSum(self, target, nums):
        start = 0
        end = len(nums)-1
        lst = []
        while start < end:
            if nums[start]+nums[end]+ target==0:
                lst.append([target, nums[start], nums[end]])
                end-=1
                start+=1
                while start < end and nums[start-1]==nums[start]:
                    start+=1
            elif nums[start]+nums[end] + target > 0:
                end -= 1
            else:
                start+= 1
        return lst
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i == 0 or nums[i]!= nums[i-1]:
                val = self.twoSum(nums[i], nums[i+1:])
                if val:
                    result= result + val
        return result