# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left == None and root.right== None:
            return root.val == targetSum

        
        targetSum -= root.val

        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
        