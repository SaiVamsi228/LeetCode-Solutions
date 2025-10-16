# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def getLCA(node,p,q):

            if not node:

                return None
            
            if node == p :

                return p
            
            if node == q:

                return q
            
            if p.val < node.val < q.val or p.val > node.val > q.val:

                return node
            
            if p.val < node.val and q.val < node.val:

                return getLCA(node.left,p,q)
            
            elif p.val > node.val and q.val > node.val:

                return getLCA(node.right,p,q)
        
        return getLCA(root,p,q)