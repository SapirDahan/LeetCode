# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # Call help function
        return self.helpFunc(root.right, root.left)



    def helpFunc(self, rootR: Optional[TreeNode], rootL: Optional[TreeNode]) -> bool:

        # If both nodes empty
        if not rootR and not rootL:
            return True

        # If only one node is empty
        if not rootR or not rootL:
            return False

        # checking symmetric
        return rootR.val == rootL.val and self.helpFunc(rootR.left, rootL.right) and self.helpFunc(rootR.right, rootL.left)

        

        
        