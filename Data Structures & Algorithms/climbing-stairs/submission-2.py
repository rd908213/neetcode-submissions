class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dp1 = 1
        dp2 = 2
        i = 2
        while i < n:
            dp3 = dp1 + dp2
            dp1 = dp2
            dp2 = dp3
            i += 1
        return(dp2)