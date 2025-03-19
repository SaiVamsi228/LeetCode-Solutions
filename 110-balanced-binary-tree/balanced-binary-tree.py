# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        is_balanced = True

        def get_height_and_is_balanced(root):

            nonlocal is_balanced

            if root.left == None and root.right == None:

                return 1
            
            lh = rh = 0

            if root.left:

                lh = get_height_and_is_balanced(root.left)
            
            if root.right:
                
                rh = get_height_and_is_balanced(root.right)

            if abs(lh - rh ) > 1:

                is_balanced = False

            return 1 + max(rh,lh)        
        
        if root == None:

            return True

        get_height_and_is_balanced(root)

        return is_balanced
