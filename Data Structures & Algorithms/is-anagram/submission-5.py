class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.Ana(s)==self.Ana(t)

    def Ana(self,s):
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        return d

        