class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=self.dct(s)
        b=self.dct(t)
        return a==b
    def dct(self, s: str) -> dict:  
        d={}  
        for i in s:
            d[i]=d.get(i,0)+1
        return d
    
        
        
    