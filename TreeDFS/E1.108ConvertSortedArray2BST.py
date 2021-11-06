# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

# Example 1:

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:

# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root = None
    
    def preOrderHelper(self,nums ,left, right):
        if left <= right:
            mid = left + (right - left)//2
            node = TreeNode(nums[mid])
            if self.root is None:
                self.root = node
            
            node.left = self.preOrderHelper(nums, left, mid-1)
            node.right = self.preOrderHelper(nums, mid+1, right)
            return node
        return None
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        self.preOrderHelper(nums, 0 , len(nums)-1 )
        return self.root
