class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Start with the first word
        result = strs[0]

        # Go over the works in the list
        for word in strs:

            result_copy = result
            result = ""

            # Find the largest prefix
            for i in range(0, len(word)):
                if len(result_copy) > i and word[i] == result_copy[i]:
                    result += word[i]
                else:
                    break

        # Return the result
        return result
        