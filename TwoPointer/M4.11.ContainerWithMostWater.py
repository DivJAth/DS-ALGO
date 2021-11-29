# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16

# Example 4:
# Input: height = [1,2,1]
# Output: 2

class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        # left_max = [0]*n
        # right_max = [0]*n
        # for i in range(0,n):
        #     if not i:
        #         left_max[i] = height[i]
        #         right_max[n-i-1] = height[n-i-1]
        #     else:
        #         left_max[i] = max(left_max[i-1], height[i])
        #         right_max[n-i-1] = max(right_max[n-i],height[n-i-1])
        
        i = 0
        j = n-1
        maxArea= -float(inf)
        while i < j:
            maxArea = max(maxArea, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return maxArea
        
