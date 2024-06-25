class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Split by " "
        words = s.split()

        # If no words exists
        if not words:
            return 0 

        # Return the length of the last word
        return len(words[-1])
        