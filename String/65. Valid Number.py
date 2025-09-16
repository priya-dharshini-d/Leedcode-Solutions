"""
The function checks if a given string S is a valid number by scanning character by character.

Four boolean flags are used:

num → Have we seen at least one digit so far?

exp → Have we seen an exponent (e/E)?

sign → Have we seen a sign (+/-) in the current section?

dec → Have we seen a decimal point (.)?
"""

class Solution:      #100% Beats
    
    def isNumber(self, S: str) -> bool:    
        num, exp, sign, dec = False, False, False, False
        for c in S:
            if c >= '0' and c <= '9': 
                num = True     
            elif c == 'e' or c == 'E':
                if exp or not num: 
                    return False
                else: 
                    exp, num, sign, dec = True, False, False, False
            elif c == '+' or c == '-':
                if sign or num or dec: 
                    return False
                else: 
                    sign = True
            elif c == '.':
                if dec or exp: 
                    return False
                else: 
                    dec = True
            else: 
                return False
        return num

#100% Beats
"""
⏱ Complexity Analysis

Time Complexity: O(n), where n = len(S) → we scan the string once.
Space Complexity: O(1) → only four boolean flags used.

"""

