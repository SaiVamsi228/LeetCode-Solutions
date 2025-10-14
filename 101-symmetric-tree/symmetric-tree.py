# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def getIsSymm(p,q):

            if not p and not q:

                return True
            
            if (p and not q ) or (not p and q):

                return False
            
            if p.val != q.val:

                return False
            
            left_symm = getIsSymm(p.left,q.right)
            right_symm = getIsSymm(p.right,q.left)

            return left_symm and right_symm
        
        if not root:

            return True
            
        return getIsSymm(root.left,root.right)
