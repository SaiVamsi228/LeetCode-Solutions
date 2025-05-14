from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone_hm = {}  # original node -> cloned node
        q = deque([node])
        clone_hm[node] = Node(node.val)

        while q:
            cur_node = q.popleft()

            for neighbor in cur_node.neighbors:
                if neighbor not in clone_hm:
                    # Clone the neighbor
                    clone_hm[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                # Append the cloned neighbor to the cloned current node
                clone_hm[cur_node].neighbors.append(clone_hm[neighbor])

        return clone_hm[node]
