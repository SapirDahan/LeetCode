class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Check if the length of needle is 0
        if len(needle) == 0:
            return -1

        # Check if needle is longer then haystack
        if len(needle) > len(haystack):
            return -1

        # Use sliding window
        for i in range(0, (len(haystack) - len(needle) + 1)):
            for j in range(0, len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                elif j == (len(needle) - 1):
                    return i
        
        # Needle was not found
        return -1
        