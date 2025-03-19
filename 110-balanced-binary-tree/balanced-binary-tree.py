# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_height(root):

            if root.left == None and root.right == None:

                return 1
            
            lh = rh = 0

            if root.left:

                lh = get_height(root.left)
            
            if root.right:
                
                rh = get_height(root.right)

            return 1 + max(rh,lh)

        def get_is_balanced(root):

            if root.left == None and root.right == None:

                return True
            
            lb = rb = True

            lh = rh = 0
            
            if root.left:
                
                lb = get_is_balanced(root.left)
                
                lh = get_height(root.left)
            
            if root.right:
                
                rb = get_is_balanced(root.right)

                rh = get_height(root.right)

            cb = True if abs(lh - rh) <= 1 else False

            return lb and rb and cb
        
        if root == None:

            return True

        return get_is_balanced(root)
