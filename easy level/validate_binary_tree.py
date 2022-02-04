# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def check_left(self, root, max_v=None, min_v=None):
        if not root:
            return False
        left = True
        right = True
        if max_v and root.val >= max_v or min_v and root.val <= min_v:
            return False
        if root.left:
            max_v_ = root.val if max_v is None else min(root.val, max_v)
            if root.left.val >= max_v_:
                return False
            if min_v and root.left.val <= min_v:
                return False
            left = self.check_left(root.left, max_v=max_v_, min_v=min_v)
        if root.right:
            if max_v and root.right.val >= max_v or root.right.val <= root.val:
                return False
            if min_v and root.right.val <= min_v:
                return False
            right = self.check_right(root.right, max_v=max_v, min_v=root.val)
        return right and left

    def check_right(self, root, max_v=None, min_v=None):
        if not root:
            return False
        left = True
        right = True
        if max_v and root.val >= max_v or min_v and root.val <= min_v:
            return False
        if root.left:
            if max_v and root.left.val >= max_v:
                return False
            if min_v and root.left.val <= min_v:
                return False
            left = self.check_left(root.left, max_v=root.val, min_v=min_v)
        if root.right:
            if max_v and root.right.val >= max_v or root.right.val <= root.val:
                return False
            min_v_ = root.val if min_v is None else max(root.val, min_v)
            if min_v and root.right.val <= min_v:
                return False
            right = self.check_right(root.right, min_v=min_v_, max_v=max_v)
        return right and left

    def isValidBST(self, root) -> bool: # root: Optional[TreeNode]
        if not root:
            return False
        if root.left and root.val <= root.left.val:
            return False
        if root.right and root.val >= root.right.val:
            return False

        a = self.check_left(root.left, max_v=root.val) if root.left else True
        b = self.check_right(root.right, min_v=root.val) if root.right else True
        return a and b