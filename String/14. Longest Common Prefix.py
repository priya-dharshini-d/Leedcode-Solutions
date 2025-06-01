class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 


"""
#100% Beats

Example: v = ["flower", "flow", "flight"]

1. Sort the list:
   v = ["flight", "flow", "flower"]

2. Take the first and last strings:
   first = "flight"
   last = "flower"

3. Compare characters one by one up to the length of the shorter string:
   Index 0: 'f' == 'f' → ans = "f"
   Index 1: 'l' == 'l' → ans = "fl"
   Index 2: 'i' != 'o' → mismatch found, stop here

4. Return ans = "fl"

Explanation:
- Sorting ensures the first and last strings differ the most.
- Longest common prefix of the entire list is the common prefix between these two.
- Comparing them character-by-character finds the prefix "fl".
- This prefix applies to the whole list.

Result: "fl"

"""
