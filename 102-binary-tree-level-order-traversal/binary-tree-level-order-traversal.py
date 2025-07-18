# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()

        q.append(root)

        ans = []

        if not root:

            return ans

        while q:

            n = len(q)

            level = []

            for _ in range(n):

                node = q.popleft()

                level.append(node.val)

                if node.left:

                    q.append(node.left)
                
                if node.right :

                    q.append(node.right)
                
            
            ans.append(level)
        
        return ans