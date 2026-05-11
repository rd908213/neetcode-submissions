# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], length=0) -> int:
        if not root:
            return length

        length += 1
        leftLength, rightLength = 0, 0 # Initialize to zero to avoid accessing uninitialized vars
        
        # Explore both sides of this branch
        if root.left:
            leftLength = self.maxDepth(root.left, length)
        if root.right:
            rightLength = self.maxDepth(root.right, length)
        if not root.left and not root.right: # If this is the bottom of this branch
            return length
        
        return(max(leftLength, rightLength))