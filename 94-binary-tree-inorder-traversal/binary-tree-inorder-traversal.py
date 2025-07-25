# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def get_inorder(root):

            if not root:

                return 
            
            get_inorder(root.left)

            ans.append(root.val)

            get_inorder(root.right)
        
        get_inorder(root)

        return ans

         
        