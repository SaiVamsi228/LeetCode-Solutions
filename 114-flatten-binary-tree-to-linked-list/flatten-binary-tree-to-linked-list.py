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

        def getFlattenedTree(root):

            if not root:

                return None

            if root.left == None and root.right == None:

                return root
            
            cur = root

            flattened_right_subtree = getFlattenedTree(root.right)

            flattened_left_subtree = getFlattenedTree(root.left)

            if flattened_left_subtree:

                cur.right = flattened_left_subtree
                
                temp = cur.right

                while temp.right:

                    temp = temp.right
                
                temp.right = flattened_right_subtree
            
            else:

                cur.right = flattened_right_subtree

            cur.left = None

            return cur
        

        return getFlattenedTree(root)
            

        