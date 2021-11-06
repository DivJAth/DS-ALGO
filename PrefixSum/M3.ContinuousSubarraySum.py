# Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false

"""
    [1, 2, 3, 4,]  <= array
    [1, 3, 6, 10] <= cummulative sums
    10 -1 =  19  = 2+3+4
    6 -1  =   5  = 2+3

if we store the cumulative sum for every point (idx) in the array,
    if (sum2-sum1) % k = 0
    then the numbers between sum2-sum1 add up to a multiple of k

if you find duplicated sum%k values, then that the sub array between those two indexes will actually be the solution.
(sum2-sum1) % k = 0
sum2%k - sum1%k = 0
sum2%k = sum1%k

"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        remainderIndex = {0:[-1, -float('inf')]}
        cumSum = 0
        for i in range(0, len(nums)):
            cumSum+=nums[i]
            remInd = cumSum%k
            # print(nums[i], cumSum, remInd)
            if (len(remainderIndex.get(remInd, [])) == 0):
                remainderIndex[remInd] = [i, -float('inf')]
            else:
                remainderIndex[remInd][1] = i
                
        for key in remainderIndex.keys():
            val = remainderIndex[key]
            if val[1]-val[0] > 1:
                return True
        
        return False

# Attempt 2
class Solution:
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False

        # 0: -1 is for edge case that current sum mod k == 0
        # for when the current running sum is cleanly divisible by k
        # e.g: nums = [4, 2], k = 3
        sums = {0: -1}  # 0
        cumulative_sum = 0
        for idx, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k

            # if current_sum mod k is in dict and index idx - sums[remainder] > 1, we got the Subarray!
            # we use 2 not 1 because the element at sums[remainder] is not in the subarray we are talking about
            if remainder in sums and idx - sums[remainder] >= 2:
                return True

            # if current sum mod k not in dict, store it so as to ensure the further values stay
            if remainder not in sums:
                sums[remainder] = idx
