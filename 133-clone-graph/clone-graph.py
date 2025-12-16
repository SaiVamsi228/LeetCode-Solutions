from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            
            return node
            
        old_mp = {}

        q = deque()

        q.append(node)
        
        main_node = node

        while q:

            node = q.popleft()
            
            old_mp[node.val] = []
            
            for neighbour in node.neighbors:
                
                old_mp[node.val].append(neighbour.val)
            
                if neighbour.val not in old_mp:
                    
                    q.append(neighbour)
        
        new_mp = {} # val: address
        
        for node,neighbours in old_mp.items():
            
            if node not in new_mp:
                
                new_mp[node] = Node(node,[])
                
            for neighbour in neighbours:
                
                if neighbour not in new_mp:
                    
                    new_mp[neighbour] = Node(neighbour,[])
                    
                if new_mp[neighbour] not in new_mp[node].neighbors:
                    new_mp[node].neighbors.append(new_mp[neighbour])
                
                if new_mp[node] not in new_mp[neighbour].neighbors:
                    new_mp[neighbour].neighbors.append(new_mp[node])                

        return new_mp[main_node.val]