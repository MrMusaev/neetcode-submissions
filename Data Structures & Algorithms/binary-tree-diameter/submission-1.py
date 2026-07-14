# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left:
            return max(self.treeHeight(root.right), self.diameterOfBinaryTree(root.right))
        
        if not root.right:
            return max(self.treeHeight(root.left), self.diameterOfBinaryTree(root.left))
        
        return self.treeHeight(root.right) + self.treeHeight(root.left)