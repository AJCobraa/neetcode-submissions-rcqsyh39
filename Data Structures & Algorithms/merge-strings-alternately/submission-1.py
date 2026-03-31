class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=0,0
        s=""
        w1,w2=len(word1),len(word2)
        while l<w1 and r<w2:
            s+=word1[l]+word2[r]
            l+=1
            r+=1
        return (s+word1[l:] if w1>w2 else s+word2[r:])
        