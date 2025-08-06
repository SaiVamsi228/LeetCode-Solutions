# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node,left_lim,right_lim):

            if not node:

                return True
            
            if not (left_lim < node.val < right_lim):

                return False
            
            check_left = isValid(node.left,left_lim, node.val)

            check_right = isValid(node.right,node.val, right_lim)

            return check_left and check_right
        
        return isValid(root,float('-inf'), float('inf'))