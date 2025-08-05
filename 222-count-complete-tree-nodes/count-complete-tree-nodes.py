# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def findLeftH(node):

            lh = 0

            while node:

                lh += 1

                node = node.left
            
            return lh
        
        def findRightH(node):

            right = 0

            while node:

                right += 1

                node = node.right
            
            return right
        
        lh = findLeftH(root)

        rh = findRightH(root)

        if lh == rh :

            return 2**lh - 1
        
        left_cnt = self.countNodes(root.left)

        right_cnt = self.countNodes(root.right)

        return 1 + left_cnt + right_cnt