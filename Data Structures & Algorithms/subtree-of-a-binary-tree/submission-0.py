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
        self.hasSubtree = False

        def isSubtreeRec(root, subRoot):
            if not root:
                return False
            
            self.hasSubtree = self.hasSubtree or self.isTheSameTree(root, subRoot)
            isSubtreeRec(root.left, subRoot)
            isSubtreeRec(root.right, subRoot)
        
        isSubtreeRec(root, subRoot)
        return self.hasSubtree

