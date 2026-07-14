# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isTheSameTree(self, rootA: Optional[TreeNode], rootB: Optional[TreeNode]) -> bool:
        if not rootA and not rootB:
            return True
        
        if not rootA:
            return False
        
        if not rootB:
            return False
        
        if rootA.val != rootB.val:
            return False
        
        return self.isTheSameTree(rootA.left, rootB.left) and self.isTheSameTree(rootA.right, rootB.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isTheSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
