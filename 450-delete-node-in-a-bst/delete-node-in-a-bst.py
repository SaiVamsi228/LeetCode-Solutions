# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def s_and_d(node,key):

            if not node:

                return None
            
            if key < node.val:

                node.left = s_and_d(node.left,key)
            
            elif key > node.val:

                node.right = s_and_d(node.right,key)
            
            elif key == node.val:

                if node.left == None and node.right == None:
                    return None
                
                if node.left and node.right:

                    temp = node.right

                    while temp.left:

                        temp = temp.left
                    
                    temp.left = node.left

                    return node.right
                
                elif node.left:

                    return node.left
                
                elif node.right:

                    return node.right
            
            return node
        
        return s_and_d(root,key)


        

        
