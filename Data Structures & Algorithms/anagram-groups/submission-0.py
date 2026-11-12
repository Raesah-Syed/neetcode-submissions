from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        res=[]
        for s in strs:
            r="".join(sorted(list(s)))
            if r in d:
                d[r].append(s)
            else:
                d[r]=[s]
        for v in d.values():
            res.append(v)
        return res