class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Initialize two pointers, one at the start and one at the end
        left = 0
        right = int(c ** 0.5)  # The maximum possible value of i^2 is c, so the maximum value of i is sqrt(c)

        while left <= right:
            square_sum = left ** 2 + right ** 2

            if square_sum == c:
                return True
            elif square_sum < c:
                left += 1  # Increase the left pointer to increase the sum
            else:
                right -= 1  # Decrease the right pointer to decrease the sum

        return False
