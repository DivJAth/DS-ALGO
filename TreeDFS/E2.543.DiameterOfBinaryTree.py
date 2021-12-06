# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:
# Input: root = [1,2]
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTreeHelper(self, root, max_path):
        if root:
            left =  self.diameterOfBinaryTreeHelper(root.left, max_path) 
            right =  self.diameterOfBinaryTreeHelper(root.right, max_path)
            max_path[0] = max(max_path[0] , left+right)
            return max(left, right)+1
        return 0
            
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = [0]
        self.diameterOfBinaryTreeHelper(root, max_path)
        return max_path[0]