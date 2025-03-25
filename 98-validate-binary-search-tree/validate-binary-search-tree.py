# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def getIsValid(root,left_lim, right_lim):

            if not root:

                return True
            
            checkIsLeftValid = getIsValid(root.left,left_lim, root.val)

            checkIsRightValid = getIsValid(root.right,root.val, right_lim)

            isCurrentValid = left_lim < root.val < right_lim 

            return checkIsLeftValid and checkIsRightValid and isCurrentValid
        
        return getIsValid(root,-float('inf'), float('inf'))

