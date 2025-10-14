# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        is_b = [True]

        def getIsBalanced(root):
            

            if not root:

                return 0
            
            left_depth = getIsBalanced(root.left)
            right_depth = getIsBalanced(root.right)

            if abs(left_depth - right_depth) > 1:

                is_b[0] = False
            
            mx_depth = 1 + max(left_depth, right_depth)

            return mx_depth
        
        dep = getIsBalanced(root)

        return is_b[0]
            
