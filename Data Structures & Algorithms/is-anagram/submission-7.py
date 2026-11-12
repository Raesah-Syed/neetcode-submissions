class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        td={}

        if len(s)!=len(t):
            return False
            
        for i in s:
            sd[i]=sd.get(i,0)+1
        
        for j in t:
            if j in sd:
                sd[j]-=1
                if sd[j]==0:
                    del sd[j]
            else:
                return False
        return True
            