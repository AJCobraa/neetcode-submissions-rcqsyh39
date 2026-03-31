class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            codex=self.Codex.findagmCodex(i)
            d[tuple(codex)].append(i)
        return list(d.values())


    class Codex:
        def findagmCodex(s: str)->str:
            code=[0]*27
            for i in s:
                code[(ord(i)-ord("a"))]+=1
            return code
        