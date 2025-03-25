# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        node = root

        while node and ((p.val < node.val and q.val < node.val) or (p.val > node.val and q.val > node.val)):

            if p.val < node.val:

                node = node.left
            
            else:

                node = node.right
        
        return node