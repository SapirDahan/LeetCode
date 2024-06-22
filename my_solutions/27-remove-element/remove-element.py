class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        counter = 0

        # Go over all the elements in nums
        for i in range(0, len(nums)):

            # If it not equal to val then insert it to nums in the correct place
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
            
        # Change nums    
        nums[:] = nums[:counter]

        # Return counter
        return counter

        