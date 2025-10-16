# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def buildBST(l,r):

            if l > r:

                return None
            
            cur_node = TreeNode(preorder[l])

            if l == r:

                return cur_node
            
            part_ind = r + 1
            
            for i in range(l+1,r+1):

                if preorder[i] > preorder[l]:

                    part_ind = i

                    break

            cur_node.left = buildBST(l+1,part_ind-1)

            cur_node.right = buildBST(part_ind,r)

            return cur_node
        
        return buildBST(0,len(preorder) - 1)
            