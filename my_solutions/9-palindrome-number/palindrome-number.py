class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Cast the integer to string
        x_str = str(x)
        
        # Reversed the string
        x_str_reversed = x_str[::-1]

        # If x is a polindrom then it should be equal to the reversed form
        if x_str == x_str_reversed:
            return True

        # x is not a polindrom
        return False

        