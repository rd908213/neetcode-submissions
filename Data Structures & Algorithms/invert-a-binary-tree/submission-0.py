# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            r = root.right
            l = root.left
            root.right = l
            root.left = r
            return root