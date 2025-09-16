
class Solution: #100%
  def intToRoman(self, num: int) -> str:
    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    chars = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    numerals = ""
    for i in range(len(vals)):
      key = vals[i]
      while num >= key:
        num -= key
        numerals += chars[i]
      
    return numerals

"""
Complexity breakdown:

Outer loop = 13 iterations = O(1).

Inner loop = ≤15 iterations total = O(1).

String concatenation = at most 15 symbols = O(1).

✅ Final Time Complexity: O(1)
✅ Space Complexity: O(1)
"""
"""
Symbol	Value

I	1
V	5
X	10
L	50
C	100
D	500
M	1000
"""
