from typing import List
import bisect

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit into a list of tuples and sort them
        jobs = sorted(zip(difficulty, profit))
        
        # Create a list to store the maximum profit up to each difficulty level
        max_profit = [0] * len(jobs)
        max_profit[0] = jobs[0][1]
        
        # Fill the max_profit array
        for i in range(1, len(jobs)):
            max_profit[i] = max(max_profit[i - 1], jobs[i][1])
        
        # Sort the worker list
        worker.sort()
        
        total_profit = 0
        j = 0
        
        # Assign the best possible job to each worker
        for ability in worker:
            # Use binary search to find the highest difficulty the worker can handle
            while j < len(jobs) and ability >= jobs[j][0]:
                j += 1
            if j > 0:
                total_profit += max_profit[j - 1]
        
        return total_profit
