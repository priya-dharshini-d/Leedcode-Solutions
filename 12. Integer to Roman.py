class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = ""
        storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                Roman += storeIntRoman[i][1]
                num -= storeIntRoman[i][0]
        return Roman


"""
Suppose num = 58.

Start with 1000 ("M"): 58 < 1000 → skip.

900 ("CM"): 58 < 900 → skip.

500 ("D"): 58 < 500 → skip.

400 ("CD"): skip.

100 ("C"): skip.

90 ("XC"): skip.

50 ("L"): 58 >= 50 → add "L" to Roman, subtract 50 → num = 8

40 ("XL"): 8 < 40 → skip.

10 ("X"): 8 < 10 → skip.

9 ("IX"): 8 < 9 → skip.

5 ("V"): 8 >= 5 → add "V", subtract 5 → num = 3

4 ("IV"): 3 < 4 → skip.

1 ("I"): 3 >= 1 → add "I", subtract 1 → num = 2

Loop repeats for "I" until num is zero, adding "III".

Final Roman numeral: "LVIII"

"""
