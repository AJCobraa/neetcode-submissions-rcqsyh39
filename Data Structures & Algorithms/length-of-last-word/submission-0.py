class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=len(s)-1
        c=0
        while s[r]==" ":
            r-=1
        while r>=0 and s[r]!=" ":
            c+=1
            r-=1
        return c
        