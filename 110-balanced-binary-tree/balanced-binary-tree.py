# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getIsBalanced(node):

            if not node:

                return 0
            
            lh = getIsBalanced(node.left)

            rh = getIsBalanced(node.right)

            if abs(lh-rh) > 1 :

                return float('inf')
            
            return 1 + max(lh,rh)
        
        ans = getIsBalanced(root)

        if ans == float('inf'):

            return False
        
        return True
