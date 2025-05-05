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
        
        def connect_all(p,q):

            if p.left == None and p.right == None or (q.left == None and q.right == None):

                return 
            
            connect_all(p.left,p.right)

            connect_all(q.left,q.right)

            connect_all(p.right,q.left)

            p.left.next = p.right

            q.left.next = q.right

            p.right.next = q.left

            return 


        if not root:

            return root

        if root.left and root.right:

            connect_all(root.left,root.right)
            
            root.left.next = root.right 

        return root