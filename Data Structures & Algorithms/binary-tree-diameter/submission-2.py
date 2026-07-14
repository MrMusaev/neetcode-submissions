# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def heightDfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            leftH = heightDfs(root.left)
            rightH = heightDfs(root.right)
            self.result = max(self.result, leftH + rightH)

            return 1 + max(leftH, rightH)
        
        heightDfs(root)
        return self.result