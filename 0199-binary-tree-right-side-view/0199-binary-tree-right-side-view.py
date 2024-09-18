# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        q=collections.deque()

        q.append(root)

        while(q):
            q_len=len(q)
            level=[]
            for i in range(q_len):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)

        final_result=[]

        for sub_list in result:
            final_result.append(sub_list[-1])
        
        return final_result    
        

        