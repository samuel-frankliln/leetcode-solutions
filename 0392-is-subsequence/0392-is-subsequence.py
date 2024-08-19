class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        if len(s) == 0:  # If s is empty, it is a subsequence of any string t
            return True

        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
            if i == len(s):  # All characters in s have been found in t
                return True

        return i == len(s)
