# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedHelper(self, root: Optional[TreeNode]) -> (bool, int):
        if root is None:
            return True, 0
        balanced_l, height_l = self.isBalancedHelper(root.left)
        balanced_r, height_r = self.isBalancedHelper(root.right)
        balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
        height = 1 + max(height_l, height_r)

        return balanced, height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root)[0]
      