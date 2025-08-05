# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        cur = root

        inord = []

        while cur:

            if cur.left:

                temp = cur.left

                while temp.right and temp.right != cur:

                    temp = temp.right
                
                if temp.right == None:

                    temp.right = cur

                    cur = cur.left
                
                else:

                    inord.append(cur.val)

                    temp.right = None

                    cur = cur.right
            
            else:

                inord.append(cur.val)

                cur = cur.right
        
        return inord


