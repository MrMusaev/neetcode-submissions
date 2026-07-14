# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def calculateHeightDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftH = self.calculateHeightDiff(root.left)
        rightH = self.calculateHeightDiff(root.right)

        if leftH == -1 or rightH == -1:
            return -1
        
        if abs(leftH - rightH) > 1:
            return -1

        return 1 + max(leftH, rightH)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calculateHeightDiff(root) != -1