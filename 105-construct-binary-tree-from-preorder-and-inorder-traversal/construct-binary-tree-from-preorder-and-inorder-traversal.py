# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def getRoot(pre_start,pre_end,in_start, in_end):

            if pre_start > pre_end or in_start > in_end :

                return None
            
            cur_root = TreeNode(preorder[pre_start])
            
            pivot_ind = mp[preorder[pre_start]]

            cnt = pivot_ind - in_start

            cur_root.left = getRoot(pre_start+1,pre_start + cnt, in_start, pivot_ind - 1 )

            cur_root.right = getRoot(pre_start+cnt+1,pre_end, pivot_ind + 1, in_end)

            return cur_root
        
        n = len(preorder)

        mp = {inorder[i]: i for i in range(n)}

        return getRoot(0,n-1,0,n-1)