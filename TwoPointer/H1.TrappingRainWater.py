# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Solution is a two pointer solution O(n), space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        
        left_max, right_max, ans = 0, 0, 0
        while i < j:
            left_max = max(left_max,height[i])
            right_max = max(right_max,height[j])
            if height[i] < height[j]:
                ans += (left_max - height[i] )
                i+=1
            else:
                ans += (right_max - height[j] )
                j-=1
                
        return ans