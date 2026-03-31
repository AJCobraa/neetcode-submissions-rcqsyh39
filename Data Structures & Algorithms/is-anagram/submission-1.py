class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.hashing(s)==self.hashing(t):
            return True
        else:
            return False
        
    def hashing(self,s: str) -> hash:
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        return dic
        
    