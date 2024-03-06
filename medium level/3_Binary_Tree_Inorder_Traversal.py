# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []

        def fgo(root: Optional[TreeNode]):
            if root.left:
                fgo(root.left)
            r.append(root.val)
            if root.right:
                fgo(root.right)

        if root:
            fgo(root)
        return r
