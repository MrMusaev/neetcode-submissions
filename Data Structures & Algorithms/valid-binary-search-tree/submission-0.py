# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBSTRec(self, root: Optional[TreeNode], lower: int, higher: int) -> bool:
        if not root:
            return True
        
        if not lower < root.val < higher:
            return False
        
        return self.isValidBSTRec(root.left, lower, root.val) and self.isValidBSTRec(root.right, root.val, higher)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRec(root, float('-inf'), float('inf'))