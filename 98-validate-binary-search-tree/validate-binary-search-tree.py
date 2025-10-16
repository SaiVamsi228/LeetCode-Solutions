# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def getIsValid(node,left_bound,right_bound):

            if not node:

                return True
            
            if not (left_bound < node.val < right_bound):

                return False
            
            left_valid = getIsValid(node.left,left_bound, node.val)

            right_valid = getIsValid(node.right, node.val, right_bound)

            return left_valid and right_valid
        
        return getIsValid(root,float('-inf'),float('inf'))

            
