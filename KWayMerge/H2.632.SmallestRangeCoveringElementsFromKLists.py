# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

# Example 1:

# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].

# Example 2:
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]

# Example 3:
# Input: nums = [[10,10],[11,11]]
# Output: [10,11]

# Example 4:
# Input: nums = [[10],[11]]
# Output: [10,11]

# Example 5:
# Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
# Output: [1,7]

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        hp = []
        max_val = -float("inf")
        min_range = float("inf")
        result = []
        for i in  range(0,len(nums)):
            heapq.heappush(hp, (nums[i][0], i, 0))
            if max_val <= nums[i][0]: 
                max_val = nums[i][0]
                
        while len(nums)==len(hp):
            val, i, j = heapq.heappop(hp)
            
            if max_val - val < min_range:
                min_range = max_val - val
                result = [val, max_val]
            
            if len(nums[i]) > j+1:
                if max_val <= nums[i][j+1]: 
                    max_val = nums[i][j+1]
                heapq.heappush(hp, (nums[i][j+1], i, j+1) )
        return result