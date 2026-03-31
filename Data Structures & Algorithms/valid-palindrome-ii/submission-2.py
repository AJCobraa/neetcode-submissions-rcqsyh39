class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r,c=0,len(s)-1,1
        while l<r and c==1:
            if s[l]!=s[r]:
                c-=1
            else:
                l+=1
                r-=1
        if c==1:
            return True
        else:
            if self.isPalin(s[l+1:r+1]) or self.isPalin(s[l:r]):
                return True
            return False

    def isPalin(self,st)->bool:
        l,r=0,len(st)-1
        while l<r:
            if st[l]!=st[r]:
                return False
            l+=1
            r-=1
        return True
        