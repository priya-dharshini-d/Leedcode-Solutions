class Solution:
    def romanToInt(self, s: str) -> int:
        # Mapping of Roman numerals to integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0       # This will store the final result
        prev_value = 0  # To keep track of the previous character's value

        # Traverse the string from right to left
        for char in reversed(s):
            current_value = roman_map[char]

            # If current value is less than the previous one, we subtract
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            # Update previous value
            prev_value = current_value

        return total

"""
# Example: s = "MCMXCIV"
# Reverse traversal: V, I, C, X, M, C, M
# V = 5 → total = 5
# I = 1 → 1 < 5 → subtract → total = 4
# C = 100 → 100 > 1 → add → total = 104
# X = 10 → 10 < 100 → subtract → total = 94
# M = 1000 → add → total = 1094
# C = 100 → 100 < 1000 → subtract → total = 994
# M = 1000 → add → total = 1994
# Final output = 1994
"""

"""    High Beats solution
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
"""
