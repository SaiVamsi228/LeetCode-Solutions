# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:

            return None

        if len(preorder) == 1:

            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])

        root_ind = inorder.index(preorder[0])

        no_ele_on_left = root_ind

        root.left = self.buildTree(preorder[1:root_ind+1],inorder[:root_ind])

        root.right = self.buildTree(preorder[root_ind+1:], inorder[root_ind+1:])

        return root