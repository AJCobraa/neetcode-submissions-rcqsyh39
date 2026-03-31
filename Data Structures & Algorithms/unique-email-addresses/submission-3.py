class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d={}
        for i in emails:
            l,h=0,0
            word=""
            while i[l]!="@":
                if i[l]=="+" or h>0:
                    h+=1
                elif i[l]!="." and h==0:
                    word+=i[l]
                l+=1
            while l<len(i):
                word+=i[l]
                l+=1
            
            d[word]=d.get(word,0)+1
        print(d)
        
        return len(d)
        