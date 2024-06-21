class Solution:
    def romanToInt(self, s: str) -> int:
        char_list = list(s)

        total_result = 0

        sybols_order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        last_letter = 'I'

        for char in reversed(char_list):
            if char == 'I' and sybols_order.index('I') < sybols_order.index(last_letter):
                total_result -= 1
                last_letter = 'I'

            elif char == 'X' and sybols_order.index('X') < sybols_order.index(last_letter):
                total_result -= 10
                last_letter = 'X'

            elif char == 'C' and sybols_order.index('C') < sybols_order.index(last_letter):
                total_result -= 100
                last_letter = 'C'

            elif char == 'I':
                total_result += 1
                last_letter = 'I'

            elif char == 'V':
                total_result += 5
                last_letter = 'V'

            elif char == 'X':
                total_result += 10
                last_letter = 'X'

            elif char == 'L':
                total_result += 50
                last_letter = 'L'

            elif char == 'C':
                total_result += 100
                last_letter = 'C'

            elif char == 'D':
                total_result += 500
                last_letter = 'D'

            elif char == 'M':
                total_result += 1000
                last_letter = 'M'

        return total_result

            


        