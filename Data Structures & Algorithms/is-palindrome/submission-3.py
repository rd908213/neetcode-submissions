class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new_s += s[i]
        pointer1 = 0
        pointer2 = -1
        for i in range(len(new_s)):
            if new_s[pointer1].lower() != new_s[pointer2].lower():
                return False
            else:
                pointer1 += 1
                pointer2 -= 1
        return True
                