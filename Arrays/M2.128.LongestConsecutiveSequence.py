# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len, ele_cnt = 0, 0
        nums = set(nums)
        for j in nums:
            if j - 1  not in nums:
                ele_cnt = 0
                start_ele = j
                while start_ele in nums:
                    ele_cnt += 1
                    start_ele += 1
            max_len = max(max_len, ele_cnt)
        
        return max_len