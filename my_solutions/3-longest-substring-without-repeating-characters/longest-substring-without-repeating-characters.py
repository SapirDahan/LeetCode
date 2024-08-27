class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Dictionary to store the last seen index of each character
        char_index = {}

        # Initialize the starting point of the current window and max length
        left = 0
        max_length = 0

        # Loop through the string
        for right in range(len(s)):

            # If the character is already in the dictionary and within the current window
            if s[right] in char_index and char_index[s[right]] >= left:
                
                # Move the left pointer to the right of the previous occurrence of the character
                left = char_index[s[right]] + 1

            # Update the last seen index of the character
            char_index[s[right]] = right

            # Calculate the current length of the substring and update max_length
            max_length = max(max_length, right - left + 1)

        return max_length