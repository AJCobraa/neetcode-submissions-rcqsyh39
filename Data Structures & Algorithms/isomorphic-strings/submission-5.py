class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t={}
        t_s={}
        for i in range(len(s)):
            if s[i] not in s_t:
                if t[i]in t_s:
                    return False
                s_t[s[i]]=t[i]
                t_s[t[i]]=s[i]
            else:
                if s_t[s[i]]!=t[i] or t_s[t[i]]!=s[i]:
                    return False
                

        return True


        