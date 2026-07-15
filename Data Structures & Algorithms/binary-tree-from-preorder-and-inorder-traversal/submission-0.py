# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.preorder_index = 0
        self.inorder_index_map = {}

    def buildSubTree(self, preorder, inorder, left, right):
        if left > right:
            return

        curVal = preorder[self.preorder_index]
        node = TreeNode(curVal)
        inorder_index = self.inorder_index_map[curVal]
        self.preorder_index += 1

        # build left subtree
        node.left = self.buildSubTree(preorder, inorder, left, inorder_index - 1)
        node.right = self.buildSubTree(preorder, inorder, inorder_index + 1, right)

        return node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # build index map of inorder array for search efficiency
        for i, val in enumerate(inorder):
            self.inorder_index_map[val] = i
        
        # pass arrays and lef and right boundaries of inorder for this subtree
        # initially it is entire inorder array
        return self.buildSubTree(preorder, inorder, 0, len(inorder) - 1)