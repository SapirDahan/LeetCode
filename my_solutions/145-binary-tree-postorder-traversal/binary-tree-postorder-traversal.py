# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # The postorder
        postorder = []

        # Call rrecursive method
        self.postorderTraversalRec(root, postorder)

        # Return the post order traversal
        return postorder

    def postorderTraversalRec(self, root: Optional[TreeNode], postorder: List[int]):

        # If the root node is not empty do the traversal
        if root:
            self.postorderTraversalRec(root.left, postorder)
            self.postorderTraversalRec(root.right, postorder)
            postorder.append(root.val)


        