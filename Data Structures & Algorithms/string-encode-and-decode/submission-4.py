class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            l=str(len(s))
            res=res+"$"+l+"$"+s
        return res


    def decode(self, s: str) -> List[str]:
        res=[]
        l=0
        r=1
        while l<len(s):
            while s[r]!="$":
                r+=1           
            n=int(s[l+1:r])            
            res.append(s[r+1:r+n+1])            
            l=r+n+1
            r=l+1
            
        
        return res
