class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s.lower().split())
        checker = ''
        for i in s:
            if i.isalnum():
                checker += i
        if checker == checker[::-1]:
            return True
        return False