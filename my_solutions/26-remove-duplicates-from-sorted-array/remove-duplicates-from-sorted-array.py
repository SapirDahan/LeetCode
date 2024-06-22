class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1  # Start from the second position since the first element is always unique

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        # Optionally, slice the list to keep only the first k elements
        nums[:] = nums[:k]
        
        return k
