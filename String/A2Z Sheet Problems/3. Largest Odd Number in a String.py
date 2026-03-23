# Complexity Analysis
# Time Complexity: O(N), since the loop runs once through the string of length N.
# Space Complexity: O(1), as we are using only a constant amount of extra space.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx=-1 #This will store the index of last odd digit

        for i in range(len(num)-1,-1,-1): #raverse from RIGHT → LEFT
            if int(num[i])%2==1: #Check for odd digit
                idx=i            #Store index
                break            #Stop at first odd digit from right (num = "0214638") (3 → idx = 5)

        i=0                      #Skip zeros at beginning
        
        while i<=idx and num[i]=="0":
            i+=1
        return num[i:idx+1]      #Extract substring
