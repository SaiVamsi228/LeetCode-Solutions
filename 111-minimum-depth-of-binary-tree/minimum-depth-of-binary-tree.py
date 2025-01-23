# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()

        node, depth = root, 1

        q.append((node,depth))

        if not root:

            return 0

        while q :

            cur_node, cur_depth = q.popleft()

            if cur_node.left == None and cur_node.right == None:

                return cur_depth
            
            if cur_node.left: 

                q.append((cur_node.left,cur_depth + 1))

            if cur_node.right: 

                q.append((cur_node.right,cur_depth + 1))
        
        return 0