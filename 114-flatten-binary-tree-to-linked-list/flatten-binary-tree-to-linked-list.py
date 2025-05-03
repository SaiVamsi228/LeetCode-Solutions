# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        pre = []

        def getPreorder(root):

            if not root:

                return
            
            pre.append(root)

            getPreorder(root.left)

            getPreorder(root.right)
        
        getPreorder(root)

        prev = None

        for node in pre:

            node.left = None

            if prev :

                prev.right = node

            prev = node
        
        if not pre:

            return None

        return pre[0]