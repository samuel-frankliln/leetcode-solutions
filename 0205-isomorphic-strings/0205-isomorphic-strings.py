class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        match={}
        if len(s)==0 and len(t)==0:
            return True
        if len(s)!= len(t):
            return False
        for i,a in enumerate(s):
            if a not in match.keys():
                match[a]=t[i]
            else:
                if match[a]!= t[i]:
                    return False
        return True
        