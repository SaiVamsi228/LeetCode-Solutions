# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildHeightBalancedBST(nums):

            if not nums:

                return
            
            n = len(nums)

            mid = n//2

            root = nums[mid]

            root = TreeNode(root)

            root.left = buildHeightBalancedBST(nums[:mid])

            root.right = buildHeightBalancedBST(nums[mid+1:])

            return root
        
        return buildHeightBalancedBST(nums)