# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:

            return TreeNode(val)
        
        cur = root

        last_pos = root

        while cur:

            last_pos = cur

            if val < cur.val:

                cur = cur.left
            
            elif val > cur.val:

                cur = cur.right
        
        if val > last_pos.val :

            last_pos.right = TreeNode(val)
        
        else:

            last_pos.left = TreeNode(val)
            
        return root


