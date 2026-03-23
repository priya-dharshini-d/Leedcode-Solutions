# Time Complexity: O(N * log N + M), where N is the number of strings and M is the minimum length of a string. 
# The sorting operation takes O(N * log N) time, and the comparison of characters in the first and last strings takes O(M) time.
# Space Complexity: O(M), as the ans variable can store the length of the prefix which in the worst case will be O(M).

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:     # Handle empty list case
            return ""
        
        strs.sort()      # Sort the list lexicographically
        
        first = strs[0]
        last = strs[-1]
        
        ans = []             # Store the common prefix characters
        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:    # Stop if characters differ
                return ''.join(ans)

            ans.append(first[i])       # Add matching character to result
        
        return ''.join(ans)            # Return the longest common prefix
