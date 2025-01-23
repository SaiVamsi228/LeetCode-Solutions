# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def getMinDepth(root,depth):

            if not root.left and not root.right:

                return depth
            
            left_depth = getMinDepth(root.left,depth+1) if root.left else float('inf')
            
            right_depth = getMinDepth(root.right,depth+1) if root.right else float('inf')

            return min(left_depth,right_depth)
        
        if not root:

            return 0

        return getMinDepth(root,1)