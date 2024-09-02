class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(len(nums)):
            x = len(nums) - i
            if nums[i] >= x:
                if i == 0 or nums[i-1] < x:
                    return x
        
        return -1