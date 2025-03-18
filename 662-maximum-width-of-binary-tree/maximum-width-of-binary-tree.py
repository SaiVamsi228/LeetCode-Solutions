# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = deque()

        node, index = root, 1

        q.append((node,index))

        maxi_width = 1

        while q:

            n = len(q)

            first_seen_ind , last_seen_ind = -1 , -1

            for _ in range(n):

                cur_node, index = q.popleft()

                if first_seen_ind == -1:

                    first_seen_ind = index
                
                last_seen_ind = index

                if cur_node.left:

                    q.append((cur_node.left, 2 * index))
                
                if cur_node.right:

                    q.append((cur_node.right, 2*index + 1))

            if first_seen_ind != -1 :
                
                maxi_width = max(maxi_width,last_seen_ind - first_seen_ind + 1)
        
        return maxi_width





