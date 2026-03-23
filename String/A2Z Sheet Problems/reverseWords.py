#BRUTE FORCE  

#Time Complexity: O(N),We traverse the string once to collect words (O(N)) and once more to reverse and join them (O(N)). Hence total time is O(N).
#Space Complexity: O(N),We store all words in a separate list/array, requiring extra space proportional to the number of characters.

class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        word=""

        for ch in s:
            if ch!=" ":
                word+=ch
            elif word:     # Only add non-empty words
                words+=[word]
                word=""

        if word:           # Add the last word if present
            words+=[word]

        return " ".join(words[::-1])

# OPTIMAL SOLUTION: Two Pointer / Reverse Traversal Approach
# Time Complexity: O(N), We traverse the string once from right to left and construct the result directly without extra passes.
# Space Complexity: O(1),Ignoring the output string, no additional data structures proportional to input size are used.

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        i = len(s) - 1

        while i >= 0: #Continue until we scan the whole string
            while i >= 0 and s[i] == " ":  #trailing spaces and multiple spaces
                i -= 1

            if i < 0: #If no characters left: break
                break

            end = i  #Mark the last index of current word

            while i >= 0 and s[i] != " ": # Move left until: space OR beginning
                i -= 1

            word = s[i + 1:end + 1]       # Slice gives the word

            if result:                    # Add space if needed (No extra space at start)
                result += " "

            result += word                # Add word to result

        return result
