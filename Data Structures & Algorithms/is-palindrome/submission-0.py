class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l,r=0,len(s)-1
        while l<r:
            
            while l<r and not self.isAlphanum(s[l]):
                l+=1
            while r>l and not self.isAlphanum(s[r]):
                r-=1
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
            
    def isAlphanum(self,s: str)-> bool:
        if (ord(s)<=ord("z") and ord(s)>=ord("a")) or (ord(s)<=ord("9") and ord(s)>=ord("0")):
            return True
        return False       