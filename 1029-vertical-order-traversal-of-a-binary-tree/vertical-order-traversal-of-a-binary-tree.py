from heapq import heappush, heappop, heapify
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:

            return []

        hp = []

        heapify(hp)

        q = deque()

        rn, cn = 0,0

        q.append((root,cn,rn))

        while q:

            node,cn,rn = q.popleft()

            heappush(hp,(cn,rn,node.val))

            if node.left:

                q.append((node.left,cn-1,rn+1))
            
            if node.right:

                q.append((node.right,cn+1,rn+1))
        
        vert_ord_trav = []

        prev_hori_level = None

        my_vert_ord_level = []

        while hp:

            hori_dist, level, node_val = heappop(hp)

            if prev_hori_level == None:

                my_vert_ord_level.append(node_val)

                prev_hori_level = hori_dist

            elif hori_dist == prev_hori_level:

                my_vert_ord_level.append(node_val)
            
            else:

                vert_ord_trav.append(my_vert_ord_level)

                prev_hori_level = hori_dist

                my_vert_ord_level = []

                my_vert_ord_level.append(node_val)
        

        if my_vert_ord_level :

            vert_ord_trav.append(my_vert_ord_level)
        
            my_vert_ord_level = []
        
        return vert_ord_trav
            

