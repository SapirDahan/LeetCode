class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        # Initialize the merged intervals list
        merged = []

        # Iterate through the sorted intervals
        for interval in intervals:
            # If the merged list is empty or the current interval does not      overlap with the last interval in the merged list
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            # If the current interval overlaps with the last interval in the merged list
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        