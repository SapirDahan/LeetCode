class Solution:
    def scoreOfString(self, s: str) -> int:

        # The score
        score = 0

        # Looping over the pairs
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))

        # Return the score
        return score
            
        