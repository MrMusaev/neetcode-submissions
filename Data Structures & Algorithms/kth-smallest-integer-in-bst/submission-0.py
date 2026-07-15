# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nums = []

        def dfsInOrder(root):
            if not root:
                return
            
            dfsInOrder(root.left)
            self.nums.append(root.val)
            dfsInOrder(root.right)
        
        dfsInOrder(root)

        return self.nums[k - 1] if k <= len(self.nums) else -1
