class Solution:
    def isValid(self, s: str) -> bool:

        # Create stack
        stack = []

        opening_brackets = {'(', '[', '{'}

        for i in range(0, len(s)):

            if s[i] in opening_brackets:
                stack.append(s[i])

            elif len(stack) == 0:
                return False
            
            elif stack[-1] == '(' and s[i] == ')':
                # Remove it from the stack
                stack.pop()

            elif stack[-1] == '[' and s[i] == ']':
                # Remove it from the stack
                stack.pop()

            elif stack[-1] == '{' and s[i] == '}':
                # Remove it from the stack
                stack.pop()

            else:
                return False

        if len(stack) != 0:
            return False
        
        return True




        