"""
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution: # 56.98%
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        lis = []

        for i in range(max_len):
            if i < len(word1):
                lis.append(word1[i])
            if i < len(word2):
                lis.append(word2[i])

        return "".join(lis)
      
"""
Complexity Analysis:

Time Complexity:

Loop runs max(n, m) times → O(max(n, m))

Each iteration appends at most 2 characters.

"".join(lis) → O(n + m)

✅ Overall: O(n + m)


Space Complexity:

lis stores all characters from both strings → O(n + m)

✅ Space: O(n + m)
"""


class Solution: #89.66%
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for a, b in zip(word1, word2):  #[('a','p'), ('b','q'), ('c','r')]
            merged.append(a + b)        #merged = ["ap", "bq", "cr"]
        
        merged.append(word1[len(word2):])  #Leftover from word1  - ""
        merged.append(word2[len(word1):])  #Leftover from word2   - "st"

        return "".join(merged)

"""
Complexity Analysis:

Time Complexity:

Loop over zip(word1, word2) → O(min(n, m))

Append leftover slices: O(n - m) or O(m - n)

"".join(merged) → O(n + m)

✅ Overall: O(n + m), where n = len(word1), m = len(word2)


Space Complexity:

merged list stores about n + m characters.

✅ O(n + m) additional space.

"""
