# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def get_lca(node,p,q):

            if not node:

                return None
            
            if node == p or node == q:

                return node
            
            if (p.val < node.val and q.val > node.val) or (q.val < node.val and p.val > node.val):

                return node
            
            get_left_lca = get_right_lca = None
            
            if p.val < node.val:
                
                get_left_lca = get_lca(node.left,p,q)
            
            elif p.val > node.val:

                get_right_lca = get_lca(node.right,p,q)
            
            return get_left_lca or get_right_lca
        
        return get_lca(root,p,q)


        