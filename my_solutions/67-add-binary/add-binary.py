class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the result and carry
        result = []
        carry = 0
        
        # Pointers for a and b starting from the last character
        i, j = len(a) - 1, len(b) - 1
        
        # Loop until both strings are processed or carry exists
        while i >= 0 or j >= 0 or carry:
            
            # Get the current digit from both strings, if index is valid
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum of both bits and the carry
            total = bit_a + bit_b + carry
            
            # Append the result of total % 2 (either 0 or 1) to result
            result.append(str(total % 2))
            
            # Update carry (either 0 or 1)
            carry = total // 2
            
            # Move to the previous digits
            i -= 1
            j -= 1
        
        # The result list is in reverse order, so we reverse it before joining
        return ''.join(result[::-1])