class Solution:
    def scoreOfString(self, s: str) -> int:
        l,r=0,1
        sums=0
        while r<len(s):
            o=abs(ord(s[l])-ord(s[r]))
            sums+=o
            l+=1
            r+=1
        return sums
        