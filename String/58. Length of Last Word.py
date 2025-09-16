class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove leading/trailing spaces, then split by whitespace
        words = s.strip().split()
        # Return the length of the last word
        return len(words[-1])
"""
s.strip() → removes leading & trailing spaces.

Complexity: O(n) (scans entire string once).

split() → splits into words.

Complexity: O(n) (again scans string).

Indexing words[-1] → O(1).

len(last_word) → O(k), where k is length of the last word (≤ n).

✅ Complexity:

Time: O(n)

Space: O(n) (storing list of words).

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        res = 0
        for i in range(len(s)-1, -1, -1):   # iterate from end to start
            if s[i] == " " and count == 0:
                pass                        # skip trailing spaces
            elif s[i] == " " and count != 0:
                break                       # stop when a space is found after counting
            else:
                count += 1                  # count characters of the last word
        return count

"""
Time Complexity

The loop runs at most n times (where n = len(s)).

Each step is O(1) work (comparisons, increments).

Total: O(n).

Space Complexity

Only a few variables (count, res, i).

Total: O(1).

"""
