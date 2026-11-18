class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = ''.join(char.lower() for char in s if char.isalnum())
        return val == val[::-1]