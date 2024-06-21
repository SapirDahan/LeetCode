class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        # Iterate through the list of numbers
        for i in range(len(nums)):
            
            # Iterate through the remaining numbers in the list, starting from the current index
            for j in range(i + 1, len(nums)):
               
                # Check if the sum of the current two elements equals the target
                if nums[i] + nums[j] == target:
                    
                    # If so, return the indices of the two elements
                    return [i, j]
        
        # If no such pair is found, return an empty list
        return []
