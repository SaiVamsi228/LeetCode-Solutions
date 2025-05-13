# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    
    def __init__(self,root):

        self.asc_stack = []

        self.desc_stack = []

        temp1 = root

        while temp1:

            self.asc_stack.append(temp1)

            temp1 = temp1.left
        
        temp2 = root

        while temp2:

            self.desc_stack.append(temp2)

            temp2 = temp2.right
    
    def hasNext(self):

        return len(self.asc_stack) != 0
    
    def hasBefore(self):

        return len(self.desc_stack) != 0
    
    def next(self):

        if self.hasNext():

            nxt = self.asc_stack.pop()

            if nxt.right:

                temp = nxt.right

                while temp:

                    self.asc_stack.append(temp)

                    temp = temp.left
                
            return nxt
        
    def before(self):

        if self.hasBefore():

            bef = self.desc_stack.pop()

            if bef.left:

                temp = bef.left

                while temp:

                    self.desc_stack.append(temp)

                    temp = temp.right

            return bef

class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        bst_it = BSTIterator(root)

        left = bst_it.next()

        right = bst_it.before()

        while left and right:

            if left == right:

                return False

            if left.val + right.val == k:

                return True
            
            elif left.val + right.val < k :

                left = bst_it.next()
            
            elif left.val + right.val > k:

                right = bst_it.before()
        
        return False
            




