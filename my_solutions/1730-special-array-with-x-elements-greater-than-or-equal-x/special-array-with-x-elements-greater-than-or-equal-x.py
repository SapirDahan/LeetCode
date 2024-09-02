class Solution:
    def specialArray(self, nums: List[int]) -> int:

        # Sort nums
        nums.sort()

        # The previous number, at first we will put -1
        prev = -1

        # Loop over the array
        for i in range(len(nums)):
            x = len(nums) - i
            if nums[i] >= x:
                if i == 0 or nums[i-1] < x:
                    return x

            prev = nums[i]

        # There is no such x
        return -1