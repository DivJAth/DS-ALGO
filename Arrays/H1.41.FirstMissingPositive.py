# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
# Example 1:
# Input: nums = [1,2,0]
# Output: 3

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        space = ["x"]*(len(nums))
        min_val = float("inf")
        
        for i in nums:
            if i > 0:
                min_val = min(i, min_val)
        
        if min_val >1:
            return 1
        
        j = 0
        while j < len(nums):
            if len(nums) > nums[j] - min_val >= 0 :
                space[nums[j]-min_val] = nums[j]
            j+=1
        
        for k in range(len(space)):
            if space[k]=="x":
                return k+min_val
        return len(nums)


#  MOre efficient with space       
#         n = len(nums)
        
#         for i in range(n):
#             if nums[i] <= 0 or nums[i] > n:
#                 nums[i] = 1
        
#         for i in range(n): 
#             a = abs(nums[i])
#             if a == n:
#                 nums[0] = - abs(nums[0])
#             else:
#                 nums[a] = - abs(nums[a])
            
#         for i in range(1, n):
#             if nums[i] > 0:
#                 return i
        
#         if nums[0] > 0:
#             return n
            
#         return n + 1
