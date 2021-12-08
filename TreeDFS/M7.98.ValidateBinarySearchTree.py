# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

 

# Example 1:

# Input: root = [2,1,3] level order
# Output: true

# Example 2:

# Input: root = [5,1,4,null,null,3,6] level order
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidHelper(self, root, min_val, max_val):
        if root:
            print(min_val, root.val, max_val)
            if  min_val >= root.val  or root.val >= max_val:
                return False

            return self.isValidHelper(root.left, min_val, root.val) and self.isValidHelper(root.right, root.val, max_val)
        return True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val = -float('inf')
        max_val = float('inf')

        if root:
            return self.isValidHelper(root, min_val, max_val)
        return False
        