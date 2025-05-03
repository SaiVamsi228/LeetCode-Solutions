# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder:

            return None
        
        if len(inorder) == 1:

            return TreeNode(inorder[0])

        root = postorder[-1]

        no_ele_on_left = inorder.index(root)

        root = TreeNode(root)

        root.left = self.buildTree(inorder[:no_ele_on_left], postorder[:no_ele_on_left])


        root.right = self.buildTree(inorder[no_ele_on_left+1:], postorder[no_ele_on_left:-1])

        return root