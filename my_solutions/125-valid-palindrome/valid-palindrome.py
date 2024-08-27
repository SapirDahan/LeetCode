class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Clean the string by removing non-alphabetic characters and converting it to lowercase
        cleaned = ''.join([char for char in s if char.isalnum()]).lower()
        
        # Check if the cleaned string is equal to its reverse
        return cleaned == cleaned[::-1]