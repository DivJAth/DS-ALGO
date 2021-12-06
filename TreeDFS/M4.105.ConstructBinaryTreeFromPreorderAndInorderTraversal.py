# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeHelper(self, preorder, inorder, start, end):
        if start> end:
            return None
        
        if self.preIndex < len(preorder):
            val = preorder[self.preIndex]
            self.preIndex+=1
            
            root = TreeNode(val)
            index = self.inorderIndex[val]
            
            root.left = self.buildTreeHelper(preorder, inorder, start, index-1)
            root.right = self.buildTreeHelper(preorder, inorder, index+1, end)
            return root
            
            
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # root = TreeNode(pre)
        self.preIndex = 0
        self.inorderIndex = {}
    
        for i, val in enumerate(inorder):
            self.inorderIndex[val] = i
        
        return self.buildTreeHelper(preorder, inorder, 0, len(inorder))
        
        