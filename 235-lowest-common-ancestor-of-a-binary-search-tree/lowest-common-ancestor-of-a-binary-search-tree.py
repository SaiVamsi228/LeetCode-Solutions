# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def getLCA(root,p,q):

            if not root:

                return None 
            
            if root == p :

                return root
            
            if root == q :

                return root
            
            if root.val > p.val and root.val < q.val : 

                return root
            
            if p.val < root.val and q.val < root.val:

                return getLCA(root.left,p,q)

            if p.val > root.val and q.val > root.val:

                return getLCA(root.right,p,q)
        
        if p.val > q.val :

            return getLCA(root,q,p)
            
        return getLCA(root,p,q)