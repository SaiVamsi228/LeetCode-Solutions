# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        mx = 0

        def getHeightAndMX(node):

            nonlocal mx

            if node == None:

                return 0
            
            lh = getHeightAndMX(node.left)

            rh = getHeightAndMX(node.right)

            max_ht_possible_here = lh + rh 

            mx = max(mx, max_ht_possible_here)

            return 1 + max(lh,rh)
        
        getHeightAndMX(root)

        return mx
        