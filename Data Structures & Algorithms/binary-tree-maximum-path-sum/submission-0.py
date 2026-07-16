# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxSum = float('-inf')
    
    def maxPathSumRec(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        left_subtree_sum = max(self.maxPathSumRec(root.left), 0)
        right_subtree_sum = max(self.maxPathSumRec(root.right), 0)

        self.maxSum = max(self.maxSum, root.val + left_subtree_sum + right_subtree_sum)

        return root.val + max(left_subtree_sum, right_subtree_sum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSumRec(root)
        return self.maxSum        