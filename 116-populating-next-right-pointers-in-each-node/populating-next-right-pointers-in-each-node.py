"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        q = deque()

        if not root:

            return root

        q.append(root)

        while q :
            
            prev = None

            n = len(q)

            for i in range(n):

                cur = q.popleft()

                if cur.left:

                    q.append(cur.left)
                
                if cur.right:

                    q.append(cur.right)

                if prev:

                    prev.next = cur

                prev = cur
        
        
        return root


