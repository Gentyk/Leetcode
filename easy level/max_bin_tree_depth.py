# Given the root of a binary tree, return its maximum depth.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:  # root: TreeNode
        if not root:
            return 0
        a = self.maxDepth(root.right) if root.right else 0
        b = self.maxDepth(root.left) if root.left else 0
        return max(a,b)+1