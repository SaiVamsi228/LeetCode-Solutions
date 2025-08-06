# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def buildTreeAndGetRoot(pre_start,pre_end): # this will return the root given start and end indices

            if pre_start > pre_end:

                return None
            
            cur_root = TreeNode(preorder[pre_start])

            num_left = 0

            low = pre_start + 1

            high = pre_end

            while low <= high:

                mid = (low + high)//2
                
                if preorder[mid] < cur_root.val:

                    low = mid + 1
                
                else:

                    high = mid - 1
            
            num_left = high - pre_start

            cur_root.left = buildTreeAndGetRoot(pre_start+1,pre_start + num_left)

            cur_root.right = buildTreeAndGetRoot(pre_start+num_left+1,pre_end)

            return cur_root
        

        root = buildTreeAndGetRoot(0,len(preorder)-1)

        return root

