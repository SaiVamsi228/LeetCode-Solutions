# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        string_format = []

        q = deque()

        q.append(root)

        while q :

            node = q.popleft()

            if node == None:

                string_format.append("#,")
            
            else:

                string_format.append(str(node.val)+",")

                q.append(node.left)

                q.append(node.right)
        
        serialised_tree = "".join(string_format)

        print(serialised_tree)

        return serialised_tree
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        tokens = data.split(",")

        tokens = deque(tokens)

        q = deque()
        
        if tokens[0] == "#":

            return None

        root = TreeNode(int(tokens.popleft()))

        q.append(root)

        while q :

            node = q.popleft()

            left_val = tokens.popleft()

            if left_val != "#":

                left_node = TreeNode(int(left_val))

                node.left = left_node

                q.append(left_node)
            
            right_val = tokens.popleft()

            if right_val != "#":

                right_node = TreeNode(int(right_val))

                node.right = right_node

                q.append(right_node)
        
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))