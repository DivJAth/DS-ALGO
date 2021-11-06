# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
#     2 <= nums.length <= 105
#     -30 <= nums[i] <= 30
#     The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]*(len(nums))
        right_prod = [1]*(len(nums))
        # Compute the product for elements to the left of the index and NOT including the current index
        for i in range(1,len(nums)):            
            left_prod[i] = left_prod[i-1]*nums[i-1]
        # Compute the product for elements to the right of the index and NOT including the current index
        for i in range(len(nums)-1,0,-1):  
            right_prod[i-1] = nums[i] * right_prod[i]        
        for i in range(len(nums)):
            nums[i] = left_prod[i] * right_prod[i]
        return nums   

# Attempt 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(1,len(nums)):
            left.append(left[i-1]*nums[i-1])
        
        right = 1
        for j in range(len(nums)-1, -1, -1):
            left[j] *= right
            right*=nums[j]
        
        return left
            
      
     