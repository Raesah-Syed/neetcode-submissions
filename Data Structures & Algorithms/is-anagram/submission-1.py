class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sd=Counter(s)
        td=Counter(t)
        return sd==td
            