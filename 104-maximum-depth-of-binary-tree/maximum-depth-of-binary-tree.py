# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        

        def get_max_depth(root):

            if root.left == None and root.right == None:

                return 1

            ld = rd = 0

            if root.left:
                
                ld = get_max_depth(root.left)

            if root.right:
                
                rd = get_max_depth(root.right)

            return 1 + max(ld,rd)

        if not root:

            return 0
            
        return get_max_depth(root)