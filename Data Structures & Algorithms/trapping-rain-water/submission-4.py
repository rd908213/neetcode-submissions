class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 # Classic two pointers
        lMax = height[l] # The maximum height seen by the left pointer
        rMax = height[r] # Max height seen by right pointer
        tot = 0 # Total water for the solution

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(height[l], lMax) # Check to see if this new height beats the old lMax
                tot += lMax - height[l]
            else: # if lMax >= rMax:
                r -= 1
                rMax = max(height[r], rMax) # Check to see if this new height beats the old rMax
                tot += rMax - height[r]

        return tot