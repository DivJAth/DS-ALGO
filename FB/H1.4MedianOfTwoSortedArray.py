# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Example 3:
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000

# Example 4:
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000

# Example 5:
# Input: nums1 = [2], nums2 = []
# Output: 2.00000

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
       
        i,j,x = 0, 0, 0
        result = [0,0]
        while (i < l1 or j < l2 )and i+j <= (l1+l2)//2:
            if i< l1 and j< l2:
                if nums1[i]<nums2[j]:
                    val = nums1[i]
                    i+=1
                else:
                    nums1[i]>nums2[j]
                    val = nums2[j]
                    j+=1
            elif i<l1:
                val = nums1[i]
                i+=1
            elif j<l2:
                val = nums2[j]
                j+=1
            result[x]= val
            x = 1-x
        if (l1+l2)%2 == 0:
            return sum(result)/2.0
        else:
            return max(result)/1.0


# can be done with better complexity o(log(m+n))