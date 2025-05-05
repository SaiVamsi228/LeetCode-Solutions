# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def connect_all(p, q):
            # Base case: if either node is a leaf (no children), stop
            if (p.left is None and p.right is None) or (q.left is None and q.right is None):
                return 

            # Connect children within the left subtree
            connect_all(p.left, p.right)

            # Connect children within the right subtree
            connect_all(q.left, q.right)

            # Connect the right child of the left subtree to the left child of the right subtree
            connect_all(p.right, q.left)

            # Wire the next pointers between adjacent nodes
            p.left.next = p.right      # Connect left->right within left subtree
            q.left.next = q.right      # Connect left->right within right subtree
            p.right.next = q.left      # Connect across subtrees

        # Edge case: empty tree
        if not root:
            return root

        # Start the connection process from the two children of root
        if root.left and root.right:
            connect_all(root.left, root.right)
            root.left.next = root.right  # Initial connection between root's children

        return root
