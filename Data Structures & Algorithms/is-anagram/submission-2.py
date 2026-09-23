from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = dict(Counter(s))
        check2 = dict(Counter(t))
        if len(s) > len(t):
            for i in check1:
                if i not in check2 or check2[i] != check1[i]:
                    return False
        else:
            for i in check2:
                if i not in check1 or check1[i] != check2[i]:
                    return False
        return True
