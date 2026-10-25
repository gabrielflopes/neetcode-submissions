class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        grupo = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in grupo:
                grupo.remove(s[left])
                left += 1
            grupo.add(s[right])
            longest = max(longest, right - left + 1)

        return longest