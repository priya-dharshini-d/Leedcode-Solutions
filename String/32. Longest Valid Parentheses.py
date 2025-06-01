class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_so_far = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_so_far = max(max_so_far,i - stack[-1])
        return max_so_far

# 97.78%

"""

"""
