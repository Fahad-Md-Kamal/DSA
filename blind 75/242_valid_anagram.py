class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tmpS, tmpT = {}, {}
        for idx in range(len(t)):
            tmpS[s[idx]] = 1 + tmpS.get(s[idx], 0)
            tmpT[t[idx]] =  1 + tmpT.get(t[idx], 0)
        
        for c in tmpS:
            if tmpS[c] != tmpT.get(c):
                return False
        return True

r = Solution().isAnagram("anagram", "nagaram")
print(r)