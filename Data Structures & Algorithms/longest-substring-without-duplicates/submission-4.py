class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxcount, count = 0, 0
        lst = set()
        left, right = 0, 0
        while right < len(s):
            while s[right] in lst:
                lst.remove(s[left])
                left += 1
                count -= 1
            count += 1
            maxcount = max(count, maxcount)
            lst.add(s[right])
            right += 1
        return maxcount