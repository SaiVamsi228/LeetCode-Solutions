# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getIsBalanced(self,root):

        if not root:

            return [True,0]
        
        leftBalanced, lh = self.getIsBalanced(root.left)
        rightBalanced, rh = self.getIsBalanced(root.right)

        balanced = abs(lh - rh) <= 1 and leftBalanced and rightBalanced

        return [balanced,1 + max(lh,rh)] 

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.getIsBalanced(root)[0]
        