class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while end >= start:

            #Find the middle index
            middle = (start + end) // 2

            # Check if we found the target
            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                start = middle + 1

            if nums[middle] > target:
                end = middle - 1

        # we didn't found the target but it should be inserted at the start index
        return start

    
        