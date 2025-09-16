
class Solution:  #Complexity wise 1 st
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
Works in O(n) time, O(1) space.
"""



class Solution:#This is best
    
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50,
                 'C':100, 'D':500, 'M':1000}
        
        result = 0
        for i in range(len(s)):
            curr = roman[s[i]]
            next_val = roman[s[i+1]] if i+1 < len(s) else 0 #if i+1 < len(s) → check if there is a next character.
            
            if curr < next_val:
                result -= curr
            else:
                result += curr
        
        return result

"""
s = "MCMXCIV"
(expected output = 1994)

Roman Numeral Rules Reminder:

Normally add values: M = 1000, C = 100, X = 10, I = 1

But if a smaller number comes before a bigger one → subtract rule
(like IV = 4, IX = 9, XL = 40, CM = 900).

""""



"""

⏱ Complexity Analysis

Time Complexity:

We loop once through all characters of s.

Each step does constant work (dictionary lookup + comparison + addition/subtraction).

O(n) where n = len(s).


Space Complexity:

Dictionary roman is fixed (7 entries, independent of input).

A few variables (curr, next_val, result).

So O(1) (constant extra space).
"""
