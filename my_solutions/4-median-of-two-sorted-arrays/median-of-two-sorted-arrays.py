class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays
        merged = []
        i, j = 0, 0
        
        # Use two pointers to merge the arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Append the remaining elements from nums1 or nums2
        if i < len(nums1):
            merged.extend(nums1[i:])
        if j < len(nums2):
            merged.extend(nums2[j:])
        
        # Find the median of the merged sorted array
        n = len(merged)
        if n % 2 == 1:
            # If odd, return the middle element
            return float(merged[n // 2])
        else:
            # If even, return the average of the two middle elements
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0