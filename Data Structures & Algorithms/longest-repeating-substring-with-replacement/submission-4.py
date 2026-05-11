class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        windowHash = {} # Initialize with the first char
        most_common = s[l]
        while r < len(s):
            # Add rightmost char to hash or increment by 1
            if s[r] not in windowHash:
                windowHash[s[r]] = 1
            else:
                windowHash[s[r]] += 1

            # Update to see if rightmost char is the most common in the hash
            if windowHash[s[r]] >= windowHash[most_common]:
                most_common = s[r]
            
            # Check with k
            if k < (r + 1 - l) - windowHash[most_common]:
                windowHash[s[l]] -= 1
                l += 1
            r += 1
        return r - l

            