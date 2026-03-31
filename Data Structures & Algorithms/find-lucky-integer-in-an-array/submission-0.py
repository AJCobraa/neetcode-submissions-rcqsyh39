class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        m=-1
        for i in arr:
            d[i]=d.get(i,0)+1

        for k,v in d.items():
            if k==v:
                m=max(m,k)
        return m
        