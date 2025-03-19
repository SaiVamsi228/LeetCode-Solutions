# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def get_is_same_tree(p,q) -> bool:

            if p == None and q == None:

                return True
            
            if (p and not q) or (not p and q):

                return False
            
            left = get_is_same_tree(p.left, q.left)

            right = get_is_same_tree(p.right, q.right)

            if left and right and p.val == q.val :

                return True
            
            return False

        return get_is_same_tree(p,q)
