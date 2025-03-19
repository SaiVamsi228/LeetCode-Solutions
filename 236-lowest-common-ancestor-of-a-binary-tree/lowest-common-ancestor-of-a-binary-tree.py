# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(root,p,q):

            if root == p :

                return root
            
            if root == q:

                return root
            
            if not root.left and not root.right:

                return None
            
            rlca = llca = None

            if root.left:
                
                llca = lca(root.left, p , q)

            if root.right:
                
                rlca = lca(root.right, p, q)

            if llca == None :

                return rlca
            
            if rlca == None:

                return llca
            
            return root
        
        return lca(root,p,q)