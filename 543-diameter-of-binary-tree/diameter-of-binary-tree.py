# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def get_height_and_dia(root):

            nonlocal diameter

            if root.left == None and root.right == None:

                return 1
            
            lh = rh = 0

            if root.left :
                
                lh = get_height_and_dia(root.left)
            
            if root.right:
                
                rh = get_height_and_dia(root.right)
            
            if lh + rh > diameter:

                diameter = lh + rh

            return 1 + max(lh,rh)
        
        get_height_and_dia(root)

        return diameter
        