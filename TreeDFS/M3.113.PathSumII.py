# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22

# Example 2:

# Input: root = [1,2,3], targetSum = 5
# Output: []

# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSumHelper(self, root, targetSum, path, paths):
        if root:
            targetSum-=root.val
            path.append(root.val)
            if targetSum == 0 and root.right==None and root.left == None:
                paths.append(list(path))
            self.pathSumHelper(root.left, targetSum, path, paths)
            self.pathSumHelper(root.right, targetSum, path, paths)
            path.pop()
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        paths = []
        self.pathSumHelper(root, targetSum, path, paths)
        return paths
