class Solution:
    def isPalindrome(self, s: str) -> bool:

        str_original = ""
        str_reversed = ""

        # Append the chars accordingly in the new strings
        for i in range(0, len(s)):
            if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9':
                str_original += s[i].lower()
                str_reversed = s[i].lower() + str_reversed

        if str_original == str_reversed:
            return True
        
        return False

        