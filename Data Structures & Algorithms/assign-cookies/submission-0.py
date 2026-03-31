class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s=sorted(s)
        g=sorted(g)
        l,r=0,0
        while l<len(g) and r<len(s):
            if g[l]<=s[r]:
                l+=1
                r+=1
            else:
                r+=1
        return l
        