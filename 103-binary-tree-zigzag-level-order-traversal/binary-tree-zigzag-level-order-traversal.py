# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level_ord = []

        if not root:

            return level_ord

        q = deque()

        q.append(root)

        rev = False

        while q :

            n = len(q)

            level = [0 for i in range(n)]

            for i in range(n):

                cur_node = q.popleft()

                if rev == False:
                    
                    level[i] = cur_node.val
                
                else:

                    level[n-i-1] = cur_node.val

                if cur_node.left:

                    q.append(cur_node.left)
                
                if cur_node.right :

                    q.append(cur_node.right)

            level_ord.append(level)

            rev = ~rev
        
        return level_ord