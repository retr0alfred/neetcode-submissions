class Solution:
    def isPalindrome(self, s: str) -> bool:
        checker = ''.join(char.lower() for char in s if char.isalnum())
        return checker == checker[::-1]