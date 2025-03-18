# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        hp = []

        heapify(hp)

        q = deque()

        cur_node, cur_level, hori_dist = root, 0, 0

        q.append((cur_node,cur_level + 1, hori_dist - 1))

        while q:

            cur_node, cur_level, hori_dist = q.popleft()

            heappush(hp, (hori_dist, cur_level , cur_node.val))

            if cur_node.left:

                q.append((cur_node.left,cur_level + 1, hori_dist - 1))
            
            if cur_node.right:

                q.append((cur_node.right, cur_level + 1, hori_dist + 1))
            
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
                



                

        