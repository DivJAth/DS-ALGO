# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        sum_val = 0
        min_range = float('inf')
        while j < len(nums):
            sum_val+=nums[j]
            while i < len(nums) and target <= sum_val:
                if target <= sum_val:
                    min_range = min(min_range, j-i+1)
                sum_val-=nums[i]
                i+=1
            j+=1
        return min_range if min_range != float('inf') else 0
            
        