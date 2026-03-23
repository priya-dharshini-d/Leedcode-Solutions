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
