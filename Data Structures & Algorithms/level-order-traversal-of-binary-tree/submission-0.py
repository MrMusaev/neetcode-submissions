# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            queueL = len(q)
            curLevel = []
            for i in range(queueL):
                node = q.popleft()
                curLevel.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            result.append(curLevel)
        
        return result