class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Go in reversed order
        for i in range(len(digits) - 1, -1, -1):

            # If not 9 then add 1 and finnish
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits

            else:
                digits[i] = 0
        
        # Append the number with 1
        digits.insert(0, 1)

        return digits
        