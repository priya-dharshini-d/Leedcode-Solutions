class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output=""
        level=0

        for ch in s:
            if ch=="(":
                if level>0:        # IF We are inside a primitive
                    output+=ch
                level+=1           # Increase the nesting level for '('
            elif ch==")":
                level-=1           # Decrease the nesting level for ')'
                if level>0:        # If we're inside a primitive, add ')' to result
                    output+=ch
                
        return output
