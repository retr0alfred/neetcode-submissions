class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        left, right, count, maxcount = 0, 0, 0, 0
        while right < len(s):
            while s[right] in check:
                check.remove(s[left])
                count -= 1
                left += 1
            count += 1
            maxcount = max(count, maxcount)
            check.add(s[right])
            right += 1
        return maxcount