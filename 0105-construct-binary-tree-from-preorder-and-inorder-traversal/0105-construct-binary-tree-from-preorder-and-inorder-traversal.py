# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Base case: if the preorder list is empty, return None (no tree/subtree to build)
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is the root of the current tree/subtree
        root = TreeNode(preorder[0])
        
        # Find the index of the root in inorder to divide the tree into left and right subtrees
        mid = inorder.index(preorder[0])
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
