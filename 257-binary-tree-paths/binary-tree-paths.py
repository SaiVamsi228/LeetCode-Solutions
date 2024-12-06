# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def getPaths(root,path):

            if root.left == None and root.right == None:

                ans.append("".join(path))

                return 
            
            if root.left:

                path.append("->")

                path.append(str(root.left.val))

                getPaths(root.left,path)

                path.pop()

                path.pop()
            
            if root.right:

                path.append("->")

                path.append(str(root.right.val))

                getPaths(root.right,path)

                path.pop()

                path.pop()
        
        path = [str(root.val)]

        getPaths(root,path)

        return ans

