class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            x=s.index('#',i)

            l=int(s[i:x])
            res.append(s[x+1:x+1+l])

            i=x+1+l
        return res