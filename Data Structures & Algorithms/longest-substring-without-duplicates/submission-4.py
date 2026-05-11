class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Two pointer approach. One starts at the beginning of
        # the current substring. The other at the end of the substring.
        # Substring held in a hash with the character and index.
        substr = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] in substr and substr[s[r]] >= l:
                l = substr[s[r]] + 1 # Jump the left pointer forward

            substr[s[r]] = r
            max_len = max(r - l + 1, max_len)
        return max_len