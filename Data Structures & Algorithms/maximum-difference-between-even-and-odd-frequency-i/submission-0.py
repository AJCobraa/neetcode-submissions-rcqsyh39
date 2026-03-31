class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        mo=[]
        me=[]
        for k,v in d.items():
            if v%2==0:
                me.append(v)
            else:
                mo.append(v)
        return max(mo)-min(me)