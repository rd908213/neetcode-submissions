class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = {}
        cur = {}
        for i in range(len(s)):
            try:
                if cur[s[i]]:
                    cur = {}
            except KeyError: # If the current letter is not in the current substring
                cur[s[i]] = i
                if len(cur) > len(res):
                    res = cur
        return len(res)