# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def get_right_view(node,level,res):

            if node == None:

                return 

            if len(res) == level:

                res.append(node.val)

            get_right_view(node.right,level+1,res)
            
            get_right_view(node.left,level+1,res)
        
        res = []

        level = 0

        get_right_view(root,level,res)

        return res
        

         