# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def f(pre):

            if len(pre) == 0:

                return None
            
            if len(pre) == 1:

                return TreeNode(pre[0])

            root = TreeNode(pre[0])

            for i in range(1,len(pre)):

                if pre[i] > pre[0]:

                    break
            else:

                i = len(pre) # when we find no elements which are greater

            root.left = f(pre[1:i])

            root.right = f(pre[i:])

            return root
        
        # print(preorder)

        return f(preorder)