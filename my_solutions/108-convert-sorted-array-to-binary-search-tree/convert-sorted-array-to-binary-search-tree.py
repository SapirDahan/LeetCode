class Solution(object):
    def sortedArrayToBST(self, nums):
        
        # Base condition
        if len(nums) == 0:
            return None

        # set the middle node
        mid = len(nums) // 2

        # Initialise root node with value same as nums[mid]
        root = TreeNode(nums[mid])

        # Assign left subtrees as the same function called on left subranges
        root.left = self.sortedArrayToBST(nums[:mid])

        # Assign right subtrees as the same function called on right subranges
        root.right = self.sortedArrayToBST(nums[mid+1:])

        # Return the root node
        return root